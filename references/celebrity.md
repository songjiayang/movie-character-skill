# Celebrity Photos

Generate photos with movie characters on film sets.

## Overview

Take photos with popular movie characters in authentic behind-the-scenes settings. The skill generates realistic photos of you standing next to movie stars on film sets, at movie premieres, or at fan meet-and-greet events.

## Use Cases

- User wants to take photos with favorite movie characters
- User wants to create fun celebrity interaction memories
- User wants to generate fan photos with movie stars
- User wants to create social media content with celebrity appearances

## Available Characters

The following movie characters are available:

| Character | Description |
|-----------|-------------|
| Iron Man | Tony Stark as Iron Man on Avengers film set, high-tech suit |
| Wonder Woman | Diana Prince as Wonder Woman on Justice League film set, golden armor |
| Spider-Man | Peter Parker as Spider-Man on Marvel film set, friendly neighborhood hero |
| Harry Potter | Harry Potter on Hogwarts film set, magical atmosphere |
| Neo (Matrix) | Neo from The Matrix wearing sunglasses and black coat |
| Star-Lord | Peter Quill as Star-Lord wearing leather jacket and helmet |
| Captain America | Steve Rogers as Captain America in patriotic uniform |
| Thor | Thor with Mjolnir, Asgardian armor |
| Black Widow | Natasha Romanoff as Black Widow, tactical suit |
| Black Panther | T'Challa as Black Panther, Vibranium suit |
| Elsa | Elsa from Frozen in ice dress, magical powers |
| Luke Skywalker | Luke Skywalker with lightsaber, Jedi robe |
| Darth Vader | Darth Vader with lightsaber, iconic helmet |
| Joker | The Joker with green hair and makeup |
| Harley Quinn | Harley Quinn in colorful costume |
| Deadpool | Deadpool in red and black suit |
| Catwoman | Catwoman in sleek black suit |
| Jack Sparrow | Captain Jack Sparrow in pirate outfit |

To see the complete list:
```bash
python scripts/main.py list-characters
```

## Command Examples

```bash
# Generate with all available characters
python scripts/main.py generate --photo "user.jpg" --scenario celebrity

# Generate with specific characters
python scripts/main.py generate --photo "user.jpg" --scenario celebrity \
    --characters "Iron Man,Wonder Woman,Spider-Man" \
    --non-interactive

# Generate with custom count
python scripts/main.py generate --photo "user.jpg" --scenario celebrity \
    --count 3 \
    --non-interactive
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|-------|-----------|-------------|
| `--photo, -p` | path | Yes | Path to user photo |
| `--characters` | string | No | Comma-separated character names (defaults to all) |
| `--count, -c` | number | No | Number of images to generate (default: 5) |
| `--scenario, -s` | string | Yes | Scenario type: `celebrity` |
| `--non-interactive, -ni` | flag | No | Run in non-interactive mode |

## Best Practices

1. **Use clear photos**: Front-facing photos with good lighting work best
2. **Specify characters**: Choose specific characters for better control
3. **Photo resolution**: Use photos ≥1024×1024 for best results
4. **Add custom characters**: Use `add-character` command for characters not in the list

## Add Custom Character

```bash
python scripts/main.py add-character "Character Name" "Description prompt" --scene "Scene description"
```

Example:
```bash
python scripts/main.py add-character "Batman" \
    "Bruce Wayne as Batman in dark knight suit" \
    --scene "Gotham city at night"
```

## Available Styles

The celebrity scenario includes 3 built-in styles:

| Style | Description |
|-------|-------------|
| 电影片场 | On film set with crew, cameras, lighting equipment |
| 首映礼 | At movie premiere, red carpet, flash photography |
| 粉丝见面会 | At fan meet-and-greet, friendly interaction |
