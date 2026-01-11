# Series Creation

Create series of related images with 4 creative templates.

## Overview

Generate cohesive series of images (4-10 images) using 4 templates: seasons theme, brand visual kit, character states, or story sequence.

## Use Cases

- User wants to create seasonal theme illustrations
- User wants to design unified brand visual kit
- User wants to create character state variations
- User wants to create story sequence with narrative

## Available Templates

### 1. Seasons Theme (四季主题)

Create 4 seasonal illustrations showing seasonal changes.

**Required Photos:** 1 (reference for person features)

**Fields:**
| Parameter | Type | Options | Default |
|-----------|-------|----------|---------|
| `--theme` | text | Theme description | Required |
| `--style` | select | 插画风格, 水彩画风格, 油画风格, 动漫风格, 写实摄影风格 | 插画风格 |
| `--scene` | select | 户外庭院, 城市街道, 田园风光, 公园长椅, 山顶景色, 湖畔景色 | 户外庭院 |
| `--count` | select | 4, 6, 8 | 4 |

**Theme Examples:**
- "同一庭院的四季变迁"
- "同一建筑的四季"
- "同一街道的四季"
- "同一花园的四季"

**Style Examples:**
- 插画风格 - Soft, colorful illustrations
- 水彩画风格 - Gentle watercolor paintings
- 油画风格 - Rich oil painting style
- 动漫风格 - Anime/manga aesthetic
- 写实摄影风格 - Photorealistic photography

**Scene Examples:**
- 户外庭院 - Courtyard or garden
- 城市街道 - Urban street
- 田园风光 - Countryside landscape
- 公园长椅 - Park bench
- 山顶景色 - Mountain view
- 湖畔景色 - Lakeside scenery

**Example:**
```bash
python scripts/main.py generate --photo "me.jpg" --scenario series \
    --template seasons \
    --theme "同一庭院的四季变迁" \
    --style "插画风格" \
    --scene "户外庭院" \
    --count 4 \
    --non-interactive
```

---

### 2. Brand Visual Kit (品牌整套视觉)

Create unified brand visual design for multiple items.

**Required Photos:** 1 (LOGO or brand reference)

**Fields:**
| Parameter | Type | Description |
|-----------|-------|-------------|
| `--brand-name` | text | Brand name |
| `--color` | text | Primary color (e.g., 绿色, 蓝色, 红色) |
| `--style` | select | 简约现代, 复古风, 科技感, 文艺风, 极简主义 |
| `--items` | text | Comma-separated items |
| `--count` | select | 4, 6, 8, 10 | 4 |

**Common Items:**
- 包装袋 - Packaging bags
- 帽子 - Hats
- 卡片 - Cards
- 挂绳 - Lanyards
- 徽章 - Badges
- 服装 - Clothing
- 马克杯 - Mugs
- 笔记本 - Notebooks
- 贴纸 - Stickers

**Style Options:**
- 简约现代 - Clean, modern design
- 复古风 - Retro, vintage style
- 科技感 - Tech-oriented, futuristic
- 文艺风 - Artistic, creative
- 极简主义 - Minimalist design

**Example:**
```bash
python scripts/main.py generate --photo "logo.jpg" --scenario series \
    --template brand-kit \
    --brand-name "MyBrand" \
    --color "绿色" \
    --style "简约现代" \
    --items "包装袋,帽子,卡片,挂绳" \
    --count 4 \
    --non-interactive
```

---

### 3. Character States (角色状态变体)

Create variations of same character in different states.

**Required Photos:** 1 (character reference)

**Fields:**
| Parameter | Type | Options |
|-----------|-------|----------|
| `--scene` | text | Scene description |
| `--state-type` | select | 动作状态, 表情状态, 服装状态, 道具状态 |
| `--custom-states` | text | Comma-separated state descriptions |
| `--count` | select | 4, 6, 8 | 4 |

**State Types:**

**动作状态 - Action States:**
- 戴墨镜 - Wearing sunglasses
- 骑摩托 - Riding motorcycle
- 戴帽子 - Wearing hat
- 拿棒棒糖 - Holding lollipop
- 拿咖啡 - Holding coffee
- 打电话 - Making phone call

**表情状态 - Expression States:**
- 开心 - Happy
- 思考 - Thinking
- 惊讶 - Surprised
- 生气 - Angry
- 害羞 - Shy

**服装状态 - Clothing States:**
- 穿西装 - Wearing suit
- 穿运动装 - Wearing sportswear
- 穿休闲装 - Wearing casual wear
- 穿古装 - Wearing traditional costume

**道具状态 - Prop States:**
- 拿吉他 - Holding guitar
- 拿书籍 - Holding book
- 拿手机 - Holding phone
- 拿书包 - Carrying backpack

**Example:**
```bash
python scripts/main.py generate --photo "me.jpg" --scenario series \
    --template character-states \
    --scene "游乐园" \
    --state-type "动作状态" \
    --custom-states "戴墨镜,骑摩托,戴帽子,拿棒棒糖" \
    --count 4 \
    --non-interactive
```

---

### 4. Story Sequence (故事序列)

Create narrative sequence with story progression.

**Required Photos:** 1 (character or reference)

