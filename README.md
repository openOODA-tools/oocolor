# oocolor: Sovereign COLOR CONVERTER

<div align="center">

```
================================================================================
                                oocolor
               Sovereign openOODA COLOR CONVERTER
================================================================================
```

**Sovereign COLOR CONVERTER**  
*Converts between HEX, RGB, HSL, CMYK, and ANSI 256 color representations.*  
*Two Faces, One Engine:* Modern TrueColor terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oocolor/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oocolor-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oocolor/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oocolor/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oocolor-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oocolor/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oocolor [options] [COLOR] [CONTRAST_COLOR]

Converts between HEX, RGB, HSL, CMYK, and ANSI 256 color representations.

Options:
  -x, --hex              output HEX color value (#RRGGBB)
  -r, --rgb              output RGB representation rgb(R, G, B)
  -s, --hsl              output HSL representation hsl(H, S%, L%)
  -c, --cmyk             output CMYK representation cmyk(C%, M%, Y%, K%)
  -a, --ansi             output ANSI 256 index
  -p, --preview          render TrueColor terminal swatch
      --contrast COLOR   calculate WCAG 2.1 contrast ratio against color
      --palette MODE     generate palette (tints, shades) [default: tints]
      --demo             showcase chromatic models and WCAG matrix
      --json             output formatted as JSON Lines
  -h, --help             display this help and exit
  -v, -V, --version      output version information and exit
      --mcp              run as Model Context Protocol stdio server
```

### Examples

```bash
# Display full color card with TrueColor swatch
oocolor "#3498DB"

# Convert HEX to RGB
oocolor -r "#3498DB"

# Convert named color to CMYK
oocolor -c "coral"

# Calculate WCAG 2.1 contrast ratio between two colors
oocolor "#FFFFFF" --contrast "#000000"

# Generate 5 tint palette swatches
oocolor "#E74C3C" --palette tints --preview

# Output structured telemetry JSON
oocolor "#9B59B6" --json
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oocolor` operates as a JSON-RPC 2.0 stdio server providing sovereign chromatic capabilities for AI agents without network authority:

```bash
oocolor --mcp
```

### Exposed MCP Tools

1. **`color_convert`**: Convert any color string to HEX, RGB, HSL, CMYK, and ANSI 256 representations.
2. **`color_contrast`**: Calculate WCAG 2.1 contrast ratio and AA/AAA compliance ratings between two colors.
3. **`color_palette`**: Generate tints, shades, or harmonic steps from a base color.
4. **`color_blend`**: Weighted linear interpolation and chromatic blending between two colors.
5. **`color_inspect`**: Inspect detailed chromatic metrics, relative luminance, and formatting cards.

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Zero ambient authority or network egress.
* **Negative-Trust Architecture:** Strict boundary validation on input strings, color formats, and palette boundaries.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
