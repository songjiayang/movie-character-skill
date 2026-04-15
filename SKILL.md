---
name: photo-studio-skill
description: "Generate professional AI-enhanced photos using ByteDance Seedream 4.5 model. Use when users want to, (1) Create portraits with various styles, (2) Generate couple or family group photos, (3) Take photos with movie characters, (4) Edit images (change clothing, background, material, style), (5) Merge multiple photos (outfit fusion, person-scenery fusion, brand design), (6) Create series of related images (seasons, character states, story sequences), (7) Design posters (movie, event, product), or (8) Use custom prompts with full creative control."
---

# Photo Studio

Generate professional AI-enhanced portraits and group photos using Seedream 4.5 AI model.

## Quick Start

```bash
# Interactive mode - easiest way to start
python scripts/main.py generate --photo path/to/your/photo.jpg

# Non-interactive mode - for agent integration
python scripts/main.py generate --photo "$USER_PHOTO" --scenario portrait --non-interactive
```

## Core Workflow

1. **Select scenario** from 9 options: celebrity, portrait, couple, family, edit, fusion, series, poster, free
2. **Provide inputs**: photos, styles, templates, prompts based on scenario
   - **Validate**: Ensure photos exist and meet minimum resolution (≥1024×1024). Check with `python scripts/main.py config --show` that `ARK_API_KEY` is configured
3. **Generate images**: CLI preprocesses photos, calls Seedream 4.5 API, saves results to `output/images/`
   - **Validate**: Check `logs/` for errors if generation fails. Verify output files exist in `output/images/` before proceeding
4. **Review and save**: View, reorder, regenerate, or confirm images

## Essential Commands

### Generate Images

```bash
# Celebrity photos with characters
python scripts/main.py generate --photo "$USER_PHOTO" --scenario celebrity --non-interactive

# Portrait photos with style
python scripts/main.py generate --photo "$USER_PHOTO" --scenario portrait --style "职业商务照" --non-interactive

# Couple photos with pose and background
python scripts/main.py generate --photos "$PHOTO1,$PHOTO2" --scenario couple --pose "手牵手面向镜头" --background "海滩日落" --non-interactive

# Family photos with template
python scripts/main.py generate --photos "$PHOTO1,$PHOTO2,$PHOTO3" --scenario family --template "温馨家庭聚会" --non-interactive

# Edit images (change clothing, material, background, style, enhance)
python scripts/main.py generate --photo "$USER_PHOTO" --scenario edit --template change-clothing --clothing "运动外套" --non-interactive

# Fuse images (outfit, person-scenery, brand, multi-person)
python scripts/main.py generate --photos "$PHOTO1,$PHOTO2" --scenario fusion --template outfit-fusion --non-interactive

# Create series (seasons, brand kit, character states, story sequence)
python scripts/main.py generate --photo "$USER_PHOTO" --scenario series --template seasons --count 4 --non-interactive

# Design poster (movie, event, product)
python scripts/main.py generate --photo "$USER_PHOTO" --scenario poster --template movie-poster --non-interactive

# Free mode with custom prompt
python scripts/main.py generate --photo "$USER_PHOTO" --scenario free --prompt "A futuristic cyberpunk portrait" --non-interactive
```

### List Available Options

```bash
# List all scenarios
python scripts/main.py list-scenarios

# List styles for portrait/couple/family/celebrity
python scripts/main.py list-styles --scenario <scenario_id>

# List couple poses
python scripts/main.py list-poses

# List family templates
python scripts/main.py list-templates

# List backgrounds for couple/family
python scripts/main.py list-backgrounds --scenario <scenario_id>

# List characters
python scripts/main.py list-characters
```

### Configuration and Utilities

```bash
# View configuration
python scripts/main.py config --show

# Update configuration
python scripts/main.py config --set generation.default_image_count=3

# Add custom character
python scripts/main.py add-character "Character Name" "Description" --scene "Scene"

# Clean temporary files
python scripts/main.py cleanup
```

## Scenarios Overview

| Scenario | Photos Required | Key Options |
|----------|----------------|-------------|
| Celebrity | 1 | characters, count |
| Portrait | 1 | style, count |
| Couple | 2 | pose, background, count |
| Family | 1-6 | template, background, count |
| Edit | 1 | template (5 options), template-specific params |
| Fusion | 1-6 | template (4 options), template-specific params |
| Series | 1 | template (4 options), count (4/6/8/10) |
| Poster | 1 | template (3 options), template-specific params |
| Free | 1-14 | prompt, negative-prompt, count |

## Environment Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key (required for operation)
export ARK_API_KEY="your_key_here"

# Mock mode for testing without API (optional)
export MOCK_API=true
```

## Configuration

Key settings in `config.json`:
- `generation.image_width` / `generation.image_height` - Image dimensions (default: 2048)
- `generation.default_image_count` - Default number of images (default: 5)
- `scenarios.default_scenario` - Default scenario (default: celebrity)

## References

Load these reference files when working with specific features:

**Feature Modules:**
- **[references/celebrity.md](references/celebrity.md)** - Celebrity photos with movie characters
- **[references/portrait.md](references/portrait.md)** - Professional personal portraits with various styles
- **[references/couple.md](references/couple.md)** - Couple or friend portraits with poses and backgrounds
- **[references/family.md](references/family.md)** - Family group photos with templates
- **[references/edit.md](references/edit.md)** - Image editing (clothing, material, background, style, enhancement)
- **[references/fusion.md](references/fusion.md)** - Multi-photo fusion (outfit, person-scenery, brand, composite)
- **[references/series.md](references/series.md)** - Series creation (seasons, brand kit, character states, story)
- **[references/poster.md](references/poster.md)** - Poster design (movie, event, product)
- **[references/free.md](references/free.md)** - Free mode with custom prompts

## Technical Notes

- **Model**: Seedream 4.5 (`doubao-seedream-4.5-251128`), resolution 2048x2048 (configurable)
- **Reference photos**: Supports 1-14 per generation using image-to-image synthesis
- **Multi-photo scenarios**: Couple and family use multi-reference fusion; person count is prompt-controlled (approximate)
- **Mock mode**: Set `MOCK_API=true` to test without API calls or costs
