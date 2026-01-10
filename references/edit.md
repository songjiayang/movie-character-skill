# Image Editing

Edit existing photos with 5 professional editing templates.

## Overview

Modify photos while preserving original subjects with 5 editing templates: change clothing, change material, change background, change style, or enhance portraits.

## Use Cases

- User wants to change clothing while keeping same pose
- User wants to change material (e.g., metal to water)
- User wants to change background while keeping person
- User wants to change artistic style (oil painting, sketch, etc.)
- User wants to enhance portrait (skin texture, lighting, eyes)

## Available Templates

### 1. Change Clothing (换衣服)

Keep pose unchanged, only replace clothing.

**Fields:**
| Parameter | Type | Options |
|-----------|-------|---------|
| `--clothing` | text | Clothing description (e.g., 运动外套, 连衣裙, 西装) |
| `--style` | select | 休闲, 正式, 运动, 时尚, 复古, 古风 |

**Example:**
```bash
python scripts/main.py generate --photo "user.jpg" --scenario edit \
    --template change-clothing \
    --clothing "运动外套" \
    --style "时尚" \
    --non-interactive
```

---

### 2. Change Material (换材质)

Replace material of clothing or object while maintaining shape.

**Fields:**
| Parameter | Type | Description |
|-----------|-------|-------------|
| `--from-material` | text | Original material (e.g., 金属, 木质, 织物) |
| `--to-material` | text | New material (e.g., 透明水流, 水晶, 火焰) |

**Example:**
```bash
python scripts/main.py generate --photo "user.jpg" --scenario edit \
    --template change-material \
    --from-material "金属" \
    --to-material "透明水流" \
    --non-interactive
```

---

### 3. Change Background (换背景)

Replace background while keeping person in original pose.

**Fields:**
| Parameter | Type | Description |
|-----------|-------|-------------|
| `--background` | text | Background description (e.g., 城市天际线, 海滩日落, 森林) |
| `--lighting` | text | Lighting type (e.g., 自然光, 黄昏光, 室内光) |

**Example:**
```bash
python scripts/main.py generate --photo "user.jpg" --scenario edit \
    --template change-background \
    --background "城市天际线" \
    --lighting "自然光" \
    --non-interactive
```

---

### 4. Change Style (换风格)

Apply artistic style transformation to the photo.

**Fields:**
| Parameter | Type | Options |
|-----------|-------|---------|
| `--style` | select | 油画, 素描, 水彩, 印象派, 动漫, 国画, 复古照片 |

**Example:**
```bash
python scripts/main.py generate --photo "user.jpg" --scenario edit \
    --template change-style \
    --style "油画" \
    --non-interactive
```

---

### 5. Enhance Portrait (人像优化)

Enhance facial features and overall portrait quality.

**Fields:**
| Parameter | Type | Description |
|-----------|-------|-------------|
| `--enhancements` | text | Comma-separated enhancements (e.g., 改善肤质,增加光泽,明亮的眼睛) |

**Common enhancements:**
- 改善肤质 - Improve skin texture
- 增加光泽 - Add healthy glow
- 明亮的眼睛 - Brighten eyes
- 平滑肤色 - Smooth skin tones
- 增加细节 - Enhance details
- 专业修图 - Professional retouching

**Example:**
```bash
python scripts/main.py generate --photo "user.jpg" --scenario edit \
    --template enhance-portrait \
    --enhancements "改善肤质,增加光泽,明亮的眼睛" \
    --non-interactive
```

## Command Examples

```bash
# Change clothing
python scripts/main.py generate --photo "user.jpg" --scenario edit \
    --template change-clothing \
    --clothing "运动外套" \
    --style "时尚" \
    --non-interactive

# Change material
python scripts/main.py generate --photo "user.jpg" --scenario edit \
    --template change-material \
    --from-material "金属" \
    --to-material "透明水流" \
    --non-interactive

# Change background
python scripts/main.py generate --photo "user.jpg" --scenario edit \
    --template change-background \
    --background "城市天际线" \
    --lighting "自然光" \
    --non-interactive

# Change style
python scripts/main.py generate --photo "user.jpg" --scenario edit \
    --template change-style \
    --style "油画" \
    --non-interactive

# Enhance portrait
python scripts/main.py generate --photo "user.jpg" --scenario edit \
    --template enhance-portrait \
    --enhancements "改善肤质,增加光泽" \
    --non-interactive
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|-------|-----------|-------------|
| `--photo, -p` | path | Yes | Path to photo to edit |
| `--template` | string | Yes | Template ID (change-clothing, change-material, etc.) |
| Template-specific | varies | Varies | See template-specific fields above |
| `--scenario, -s` | string | Yes | Scenario type: `edit` |
| `--non-interactive, -ni` | flag | No | Run in non-interactive mode |

## Best Practices

### Change Clothing
1. **Describe clearly**: Be specific about clothing type and style
2. **Match style**: Choose style that matches clothing description
3. **Clear pose photos**: Front-facing photos with clear pose work best

### Change Material
1. **Original material**: Accurately describe the original material
2. **New material**: Be specific about the desired new material
3. **Consider lighting**: Different materials reflect light differently

### Change Background
1. **Scene description**: Provide detailed background description
2. **Lighting matching**: Choose lighting that complements the new background
3. **Subject isolation**: Clear subject separation from original background helps

### Change Style
1. **Choose appropriate style**: Match style to photo content
2. **Style understanding**: Different styles produce different artistic effects
3. **Original quality**: Higher quality photos produce better style transfers

### Enhance Portrait
1. **Specific enhancements**: Be clear about what to enhance
2. **Natural results**: Focus on subtle improvements rather than dramatic changes
3. **Multiple enhancements**: Combine multiple enhancement types for best results

## Template Comparison

| Template | Photos Required | Preserves Pose | Changes |
|----------|----------------|----------------|---------|
| Change Clothing | 1 | Yes | Clothing only |
| Change Material | 1 | Yes | Material texture only |
| Change Background | 1 | Yes | Background only |
| Change Style | 1 | Yes | Overall artistic style |
| Enhance Portrait | 1 | Yes | Improves portrait quality |

## Common Use Cases

### Fashion & Clothing
- Try different outfits without changing
- Visualize new clothing styles
- Create fashion mockups

### Product Visualization
- Change product materials (metal to plastic, etc.)
- Visualize products in different environments
- Showcase product variations

### Photography Enhancement
- Replace distracting backgrounds
- Apply artistic styles for creative effects
- Enhance portrait quality for professional use
