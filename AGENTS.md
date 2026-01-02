# AGENTS.md

This file provides guidance for agentic coding assistants working on this repository.

## Build/Lint/Test Commands

**Note:** This project currently has no automated testing or linting infrastructure configured.

### Running Tests
```bash
# No test framework configured. To add tests:
# 1. Install pytest: pip install pytest pytest-cov
# 2. Create test files: scripts/test_*.py
# 3. Run all tests: pytest scripts/
# 4. Run single test: pytest scripts/test_module.py::test_function

# To test the main CLI manually:
python scripts/main.py generate --help
python scripts/main.py list-scenarios
python scripts/main.py list-styles --scenario portrait
```

### Linting
```bash
# No linter configured. Recommended tools:
# Install pylint: pip install pylint
# Run lint: pylint scripts/
# Install black: pip install black
# Format code: black scripts/
# Install mypy: pip install mypy
# Type check: mypy scripts/
```

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Set API key (required for operation)
export ARK_API_KEY="your_api_key_here"

# Mock mode for testing without API
export MOCK_API="true"
```

## Code Style Guidelines

### File Structure
- Entry point: `scripts/main.py` (CLI with argparse subcommands)
- Core modules: `scripts/config.py`, `scripts/interaction.py`, `scripts/image_generator.py`
- Data files: `data/*.json` (scenarios, styles, poses, templates, characters)
- Output: `output/images/`, `temp/`, `logs/` (auto-generated)

### Import Order
1. Standard library (sys, os, json, time, argparse, pathlib)
2. Third-party libraries (requests, cv2, numpy, PIL)
3. Local imports (from config import config, from interaction import InteractionManager)

```python
import sys
import os
import json
from pathlib import Path

import requests
import cv2
import numpy as np

from config import config
from interaction import InteractionManager
```

### Formatting
- Indentation: 4 spaces
- Strings: Single quotes for code, double quotes for user-facing text
- Line length: Keep readable, typically under 100-120 characters
- Blank lines: Between methods and logical sections
- Use shebang: `#!/usr/bin/env python3` at top of main.py

### Type Hints
Use type hints from `typing` module in function signatures:
```python
from typing import List, Dict, Optional

def generate_images(self, photos: List[str], count: int) -> Optional[List[str]]:
    """Generate images with type hints for parameters and return values"""
    pass
```

### Naming Conventions
- **Classes**: PascalCase (`Config`, `InteractionManager`, `ImageGenerator`)
- **Functions/Methods**: snake_case (`generate_single_image`, `load_config`)
- **Variables**: snake_case (`user_photo_path`, `image_count`)
- **Constants**: UPPER_SNAKE_CASE (`DEFAULT_DATA_DIR`, `DEFAULT_TEMP_DIR`)
- **Private methods**: Leading underscore (`_load_state`, `_save_config`)
- **Boolean variables**: Prefix with `is_`/`has_` (`is_valid`, `has_error`)

### Error Handling
- Use specific exception types in try-except blocks
- Return None on errors for functions that return values
- Print error messages to stdout with emoji prefixes (❌, ⚠️, ✅)
- Catch specific exceptions: `json.JSONDecodeError`, `ValueError`, `IOError`, `requests.exceptions.RequestException`
- Always validate file paths with `Path(path).exists()`

```python
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f"❌ Invalid JSON: {e}")
    return None
except IOError as e:
    print(f"❌ File error: {e}")
    return None
```

### Documentation
- Use triple double-quotes for docstrings
- Document classes and public methods
- Include Args and Returns sections for complex functions
- Add inline comments for complex logic
- Use emojis in user-facing print statements (📷, ✅, ❌, ⚠️)

```python
def generate_single_image(self, user_photo: str, character: Dict, index: int) -> Optional[str]:
    """Generate a single image with the given character using Seedream 4.5 API
    
    Args:
        user_photo: Path to user's reference photo
        character: Character dictionary with name, prompt, scene
        index: Image index for filename generation
    
    Returns:
        Path to generated image file, or None if generation fails
    """
    pass
```

### Path Handling
- Always use `pathlib.Path` for file operations
- Use relative paths in config, resolve to absolute paths at runtime
- Ensure directories exist with `mkdir(parents=True, exist_ok=True)`
- Use `str(path)` when passing to external functions expecting strings

```python
from pathlib import Path

def get_output_path(self, filename: str) -> Path:
    output_dir = Path(self.config.config["paths"]["output_dir"]) / "images"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / filename
```

### API Integration
- Handle timeouts (default 120s for image generation)
- Implement retry logic for transient failures
- Use mock mode for testing without API calls
- Validate API responses before processing
- Rate limit between requests (2-3 second delay)

```python
# Mock mode for testing
self.mock_mode = os.getenv("MOCK_API", "false").lower() == "true"

# API request with timeout and error handling
try:
    response = requests.post(self.api_url, json=payload, timeout=120)
    response.raise_for_status()
    return self._process_response(response.json())
except requests.exceptions.Timeout:
    print(f"⚠️ Timeout error")
    return None
```

### JSON Handling
- Always use `encoding='utf-8'` when opening files
- Use `indent=2, ensure_ascii=False` for readable JSON
- Validate JSON structure before accessing keys
- Use `json.dump()` for writing, `json.load()` for reading

```python
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

### Configuration Management
- Store settings in `config.json`
- Use environment variables for secrets (API keys)
- Provide defaults for all configuration values
- Support both relative and absolute paths
- Maintain backward compatibility with old config formats

### CLI Design
- Use argparse with subcommands for complex CLIs
- Provide `--help` for all commands
- Support `--non-interactive` mode for agent integration
- Use clear argument names with short options
- Show progress for long-running operations

### State Management
- Persist state in JSON files in `temp/` directory
- Save state after significant changes
- Load state on startup to resume operations
- Clean up temporary files after completion

### Image Processing
- Use OpenCV (cv2) for image operations
- Resize to max 2048x2048 for API requirements
- Use high-quality interpolation (cv2.INTER_LANCZOS4)
- Save as JPEG with quality 95+
- Validate generated images (check size, blurriness)

```python
# Resize image while maintaining aspect ratio
max_size = 2048
if max(h, w) > max_size:
    scale = max_size / max(h, w)
    img = cv2.resize(img, (int(w*scale), int(h*scale)), interpolation=cv2.INTER_LANCZOS4)
```

### OOP Design Principles

**Encapsulation:**
- Hide implementation details with private methods (prefix `_`)
- Use properties for computed attributes instead of getter methods
- Keep class internals private, expose only necessary public interface
- Avoid global mutable state; use dependency injection instead

```python
class ImageGenerator:
    def __init__(self, config: Config, interaction: InteractionManager):
        self._config = config  # Private attribute
        self._interaction = interaction
        self.api_key = config.get_api_key()  # Public readonly
    
    @property
    def image_dir(self) -> Path:
        """Computed property for image directory"""
        return Path(self._config.config["paths"]["output_dir"]) / "images"
```

**Inheritance & Polymorphism:**
- Create base classes for common functionality
- Use abstract base classes (ABC) for interfaces
- Override methods in subclasses to specialize behavior
- Favor composition over inheritance when appropriate

```python
from abc import ABC, abstractmethod

class BaseScenario(ABC):
    """Base class for all generation scenarios"""
    
    def __init__(self, config: Config, interaction: InteractionManager):
        self._config = config
        self._interaction = interaction
    
    @abstractmethod
    def collect_inputs(self) -> Dict:
        """Collect scenario-specific inputs"""
        pass
    
    @abstractmethod
    def generate_images(self, photos: List[str], **kwargs) -> List[str]:
        """Generate images for this scenario"""
        pass

class PortraitScenario(BaseScenario):
    """Portrait photo generation scenario"""
    
    def collect_inputs(self) -> Dict:
        # Portrait-specific input collection
        pass
    
    def generate_images(self, photos: List[str], **kwargs) -> List[str]:
        # Portrait-specific generation logic
        pass
```

**Single Responsibility Principle:**
- Each class should have one reason to change
- Each method should do one thing well
- Separate data access, business logic, and presentation

**Dependency Injection:**
- Pass dependencies through constructors
- Avoid creating dependencies inside methods
- Makes testing easier and code more maintainable

### Function Complexity Control

**Maximum Complexity Guidelines:**
- Function length: ≤ 50 lines (ideal), ≤ 100 lines (absolute maximum)
- Cyclomatic complexity: ≤ 10
- Nesting depth: ≤ 4 levels
- Parameters: ≤ 7 parameters (use dataclasses for more)

**Refactoring Strategies:**

```python
# BAD: Too long, too complex
def generate_all_images(self, user_photo: str, characters: List[Dict]) -> List[str]:
    # 200+ lines of mixed concerns
    # - preprocessing
    # - API calls
    # - validation
    # - error handling
    # - state updates
    pass

# GOOD: Broken down into focused methods
def generate_all_images(self, user_photo: str, characters: List[Dict]) -> List[str]:
    """Generate images for all characters"""
    processed_photo = self._preprocess_photo(user_photo)
    return self._generate_and_track_images(processed_photo, characters)

def _preprocess_photo(self, photo: str) -> str:
    """Preprocess single photo for generation"""
    pass

def _generate_and_track_images(self, photo: str, chars: List[Dict]) -> List[str]:
    """Generate images with state tracking"""
    pass

def _generate_single_image(self, photo: str, char: Dict, index: int) -> Optional[str]:
    """Generate single image with error handling"""
    pass
```

**Extract Method Pattern:**
- Extract repeated logic into separate methods
- Give methods descriptive names that explain "what" not "how"
- Keep methods at the same abstraction level

```python
# Extract complex conditions
if (user_photo and Path(user_photo).exists() and 
    self._validate_photo_format(user_photo) and 
    self._check_photo_resolution(user_photo)):
    # do something

# Better
if self._is_valid_photo(user_photo):
    # do something

def _is_valid_photo(self, photo: str) -> bool:
    """Check if photo is valid for generation"""
    if not photo or not Path(photo).exists():
        return False
    return (self._validate_photo_format(photo) and 
            self._check_photo_resolution(photo))
```

### Avoid Code Duplication

**DRY Principle (Don't Repeat Yourself):**
- Extract repeated code into methods or functions
- Use inheritance for shared behavior
- Create utility modules for common operations
- Use configuration over hardcoded values

**Template Method Pattern:**
- Define algorithm skeleton in base class
- Override specific steps in subclasses
- Common pattern for scenario generation

```python
# BAD: Duplicated generation logic in multiple methods
def generate_portrait_images(self, photo, styles, count):
    for i in range(count):
        prompt = self._build_prompt(...)
        payload = self._build_payload(prompt)
        response = self._make_request(payload)
        self._save_image(response, filename)
        time.sleep(2)

def generate_couple_images(self, photos, pose, count):
    for i in range(count):
        prompt = self._build_prompt(...)
        payload = self._build_payload(prompt)
        response = self._make_request(payload)
        self._save_image(response, filename)
        time.sleep(2)

# GOOD: Use template method
class BaseGenerator(ABC):
    def generate_batch(self, count: int) -> List[str]:
        """Template method for batch generation"""
        results = []
        for i in range(count):
            result = self._generate_single(i)
            if result:
                results.append(result)
            self._rate_limit_delay()
        return results
    
    @abstractmethod
    def _generate_single(self, index: int) -> Optional[str]:
        """Generate single image"""
        pass
    
    def _rate_limit_delay(self):
        """Rate limiting between requests"""
        time.sleep(2)
```

**Strategy Pattern:**
- Encapsulate interchangeable algorithms
- Use for different validation strategies
- Good for prompt building strategies

```python
class PromptStrategy(ABC):
    @abstractmethod
    def build(self, **kwargs) -> str:
        pass

class PortraitPromptStrategy(PromptStrategy):
    def build(self, style, **kwargs) -> str:
        # Build portrait-specific prompt
        pass

class CouplePromptStrategy(PromptStrategy):
    def build(self, pose, background, **kwargs) -> str:
        # Build couple-specific prompt
        pass

class ImageGenerator:
    def __init__(self, prompt_strategy: PromptStrategy):
        self._prompt_strategy = prompt_strategy
    
    def generate(self, **kwargs):
        prompt = self._prompt_strategy.build(**kwargs)
        # Use prompt for generation
```

**Utility Functions:**
- Create `utils.py` for common operations
- Extract repeated file operations
- Share validation logic across modules

```python
# scripts/utils.py
def validate_image_path(path: str) -> bool:
    """Validate image file exists and is readable"""
    if not path or not Path(path).exists():
        return False
    try:
        img = cv2.imread(path)
        return img is not None
    except Exception:
        return False

def resize_image(img: np.ndarray, max_size: int) -> np.ndarray:
    """Resize image while maintaining aspect ratio"""
    h, w = img.shape[:2]
    if max(h, w) <= max_size:
        return img
    scale = max_size / max(h, w)
    return cv2.resize(img, (int(w*scale), int(h*scale)), 
                     interpolation=cv2.INTER_LANCZOS4)

def encode_image_to_base64(path: str) -> str:
    """Encode image file to base64 string"""
    with open(path, "rb") as f:
        image_data = f.read()
    base64_str = base64.b64encode(image_data).decode('utf-8')
    return f"data:image/jpeg;base64,{base64_str}"
```

**Configuration-Driven Behavior:**
- Move hardcoded values to config files
- Use data files for scenario-specific logic
- Avoid switch-like if-else chains

```python
# BAD: Hardcoded scenario logic
if scenario_type == 'portrait':
    required = 1
    max_photos = 1
elif scenario_type == 'couple':
    required = 2
    max_photos = 2
elif scenario_type == 'family':
    required = 1
    max_photos = 6

# GOOD: Load from configuration
scenario = self.config.get_scenario(scenario_type)
required = scenario['required_photos']
max_photos = scenario['max_photos']
```

### Code Quality Metrics

When refactoring, aim for:
- **Cyclomatic complexity**: < 10 per function
- **Lines per function**: 20-50 lines average
- **Parameters**: < 7 (use dataclasses/kwargs for more)
- **Nesting depth**: < 4 levels
- **Duplicate code**: < 5% of codebase
- **Test coverage**: Aim for 80%+ (when tests are added)

Use tools to measure:
```bash
# Install complexity checker
pip install radon

# Check complexity
radon cc scripts/ -a -s

# Check maintainability
radon mi scripts/ -s

# Check for duplicates
pip install duplicate-code-detector
```

## Important Notes

1. **No tests configured**: Add pytest infrastructure before writing tests
2. **No linter configured**: Consider adding pylint/black/mypy
3. **API key required**: Set `ARK_API_KEY` environment variable or use mock mode
4. **Mock mode available**: Set `MOCK_API=true` for testing without API calls
5. **Entry point**: Always `scripts/main.py` for CLI operations
6. **Encoding**: Always use UTF-8 for JSON and text files
7. **Paths**: Prefer pathlib over os.path
8. **Error messages**: Use emoji prefixes and print to stdout
9. **Type hints**: Use typing module for better code clarity
10. **Documentation**: Add docstrings to all public classes and methods
