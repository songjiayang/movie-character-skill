# Couple Photos

Generate romantic or friendly couple portraits with various poses and backgrounds.

## Overview

Create couple photos (romantic or friendly) with two people using 12 different pose options and 6 background settings. The skill generates natural, authentic couple photos with coordinated outfits and appropriate atmospheres.

## Use Cases

- User wants romantic couple photos for anniversaries or celebrations
- User wants friendly photos with friends
- User wants to create memorable couple or friendship portraits
- User wants to generate social media content for two people

## Available Poses

| Pose | Description |
|-------|-------------|
| 并肩站立 | Two people standing side by side, shoulders touching |
| 面对面 | Two people facing each other, engaged in conversation |
| 揽肩拥抱 | One person's arm around other's shoulder, relaxed |
| 背对背 | Two people standing back to back, playful pose |
| 并肩而坐 | Two people seated together on bench or chair |
| 携手同行 | Walking together, holding hands |
| 手牵手面向镜头 | Holding hands facing camera, romantic |
| 背背抱 | Piggyback pose, playful and fun |
| 拥抱姿势 | Hugging each other, warm embrace |
| 额头相抵 | Foreheads touching, intimate moment |
| 坐地相拥 | Sitting on ground, cuddling |
| 舞动时刻 | Dancing together, dynamic pose |

To see complete list:
```bash
python scripts/main.py list-poses
```

## Available Backgrounds

| Background | Description |
|------------|-------------|
| 城市街头 | Urban street with cityscape backdrop |
| 公园自然 | Park with natural scenery, trees, flowers |
| 海滩日落 | Beach with sunset, warm golden light |
| 咖啡厅内 | Cozy cafe interior, ambient lighting |
| 屋顶天台 | Rooftop view with city skyline |
| 摄影棚简约 | Simple studio background, clean setup |

To see complete list:
```bash
python scripts/main.py list-backgrounds --scenario couple
```

## Couple Types

| Type | Description |
|------|-------------|
| 情侣合影 | Romantic couple, intimate moment, loving atmosphere |
| 朋友合影 | Best friends, friendly interaction, casual atmosphere |

## Command Examples

```bash
# Generate couple photos with default pose and background
python scripts/main.py generate --photos "photo1.jpg,photo2.jpg" --scenario couple

# Generate with specific pose
python scripts/main.py generate --photos "photo1.jpg,photo2.jpg" --scenario couple \
    --pose "手牵手面向镜头" \
    --non-interactive

# Generate with custom background
python scripts/main.py generate --photos "photo1.jpg,photo2.jpg" --scenario couple \
    --pose "手牵手面向镜头" \
    --background "海滩日落" \
    --non-interactive

# Generate multiple variations
python scripts/main.py generate --photos "photo1.jpg,photo2.jpg" --scenario couple \
    --pose "并肩站立" \
    --count 4 \
    --non-interactive
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|-------|-----------|-------------|
| `--photos` | paths | Yes | Comma-separated photo paths (2 photos required) |
| `--pose` | string | No | Specific pose name (default: 并肩站立) |
| `--background` | string | No | Background name (default: pose's built-in scene) |
| `--count, -c` | number | No | Number of images (default: 4) |
| `--scenario, -s` | string | Yes | Scenario type: `couple` |
| `--non-interactive, -ni` | flag | No | Run in non-interactive mode |

## Pose Selection Guide

### Romantic Poses
- 手牵手面向镜头 - Romantic, intimate
- 拥抱姿势 - Warm, loving
- 额头相抵 - Intimate connection
- 坐地相拥 - Cozy, romantic

### Friendly Poses
- 并肩站立 - Casual, friendly
- 面对面 - Conversation, friendly
- 揽肩拥抱 - Affectionate friendship
- 携手同行 - Walking together

### Playful Poses
- 背对背 - Fun, playful
- 背背抱 - Playful piggyback
- 舞动时刻 - Dynamic, energetic

## Best Practices

1. **Use both photos**: Both people's photos are required for best results
2. **Coordinate outfits**: Wear complementary colors or styles
3. **Match pose to mood**: Choose romantic poses for couples, friendly for friends
4. **Consider background**: Select background that matches the atmosphere
5. **Photo quality**: Use clear, well-lit photos ≥1024×1024
6. **Natural expressions**: Photos with natural smiles work best

## Attire Recommendations

Each pose includes attire recommendations for natural, coordinated looks:

- **Side by side**: Casual outfits, matching colors
- **Facing each other**: Complementary outfits, soft fabrics
- **Arm around shoulder**: Relaxed casual wear, comfortable clothing
- **Back to back**: Sporty or casual, activewear
- **Seated together**: Comfortable clothing for sitting
- **Holding hands**: Romantic coordinated outfits
- **Piggyback**: Playful casual wear
- **Hugging**: Soft, comfortable fabrics
- **Forehead touch**: Intimate coordinated outfits
- **Sitting**: Cozy, relaxed clothing
- **Dancing**: Flowing or comfortable movement-friendly wear