**Fields:**
| Parameter | Type | Description |
|-----------|-------|-------------|
| `--theme` | text | Story theme |
| `--style` | select | 温馨童趣, 悬疑推理, 奇幻冒险, 科幻未来, 现实主义 |
| `--count` | select | 4, 6, 8, 10 | 6 |

**Theme Examples:**
- "小猫的奇幻冒险"
- "城市夜晚的神秘事件"
- "森林里的神奇遭遇"
- "太空探索之旅"
- "校园生活的日常点滴"

**Style Options:**
- 温馨童趣 - Warm, childlike, playful
- 悬疑推理 - Suspenseful, mystery
- 奇幻冒险 - Fantasy, adventure
- 科幻未来 - Sci-fi, futuristic
- 现实主义 - Realistic, grounded

**Example:**
```bash
python scripts/main.py generate --photo "me.jpg" --scenario series \
    --template story-sequence \
    --theme "小猫的奇幻冒险" \
    --style "温馨童趣" \
    --count 6 \
    --non-interactive
```

## Command Examples

```bash
# Seasons theme
python scripts/main.py generate --photo "me.jpg" --scenario series \
    --template seasons \
    --theme "同一庭院的四季变迁" \
    --style "插画风格" \
    --scene "户外庭院" \
    --count 4 \
    --non-interactive

# Brand kit
python scripts/main.py generate --photo "logo.jpg" --scenario series \
    --template brand-kit \
    --brand-name "MyBrand" \
    --color "绿色" \
    --style "简约现代" \
    --items "包装袋,帽子,卡片,挂绳" \
    --count 4 \
    --non-interactive

# Character states
python scripts/main.py generate --photo "me.jpg" --scenario series \
    --template character-states \
    --scene "游乐园" \
    --state-type "动作状态" \
    --custom-states "戴墨镜,骑摩托,戴帽子,拿棒棒糖" \
    --count 4 \
    --non-interactive

# Story sequence
python scripts/main.py generate --photo "me.jpg" --scenario series \
    --template story-sequence \
    --theme "小猫的奇幻冒险" \
    --style "温馨童趣" \
    --count 6 \
    --non-interactive
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|-------|-----------|-------------|
| `--photo, -p` | path | Yes | Path to reference photo |
| `--template` | string | Yes | Template ID |
| Template-specific | varies | Varies | See template-specific fields above |
| `--count, -c` | select | No | Number of images (default varies by template) |
| `--scenario, -s` | string | Yes | Scenario type: `series` |
| `--non-interactive, -ni` | flag | No | Run in non-interactive mode |

## Best Practices

### Seasons Theme
1. **Clear theme**: Describe consistent theme across seasons
2. **Choose appropriate style**: Match style to theme type
3. **Scene selection**: Pick scene that works in all seasons
4. **Consistent character**: Use clear reference photo for person features

### Brand Visual Kit
1. **Clear brand identity**: Define brand name, color, and style clearly
2. **Specific items**: List items clearly with correct formatting
3. **Consistent style**: Match style to brand personality
4. **Professional reference**: Use high-quality LOGO or brand reference

### Character States
1. **Clear scene**: Provide detailed scene description
2. **Appropriate state type**: Choose state type that fits character
3. **Specific states**: List states clearly with correct formatting
4. **Consistent character**: Use clear reference photo showing face and body

### Story Sequence
1. **Engaging theme**: Create compelling story concept
2. **Appropriate style**: Match style to story type and audience
3. **Logical progression**: Ensure story flows naturally
4. **Consistent elements**: Keep character and setting consistent

## Template Comparison

| Template | Photos | Count Range | Output Type |
|----------|---------|-------------|-------------|
| Seasons Theme | 1 | 4-8 | Seasonal illustrations |
| Brand Visual Kit | 1 | 4-10 | Brand visual designs |
| Character States | 1 | 4-8 | Character variations |
| Story Sequence | 1 | 4-10 | Narrative sequence |

## Photo Guidelines

### Photo Requirements
- **All templates**: 1 reference photo
- **Resolution**: ≥1024×1024 for best results
- **Subject clarity**: Clear facial features and visible body
- **Lighting**: Even lighting without harsh shadows

### Photo Quality Tips
- Front-facing or three-quarter view works best
- Clear facial features ensure consistency across series
- Neutral expression allows better variation control
- Simple background helps focus on subject

## Common Issues & Solutions

### Series Consistency Issues
- **Character looks different**: Use clearer reference photo
- **Style varies**: Ensure consistent style settings
- **Lighting mismatch**: Choose style with consistent lighting

### Seasons Theme Issues
- **Seasons unclear**: Provide more specific theme description
- **Colors don't match season**: Adjust style selection
- **Scene doesn't fit season**: Choose appropriate scene type

### Brand Kit Issues
- **Inconsistent design**: Ensure brand name, color, and style match
- **Unclear items**: List items in correct comma-separated format
- **Style mismatch**: Match style to brand personality

### Character States Issues
- **States unclear**: Provide specific state descriptions
- **Scene mismatch**: Ensure scene supports chosen states
- **Inconsistent character**: Use clearer reference photo

### Story Sequence Issues
- **Story unclear**: Provide more detailed theme description
- **Inconsistent progression**: Ensure count matches story length
- **Style mismatch**: Match style to story type
