# LaTeX Style Guidelines for CHM_FINAL_REVIEW

## Document Class and Packages
- **Class**: `article` with `[11pt]` font.
- **Margins**: `geometry` package with 1-inch margins.
- **Chemistry**:
    - `\usepackage[version=4]{mhchem}`
    - `\usepackage{chemfig}`
- **Math & Units**:
    - `\usepackage{amsmath, amssymb}`
    - `\usepackage{siunitx}`
- **Layout**:
    - `\usepackage{tcolorbox}` for formula boxes.
    - `\usepackage{enumitem}` for consistent bullet points.
    - `\usepackage{titlesec}` for formatted headers.

## Typographic Conventions
- All chemical species must use `\ce{...}` (e.g., `\ce{H2O}`).
- All units must use `\si{...}` (e.g., `\si{g.mol^{-1}}`).
- Key formulas should be centered and enclosed in a `tcolorbox`.
- Step-by-step instructions should use an `enumerate` environment.

## Design
- **Color Palette**: Use a professional blue/gray theme for boxes.
- **Chapter Headers**: Large, bold, sans-serif font.
- **Consistency**: Ensure uniform spacing between sections and diagrams.
