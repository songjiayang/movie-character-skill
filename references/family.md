# Family Photos

Generate professional family group photos with various templates and backgrounds.

## Overview

Create family portraits (3-6 people) with 8 different template options and 6 background settings. The skill generates natural, warm family photos with coordinated attire and appropriate atmospheres.

## Use Cases

- User wants professional family portraits for holidays or events
- User wants casual family photos for albums
- User wants to capture multi-generational family moments
- User wants to create memorable family group photos

## Available Templates

| Template | Description | People |
|----------|-------------|---------|
| 经典全家福 | Classic family portrait, formal attire, elegant pose | 3-6 |
| 温馨家庭聚会 | Casual family photo, relaxed postures, authentic moment | 3-6 |
| 户外家庭照 | Family photo outdoors, natural setting, sunlight | 3-6 |
| 多代同堂 | Grandparents, parents, children, warm family bonds | 4-6 |
| 活泼家庭照 | Playful family photo, dynamic poses, energetic | 3-6 |
| 坐姿全家福 | Seated family portrait, comfortable arrangement | 3-6 |
| 专业摄影棚全家福 | Professional studio family, controlled lighting | 3-6 |
| 节日家庭照 | Holiday family photo, festive atmosphere | 3-6 |

To see complete list:
```bash
python scripts/main.py list-templates
```

## Available Backgrounds

| Background | Description |
|------------|-------------|
| 正式客厅 | Formal living room, elegant furniture |
| 温馨家庭内景 | Cozy home interior, comfortable setting |
| 专业摄影棚 | Professional studio, clean backdrop |
| 户外公园 | Outdoor park, natural scenery |
| 海滩风景 | Beach seaside, coastal scenery |
| 花园花卉 | Garden with flowers, floral backdrop |

To see complete list:
```bash
python scripts/main.py list-backgrounds --scenario family
```

## Command Examples

```bash
# Generate family photos with default template and background
python scripts/main.py generate --photos "photo1.jpg,photo2.jpg,photo3.jpg" --scenario family

# Generate with specific template
python scripts/main.py generate --photos "photo1.jpg,photo2.jpg,photo3.jpg" --scenario family \
    --template "温馨家庭聚会" \
    --non-interactive

# Generate with custom background
python scripts/main.py generate --photos "photo1.jpg,photo2.jpg,photo3.jpg" --scenario family \
    --template "温馨家庭聚会" \
    --background "户外公园" \
    --non-interactive

# Generate with 5 family members
python scripts/main.py generate --photos "p1.jpg,p2.jpg,p3.jpg,p4.jpg,p5.jpg" --scenario family \
    --template "经典全家福" \
    --non-interactive
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|-------|-----------|-------------|
| `--photos` | paths | Yes | Comma-separated photo paths (1-6 photos) |
| `--template` | string | No | Specific template name (default: 经典全家福) |
| `--background` | string | No | Background name (default: template's built-in scene) |
| `--count, -c` | number | No | Number of images (default: 4) |
| `--scenario, -s` | string | Yes | Scenario type: `family` |
| `--non-interactive, -ni` | flag | No | Run in non-interactive mode |

## Template Selection Guide

### Formal Occasions
- 经典全家福 - Traditional family events, formal portraits
- 专业摄影棚全家福 - Professional family portraits
- 多代同堂 - Generational family photos, special celebrations

### Casual & Everyday
- 温馨家庭聚会 - Everyday family moments, casual photos
- 户外家庭照 - Outdoor activities, family outings
- 活泼家庭照 - Playful, energetic family moments

### Special Occasions
- 节日家庭照 - Holiday celebrations, seasonal photos
- 坐姿全家福 - Comfortable family gathering, relaxed portraits

## Best Practices

1. **Provide all family photos**: Include all family members (1-6 photos)
2. **Coordinate attire**: Choose matching colors or complementary styles
3. **Match template to occasion**: Formal templates for special events, casual for everyday
4. **Select appropriate background**: Indoor backgrounds for formal, outdoor for casual
5. **Photo quality**: Use clear, well-lit photos ≥1024×1024
6. **Natural expressions**: Photos with natural smiles work best

## Photo Guidelines

### Photo Requirements
- **Minimum**: 1 photo (for reference)
- **Maximum**: 6 photos (one per family member)
- **Recommended**: Individual photos of each family member
- **Resolution**: ≥1024×1024 for best results

### Attire Recommendations

Each template includes specific attire suggestions:

**Classic Family Portrait** (经典全家福):
- Coordinated formal or semi-formal clothing
- Matching color palette or style
- Suits, dresses, or elegant outfits

**Casual Family Gathering** (温馨家庭聚会):
- Coordinated casual clothing
- Comfortable casual shirts, sweaters, or relaxed outfits
- Natural and cozy together

**Outdoor Family** (户外家庭照):
- Outdoor-appropriate clothing
- Casual wear, light jackets, or comfortable outfits
- Suitable for outdoor activities

**Multigenerational Family** (多代同堂):
- Formal or semi-formal clothing appropriate for all ages
- Traditional or classic styles
- Respectful of family traditions

## Background Matching

### Formal Templates
- 经典全家福 → 正式客厅, 专业摄影棚
- 专业摄影棚全家福 → 专业摄影棚
- 多代同堂 → 正式客厅, 温馨家庭内景

### Casual Templates
- 温馨家庭聚会 → 温馨家庭内景
- 户外家庭照 → 户外公园, 海滩风景, 花园花卉
- 活泼家庭照 → 户外公园, 花园花卉
- 坐姿全家福 → 温馨家庭内景, 咖啡厅内

### Special Occasions
- 节日家庭照 → 温馨家庭内景, 花园花卉 (seasonally appropriate)
