# Free Mode

Generate images with custom prompts and 1-14 reference photos.

## Overview

Full creative control with custom prompts describing desired scenes, styles, atmospheres. Supports single or multiple reference photos (up to 14) for guidance while using natural language prompts for complete customization.

## Use Cases

- User wants complete creative control over image generation
- User wants to generate images not covered by specific scenarios
- User wants to experiment with unique artistic styles
- User wants to create complex multi-reference image fusion
- User has specific vision and wants to describe it in detail

## Command Examples

```bash
# Single photo with custom prompt
python scripts/main.py generate --photo "user.jpg" --scenario free \
    --prompt "A futuristic cyberpunk portrait with neon lighting and holographic elements" \
    --non-interactive

# Multiple photos with scene description
python scripts/main.py generate --photos "p1.jpg,p2.jpg,p3.jpg" --scenario free \
    --prompt "A group photo on Mars surface, wearing space suits, cinematic atmosphere" \
    --non-interactive

# With negative prompt to exclude unwanted elements
python scripts/main.py generate --photo "user.jpg" --scenario free \
    --prompt "Renaissance art style portrait, oil painting, dramatic lighting" \
    --negative-prompt "modern, digital, high contrast, low quality" \
    --non-interactive

# Generate multiple variations
python scripts/main.py generate --photo "user.jpg" --scenario free \
    --prompt "A futuristic cyberpunk portrait with neon lighting" \
    --count 4 \
    --non-interactive
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|-------|-----------|-------------|
| `--photo` or `--photos` | paths | Yes | Path(s) to reference photo(s) (1-14 photos) |
| `--prompt` | text | Yes | Custom prompt describing desired scene, style, atmosphere |
| `--negative-prompt` | text | No | Negative prompt to exclude unwanted elements |
| `--count, -c` | number | No | Number of images to generate (default: 1) |
| `--scenario, -s` | string | Yes | Scenario type: `free` |
| `--non-interactive, -ni` | flag | No | Run in non-interactive mode |

## Prompt Writing Guide

### Effective Prompts

Good prompts are specific, detailed, and include multiple elements:

**Subject Description:**
- "A woman in her 30s with curly brown hair"
- "A young man with glasses and a beard"
- "Two children playing in a park"

**Style and Technique:**
- "Renaissance oil painting style, dramatic lighting"
- "Anime style, Studio Ghibli inspired, soft colors"
- "1970s vintage photography, film grain, warm tones"

**Setting and Environment:**
- "In a cozy coffee shop with large windows"
- "On a misty mountain peak at sunrise"
- "In a futuristic cyberpunk city with neon lights"

**Mood and Atmosphere:**
- "Peaceful and serene atmosphere"
- "Energetic and vibrant mood"
- "Mysterious and shadowy ambiance"

**Technical Details:**
- "8k resolution, highly detailed"
- "Professional photography, sharp focus"
- "Cinematic lighting, dramatic shadows"

### Example Prompts

**Cyberpunk Portrait:**
```
A futuristic cyberpunk portrait with neon lighting and holographic elements.
The person has a chrome cybernetic face plate with glowing blue eyes.
Dark background with city skyline, rain, and neon signs.
Cinematic lighting, 8k resolution, highly detailed.
```

**Renaissance Art Style:**
```
Renaissance art style portrait, oil painting technique.
Dramatic chiaroscuro lighting with deep shadows.
Rich, warm color palette with gold accents.
Elegant clothing from the Renaissance period.
Fine art museum quality, classical composition.
```

**Anime Style:**
```
Anime style portrait, Studio Ghibli inspired.
Soft pastel colors, gentle lighting, dreamy atmosphere.
Character with expressive eyes and flowing hair.
Whimsical background with fantasy elements.
Hand-drawn aesthetic, clean lines, vibrant colors.
```

**Vintage Photography:**
```
1970s vintage photography style.
Film grain texture, warm sepia tones, nostalgic atmosphere.
Casual portrait in natural lighting.
Candid moment, authentic retro feel.
Professional film photography, slight light leak effect.
```

**Sci-Fi Group Scene:**
```
A group photo on Mars surface.
Five astronauts in space suits, dusty red terrain.
Mars rover in background, distant mountain range.
Cinematic sci-fi atmosphere, harsh natural lighting.
Epic exploration scene, 8k resolution, highly detailed.
```

## Negative Prompts

Negative prompts specify what to exclude from generated images.

### Common Negative Prompts

| Category | Examples |
|-----------|-----------|
| Quality | `low quality, blurry, pixelated, low resolution` |
| Artifacts | `artifacts, distortion, deformed, extra limbs, extra fingers` |
| Style | `modern, digital, anime, cartoon` (when wanting realistic) |
| Content | `watermark, text, logo, signature, frame` |
| Faces | `blurry faces, distorted faces, unnatural faces, bad proportions` |
| Lighting | `harsh lighting, overexposed, underexposed, poor lighting` |

### Negative Prompt Examples

**For Realistic Photos:**
```
--negative-prompt "anime, cartoon, illustration, painting, digital art,
low quality, blurry, distorted faces, unnatural poses, watermarks"
```

**For Artistic Styles:**
```
--negative-prompt "photorealistic, modern, digital, harsh lighting,
low contrast, poor composition, amateur"
```

**For Clean Results:**
```
--negative-prompt "artifacts, distortion, deformed hands, extra fingers,
watermarks, text, logos, frames, low quality"
```

## Best Practices

### Prompt Writing

1. **Be specific**: Describe details rather than vague concepts
2. **Use multiple elements**: Combine subject, style, setting, mood
3. **Include technical terms**: Mention resolution, lighting, composition
4. **Use natural language**: Write clear, readable descriptions
5. **Keep it focused**: Avoid contradictory or overly complex prompts

### Using Reference Photos

1. **Single reference**: Use 1 photo when wanting style or composition guidance
2. **Multiple references**: Use 2-14 photos for complex fusion scenarios
3. **Clear quality**: Use high-quality, well-lit reference photos
4. **Consistent style**: Photos with consistent style produce better fusion

### Negative Prompts

1. **Identify unwanted elements**: Think about what you don't want in the image
2. **Be specific**: List specific things to exclude
3. **Keep it relevant**: Only include negatives that matter for your goal
4. **Test variations**: Adjust negatives based on results

### Photo Guidelines

**Number of Reference Photos:**
- **1 photo**: Style or composition guidance
- **2-4 photos**: Multi-photo fusion (outfit, person-scenery, etc.)
- **5-14 photos**: Complex multi-reference fusion

**Photo Quality:**
- Resolution: ≥1024×1024 for best results
- Lighting: Even, natural lighting preferred
- Subject: Clear, focused on main elements
- Style: Consistent style across multiple photos

## When to Use Free Mode vs. Specific Scenarios

**Use Specific Scenarios When:**
- You want celebrity photos → Use **celebrity** scenario
- You want portrait photography → Use **portrait** scenario
- You want couple photos → Use **couple** scenario
- You want family photos → Use **family** scenario
- You want to edit photos (change clothing, background, etc.) → Use **edit** scenario
- You want to merge photos (outfit, person-scenery, brand) → Use **fusion** scenario
- You want to create series (seasons, character states, etc.) → Use **series** scenario
- You want to design posters → Use **poster** scenario

**Use Free Mode When:**
- You have a specific custom vision not covered by other scenarios
- You want maximum creative control
- You want to experiment with unique artistic styles
- You want to create complex multi-reference fusions
- You have detailed prompt describing exactly what you want

## Prompt Examples by Style

### Portrait Styles

**Professional Headshot:**
```
Professional headshot photography, business portrait.
Clean solid background, soft studio lighting.
Confident expression, sharp focus, 85mm lens.
Shallow depth of field, neutral color palette.
8k resolution, photorealistic.
```

**Artistic Portrait:**
```
Fine art portrait, oil painting style.
Dramatic chiaroscuro lighting, deep shadows.
Rich color palette with gold and crimson accents.
Classical composition, elegant pose.
Museum quality art, detailed brushstrokes.
```

**Lifestyle Portrait:**
```
Lifestyle photography, natural and authentic.
Soft natural window light, candid moment.
Everyday setting, relaxed posture.
Warm tones, genuine expression.
Professional photography quality, shallow depth of field.
```

### Artistic Styles

**Cyberpunk:**
```
Cyberpunk aesthetic, futuristic cityscape.
Neon lights, holographic displays, rain-slicked streets.
Chrome and metal textures, glowing circuitry.
High contrast, dramatic lighting.
8k resolution, highly detailed, cinematic.
```

**Fantasy:**
```
High fantasy illustration style.
Magical creatures, floating islands, crystal towers.
Luminous lighting, particle effects, magical atmosphere.
Vibrant color palette, rich details.
Digital art, epic scale, dreamlike quality.
```

**Surreal:**
```
Surrealist art style, dreamlike imagery.
Impossible physics, melting objects, floating elements.
Ethereal lighting, soft focus, ethereal atmosphere.
Subtle color palette with pops of unexpected color.
Fine art quality, thought-provoking composition.
```

### Photography Styles

**Vintage Film:**
```
1950s vintage film photography.
Warm sepia tones, film grain texture.
Natural lighting, soft shadows.
Candid moment, authentic retro feel.
Professional film photography, slight vignetting.
```

**Modern Editorial:**
```
High fashion editorial photography.
Studio lighting with controlled shadows.
Dramatic pose, intense gaze.
Minimalist background, monochromatic tones.
Professional magazine quality, sharp focus.
```

**Documentary:**
```
Documentary photography style.
Natural available light, authentic moment.
Environmental portrait with context.
Candid expression, genuine emotion.
Photojournalistic aesthetic, gritty realism.
```

## Common Issues & Solutions

### Prompt Issues
- **Too vague**: Add more specific details about subject, style, and setting
- **Too complex**: Simplify prompt, focus on key elements
- **Contradictory**: Ensure prompt elements are compatible
- **Missing key elements**: Add missing subject or style information

### Result Issues
- **Not matching prompt**: Be more specific, add more details
- **Style wrong**: Include style-specific terms and techniques
- **Quality issues**: Add technical details (resolution, lighting, etc.)
- **Unwanted elements**: Use negative prompts to exclude them

### Reference Photo Issues
- **Poor fusion**: Use higher quality, better-lit reference photos
- **Style mismatch**: Use reference photos with consistent style
- **Not enough guidance**: Add more specific prompt details
- **Too many references**: Reduce number of photos (2-4 often optimal)

## Advanced Tips

1. **Iterate**: Start with simple prompt, refine based on results
2. **Use negative prompts**: Exclude unwanted elements systematically
3. **Combine references**: Test different photo combinations for fusion
4. **Experiment with count**: Generate multiple variations to find best result
5. **Study art styles**: Look at art styles and techniques for prompt inspiration
6. **Be descriptive**: The more detailed your prompt, the better the control
