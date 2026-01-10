# Personal Portraits

Generate professional personal portraits in various artistic styles.

## Overview

Create professional headshots and artistic portraits using 15+ different styles ranging from business professional to creative vintage photography. Each style includes specific lighting, background, and mood settings for authentic results.

## Use Cases

- User needs professional headshot for LinkedIn or business use
- User wants artistic portraits for social media or portfolios
- User wants portrait photography without expensive studio sessions
- User wants to explore different portrait styles

## Available Styles

### Business Styles

| Style | Description |
|-------|-------------|
| 职业商务照 | Professional headshot, solid background, studio lighting, confident expression |
| 证件照 | Passport-style portrait, neutral background, straightforward pose |

### Artistic Styles

| Style | Description |
|-------|-------------|
| 艺术肖像 | Dramatic lighting, creative composition, fine art photography style |
| 古典油画 | Classic oil painting style, dramatic chiaroscuro, elegant |
| 水彩画 | Soft watercolor painting, gentle colors, artistic brushstrokes |
| 素描画 | Detailed pencil sketch, realistic shading, artistic rendering |
| 印象派油画 | Impressionist style, visible brushstrokes, light-focused |

### Lifestyle Styles

| Style | Description |
|-------|-------------|
| 时尚街拍 | Fashion street photography, candid moment, urban atmosphere |
| 咖啡厅休闲照 | Relaxed cafe setting, natural lighting, comfortable vibe |
| 户外自然照 | Natural outdoor setting, daylight, fresh atmosphere |
| 约会照 | Romantic date photo, warm lighting, intimate mood |

### Vintage Styles

| Style | Description |
|-------|-------------|
| 1970年代复古照 | 1970s vintage style, film grain, warm tones, retro feel |
| 1950年代复古照 | 1950s classic portrait, black & white or sepia |
| 1940年代复古照 | 1940s Hollywood glamour, elegant lighting |

### Cinematic Styles

| Style | Description |
|-------|-------------|
| 好莱坞电影风格 | Cinematic portrait, movie lighting, dramatic atmosphere |
| 韩国电影风格 | Korean movie aesthetic, soft focus, emotional tone |

To see complete list:
```bash
python scripts/main.py list-styles --scenario portrait
```

## Command Examples

```bash
# Generate with all portrait styles
python scripts/main.py generate --photo "user.jpg" --scenario portrait

# Generate with specific style
python scripts/main.py generate --photo "user.jpg" --scenario portrait \
    --style "职业商务照" \
    --non-interactive

# Generate multiple images with same style
python scripts/main.py generate --photo "user.jpg" --scenario portrait \
    --style "时尚街拍" \
    --count 3 \
    --non-interactive
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|-------|-----------|-------------|
| `--photo, -p` | path | Yes | Path to user photo |
| `--style` | string | No | Specific style name (defaults to all styles) |
| `--count, -c` | number | No | Number of images to generate (default: varies) |
| `--scenario, -s` | string | Yes | Scenario type: `portrait` |
| `--non-interactive, -ni` | flag | No | Run in non-interactive mode |

## Style Categories

Styles are organized by category for easy selection:

- **商务** (Business): Professional, corporate, executive portraits
- **艺术** (Artistic): Creative, dramatic, experimental portraits
- **生活** (Lifestyle): Casual, natural, everyday portraits
- **复古** (Vintage): Classic, film-like, nostalgic portraits
- **时尚** (Fashion): Trendy, stylish, magazine-quality portraits

## Best Practices

1. **Choose appropriate style**: Match style to your use case
2. **Use high-quality photos**: Clear, well-lit photos produce best results
3. **Consider background**: Each style includes specific background suggestions
4. **Test different styles**: Try multiple styles to find best fit
5. **Photo resolution**: Use photos ≥1024×1024 for best results

## Style Examples

### Professional Business
- Clean solid background (white, gray, navy blue)
- Soft studio lighting with even illumination
- Standard headshot pose facing camera
- Professional, confident, trustworthy mood

### Artistic Portrait
- Dramatic chiaroscuro lighting with side lighting
- Dark gradient or textured background
- Three-quarter angle pose with slight head tilt
- Artistic, mysterious, sophisticated mood

### Lifestyle
- Natural window light or soft ambient lighting
- Natural outdoor or cozy indoor environment
- Natural casual pose with relaxed shoulders
- Relaxed, authentic, approachable mood
