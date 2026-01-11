"""
Configuration module for movie character skill
"""

import os
import json
from pathlib import Path

# Default directory names (relative to skill directory)
DEFAULT_DATA_DIR = "data"
DEFAULT_TEMP_DIR = "temp"
DEFAULT_OUTPUT_DIR = "output"
DEFAULT_LOGS_DIR = "logs"


class Config:
    """Configuration manager for skill

    This class manages configuration with portable relative paths.
    Paths in config.json can be either:
    - Relative paths (recommended): "temp", "output", "logs"
    - Absolute paths: "/full/path/to/directory"

    The class resolves paths relative to skill directory.
    """

    def __init__(self, skill_dir=None):
        """
        Initialize configuration manager.

        Args:
            skill_dir: Path to skill directory. If None, auto-detected from script location.
        """
        self.skill_dir = Path(skill_dir) if skill_dir else Path(__file__).resolve().parent.parent
        self.config_file = self.skill_dir / "config.json"
        self.default_characters_file = self.skill_dir / DEFAULT_DATA_DIR / "default_characters.json"

        # Ensure directories exist
        self._ensure_directories()

        # Load or create config
        self.config = self._load_config()

        # Load default characters
        self.default_characters = self._load_default_characters()

    def _ensure_directories(self):
        """Ensure all required directories exist"""
        for dir_name in [DEFAULT_DATA_DIR, DEFAULT_TEMP_DIR, DEFAULT_OUTPUT_DIR, DEFAULT_LOGS_DIR]:
            (self.skill_dir / dir_name).mkdir(exist_ok=True)

    def _resolve_path(self, path_value):
        """
        Resolve a path value to absolute path.

        Args:
            path_value: Either a relative path (str) or absolute path (str starting with /)

        Returns:
            Path: Resolved absolute path
        """
        if not path_value:
            return self.skill_dir

        path = Path(path_value)

        # If it's an absolute path, use it directly
        if path.is_absolute():
            return path

        # If it's a relative path, resolve from skill directory
        return (self.skill_dir / path).resolve()

    def get_temp_dir(self):
        """Get absolute path to temp directory"""
        path_value = self.config.get("paths", {}).get("temp_dir", DEFAULT_TEMP_DIR)
        return self._resolve_path(path_value)

    def get_output_dir(self):
        """Get absolute path to output directory"""
        path_value = self.config.get("paths", {}).get("output_dir", DEFAULT_OUTPUT_DIR)
        return self._resolve_path(path_value)

    def get_logs_dir(self):
        """Get absolute path to logs directory"""
        path_value = self.config.get("paths", {}).get("logs_dir", DEFAULT_LOGS_DIR)
        return self._resolve_path(path_value)

    @property
    def temp_dir(self):
        """Property for temp directory (backward compatibility)"""
        return self.get_temp_dir()

    @property
    def image_dir(self):
        """Get absolute path to images output directory"""
        return self.get_output_dir() / "images"

    @property
    def video_dir(self):
        """Get absolute path to video output directory (for future use)"""
        return self.get_output_dir() / "videos"

    def _load_config(self):
        """Load configuration from file or create default with relative paths"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)

                # Ensure required fields exist
                if "characters" not in config:
                    config["characters"] = []
                if "paths" not in config:
                    config["paths"] = {
                        "temp_dir": DEFAULT_TEMP_DIR,
                        "output_dir": DEFAULT_OUTPUT_DIR,
                        "logs_dir": DEFAULT_LOGS_DIR
                    }
                if "generation" not in config:
                    config["generation"] = self._get_default_generation_config()

                # Save updated config if fields were added
                self._save_config(config)
                return config
            except json.JSONDecodeError:
                print(f"Warning: Config file {self.config_file} is corrupted. Using defaults.")

        # Default configuration with RELATIVE paths (portable)
        default_config = {
            "api": self._get_default_api_config(),
            "paths": {
                "temp_dir": DEFAULT_TEMP_DIR,
                "output_dir": DEFAULT_OUTPUT_DIR,
                "logs_dir": DEFAULT_LOGS_DIR
            },
            "generation": self._get_default_generation_config(),
            "characters": []
        }

        # Save default config
        self._save_config(default_config)
        return default_config

    def _get_default_api_config(self) -> dict:
        """Get default API configuration"""
        return {
            "image_generation_url": "https://ark.cn-beijing.volces.com/api/v3/images/generations"
        }

    def _get_default_generation_config(self) -> dict:
        """Get default generation configuration"""
        return {
            "default_image_count": 1,
            "max_image_count": 10,
            "image_width": 1440,
            "image_height": 2560,
            "image_model": "doubao-seedream-4-5-251128"
        }

    def _load_default_characters(self):
        """Load default movie characters from data file"""
        if self.default_characters_file.exists():
            try:
                with open(self.default_characters_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass

        # Return empty list if file doesn't exist or is invalid
        return []

    def get_all_scenarios(self):
        """Get all available scenarios from scenarios.json"""
        scenarios_config_file = self.skill_dir / "data" / self.config.get("scenarios", {}).get("config_file", "scenarios.json")

        if not scenarios_config_file.exists():
            # Fallback to old format (single celebrity scenario)
            return [{
                "id": "celebrity",
                "name": "明星合影",
                "description": "与电影明星拍照留念",
                "input_type": "single_photo",
                "required_photos": 1,
                "max_photos": 1,
                "data_file": "default_characters.json"
            }]

        try:
            with open(scenarios_config_file, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                return config_data.get("scenarios", [])
        except (json.JSONDecodeError, IOError):
            # Fallback to old format
            return [{
                "id": "celebrity",
                "name": "明星合影",
                "description": "与电影明星拍照留念",
                "input_type": "single_photo",
                "required_photos": 1,
                "max_photos": 1,
                "data_file": "default_characters.json"
            }]

    def get_scenario(self, scenario_id):
        """Get a specific scenario by ID"""
        scenarios = self.get_all_scenarios()
        for scenario in scenarios:
            if scenario.get("id") == scenario_id:
                return scenario
        return None

    def get_scenario_data(self, scenario_id):
        """Get scenario data file content (styles, poses, templates, or characters)"""
        scenario = self.get_scenario(scenario_id)
        if not scenario:
            return None

        data_file = scenario.get("data_file")
        if not data_file:
            return None

        data_file_path = self.skill_dir / "data" / data_file

        if not data_file_path.exists():
            return None

        try:
            with open(data_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Extract styles, poses, templates, or characters based on file type
            if "styles" in data:
                return data["styles"]
            elif "poses" in data:
                return data["poses"]
            elif "templates" in data:
                return data["templates"]
            else:
                # Assume it's a characters list (backward compatible)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, IOError):
            return None

    def get_backgrounds(self, scenario_id):
        """Get background options for a scenario"""
        data_file = None
        if scenario_id == 'couple':
            data_file = self.skill_dir / "data" / "couple_poses.json"
        elif scenario_id == 'family':
            data_file = self.skill_dir / "data" / "family_templates.json"
        else:
            return None

        if not data_file or not data_file.exists():
            return None

        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("backgrounds", [])
        except (json.JSONDecodeError, IOError):
            return None

    def _save_config(self, config=None):
        """Save configuration to file"""
        config = config or self.config
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

    def get_api_key(self, api_name=None):
        """
        Get API credentials from environment variable
        Retrieves API key for image generation service
        """
        return os.getenv("ARK_API_KEY")

    def add_character(self, name, prompt, scene=None):
        """Add a custom character"""
        character = {
            "name": name,
            "prompt": prompt,
            "scene": scene or "movie theater setting, cinematic photo"
        }

        self.config["characters"].append(character)
        self._save_config()
        return character

    def get_characters(self, use_defaults=True):
        """Get list of characters (custom + defaults)"""
        characters = self.config["characters"].copy()
        if use_defaults:
            characters.extend(self.default_characters)
        return characters

    def update_setting(self, section, key, value):
        """Update a configuration setting"""
        if section in self.config and key in self.config[section]:
            self.config[section][key] = value
            self._save_config()
            return True
        return False


# Global configuration instance
config = Config()
