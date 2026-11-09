# Adversarial Inspection & Architectural Audit: Slide Prototype Generation

**Audit Target:** `generate_15_prototypes.py` & 15 Generated Prototypes  
**Canvas Standard:** 2560 x 1440 QHD (16:9 Landscape)  
**Palette Standard:** Catppuccin Mocha  
**Auditor:** Adversarial QA & Systems Verification Agent  
**Date:** 2026-11-08  

---

## Executive Summary

A forensic adversarial audit was conducted on the prototype generator script `generate_15_prototypes.py` and the resulting 15 prototype slide artifacts (`proto_01` through `proto_15`) located in `/home/owen/ucf/so/s1/COP/slides/`.

The inspection confirmed all 3 user-reported defects and identified 3 additional critical architectural failures that were masked during previous self-evaluations:

1. **[CRITICAL] Tab Characters Rendering as Tofu / Missing Glyphs:** 
   115 tab characters (`\t`) in `FileTester.java` (Slide 13) and 138 tab characters in `Room.java` (Slide 15) render as hollow square boxes (tofu). Pillow font rendering lacks tab stop expansion and FreeType defaults to the font's `.notdef` missing glyph symbol.
2. **[CRITICAL] Severe Bounding Box Misalignment (Slide 11 & others):** 
   In Slide 11 (`proto_11_multi_box_instanceof.png`), the injected box for `PaymentsTester` was placed at `x = 0.40 * width` instead of `x = 0.022 * width`. The original slide code on the bottom-left was left 100% exposed and visible, while the new box awkwardly floated over the center-right terminal output.
3. **[CRITICAL] Aspect Ratio Breakdown in Adjacent Layout (Slides 13 & 14):** 
   Forcing a 16:9 landscape slide into a vertical half-pane (aspect ratio 0.88) shrinks the slide to 1200 x 675 px, wasting 765 px (53%) of vertical screen height as empty mantle void, while squeezing 57 lines of code into a microscopic 15 pt font.
4. **[CRITICAL] Silent Code Truncation Hidden by Clamp (Slide 15):** 
   In Slide 15 (`proto_15_adjacent_midterm_room.png`), `Room.java` has 97 lines. The generator script clamped minimum font size to 13 pt, calculated an overflow, and silently executed `break`. **28 lines of source code (lines 70 through 97) were completely discarded and never rendered.**
5. **[DEFECT] Box Geometry Inflation (Slides 8 & 9):** 
   In Slides 8 and 9, the injected code boxes were assigned a 90% slide width (`bw = 0.90 * sw`), despite the underlying code occupying only 38% to 54% of the slide, creating massive empty dark boxes across the slide.
6. **[DEFECT] Proportional Font Selection & Advance Drift:** 
   The script loaded `JetBrainsMonoNerdFontPropo-Bold.ttf` (the proportional variant) instead of a true monospace font, and used bounding box width (`bbox[2] - bbox[0]`) instead of `font.getlength()`, introducing cumulative horizontal alignment drift across multi-token lines.

---

## Forensic Analysis of Reported Defects

### Defect 1: Tab Characters Rendering as Tofu Squares

```text
+-----------------------------------------------------------------------------+
| TOFU ROOT CAUSE MECHANISM                                                   |
+-----------------------------------------------------------------------------+
  Source Code Line: "\t\tBufferedWriter bw = null;"
         |
         v
  `pygments.lex` splits token: (Token.Text.Whitespace, "\t\t")
         |
         v
  PIL `draw.text((cur_x, curr_y), "\t\t", font=font, ...)`
         |
         v
  FreeType queries JetBrains Mono for glyph index of ASCII 0x09 (HT).
  ASCII 0x09 is an unprintable control character; font has NO outline glyph.
         |
         v
  FreeType maps missing character to glyph index 0 (.notdef).
  In JetBrains Mono, .notdef is defined as a hollow rectangle / tofu square!
         |
         v
  Result: Every tab character draws a visible hollow square box on the slide.
+-----------------------------------------------------------------------------+
```

* **Underlying Flaw:** 
  The author assumed `PIL.ImageDraw.Draw.text()` behaves like a text terminal or IDE with automatic tab stop expansion. PIL does not expand `\t`.
* **Impact:** 
  In `FileTester.java`, there are 115 literal tab characters. In `Room.java`, there are 138 literal tab characters. Every indentation level on every indented line rendered as 1 to 4 tofu boxes.
* **Exact Code Fix:**
  At the entry of `render_catppuccin_code_box()`:
  ```python
  code_text = code_text.expandtabs(4)
  ```

---

### Defect 2: Bounding Box Misalignment & Underlying Exposed Text

```text
+-----------------------------------------------------------------------------+
| SLIDE 11 GEOMETRY CONFLICT (Slide13_InheritancePart2.pdf, Page 4)          |
+-----------------------------------------------------------------------------+
  Slide Dimensions: 960 x 540 pt (2667 x 1500 px at 200 DPI)

  Actual PDF Layout:
  +-----------------------------------+-----------------------------------+
  | CardPayment (Top-Left)            | Payment (Top-Right)               |
  | x: 0.022 - 0.459, y: 0.154 - 0.515| x: 0.512 - 0.977, y: 0.159 - 0.520|
  +-----------------------------------+-----------------------------------+
  | PaymentsTester (BOTTOM-LEFT)      | Console Output (BOTTOM-RIGHT)     |
  | x: 0.022 - 0.566, y: 0.567 - 0.967| x: 0.605 - 0.785, y: 0.568 - 0.769|
  +-----------------------------------+-----------------------------------+

  What generate_15_prototypes.py Did:
  +-----------------------------------+-----------------------------------+
  | [BOX 1: CardPayment]              | [BOX 2: Payment]                  |
  | Placed at x=0.02, y=0.14 [OK]     | Placed at x=0.50, y=0.14 [OK]     |
  +-----------------------------------+-----------------------------------+
  | ORIGINAL PaymentsTester CODE      | [BOX 3: PaymentsTester]           |
  | COMPLETELY UNCOVERED & EXPOSED!   | PASTED AT x=0.40, y=0.60!         |
  | (Original text shows through)     | (Floats over output & whitespace) |
  +-----------------------------------+-----------------------------------+
+-----------------------------------------------------------------------------+
```

* **Underlying Flaw:** 
  The developer used hardcoded manual percentage guessing:
  `img.paste(s3, (int(sw * 0.40), int(sh * 0.60)), s3)`
  The developer guessed `0.40` without inspecting where `PaymentsTester` was located. `PaymentsTester` is on the bottom-left (`x = 0.022`).
* **Root Cause Process Failure:** 
  Lack of deterministic bounding box extraction. Instead of querying Poppler's `pdftotext -bbox-layout` or running OpenCV contour detection, the developer hand-coded approximate decimal fractions.

---

### Defect 3: Adjacent Layout Imbalance & Shrunken Slides

```text
+-----------------------------------------------------------------------------+
| THE ASPECT RATIO MISMATCH IN ADJACENT FORMAT                                |
+-----------------------------------------------------------------------------+
  Canvas: 2560 x 1440 (16:9 Landscape)
  Split: Left Column = 1200 x 1360 | Right Column = 1240 x 1360

  Slide16 Page 6 is a 16:9 Widescreen Slide (2667 x 1500 px):
  Aspect Ratio = 1.778

  When fitted into 1200 px width:
    Target Width  = 1200 px
    Target Height = 1200 / 1.778 = 675 px!

  Total Canvas Height = 1440 px
  Slide Height        =  675 px
  ---------------------------------
  Vertical Dead Space =  765 px (53% of screen height is empty void!)

  Right Pane (FileTester.java, 57 lines):
    Available Height  = 1304 px
    Line Height       = 1304 / 57 = 22.8 px -> Font Size = 15 pt
    Result: Microscopic, unreadable code on a QHD 1440p canvas.
+-----------------------------------------------------------------------------+
```

* **Underlying Flaw:** 
  Format 3 (Adjacent) was conceived for portrait documents (like `sampleMidtermExam.pdf` in Slide 15, which has an aspect ratio of 0.77 and fills the vertical pane naturally). 
  When applied to 16:9 landscape slides (Slides 13 and 14), horizontal halving forces the slide into a 45% reduction, creating 53% vertical dead space while squeezing 57 lines of code into a tiny 15 pt font.
* **Furthermore:** `Slide16` page 6 already contains its own in-slide code block (`WriteFile(String fname)`). Pairing it with the 57-line external `FileTester.java` in an adjacent format was conceptually flawed.

---

### Defect 4: Silent Truncation of 28 Lines in Slide 15 (`Room.java`)

```text
+-----------------------------------------------------------------------------+
| SILENT CODE TRUNCATION MECHANISM (Slide 15)                                 |
+-----------------------------------------------------------------------------+
  Room.java Total Lines = 97 lines
  Available Height      = 1304 px
  Theoretical Font Size = 1304 / (97 * 1.48) = 9.08 pt

  Script Clamp Logic:
    font_size = max(13, int(avail_h / (num_lines * 1.48)))
    Result: font_size clamped to 13 pt!

  At 13 pt:
    Line Height   = int(13 * 1.48) = 19 px
    Height Needed = 97 lines * 19 px = 1843 px
    Height Avail  = 1304 px (DEFICIT: 539 px)

  Rendering Loop in generate_15_prototypes.py:
    for row_idx, line in enumerate(lines):
        curr_y = pad_y + row_idx * line_h
        if curr_y + line_h > height - 10:
            break   <-- SILENT BREAK! NO WARNING! NO EXCEPTION!

  Execution Result:
    Loop broke at Line 70.
    Lines 70 through 97 (28 lines!) WERE SILENTLY DISCARDED.
+-----------------------------------------------------------------------------+
```

* **Underlying Flaw:** 
  The script claims "zero code truncation" in its evaluation documentation, but in reality clamped the font at 13 pt and silently executed `break`, discarding 28% of the entire source file!

---

## Comprehensive 15-Slide Forensic Audit Matrix

| Slide # | Category | Status | Primary Defect Identified |
| --- | --- | --- | --- |
| Slide 01 | Standalone Title | [PASS] | Pristine full-bleed presentation on Mantle. |
| Slide 02 | Standalone Text | [PASS] | Crisp typography and uniform margins. |
| Slide 03 | Standalone Diagram | [PASS] | Architecture hierarchy preserved cleanly. |
| Slide 04 | Standalone Table | [PASS] | Big-O growth functions and runtime table intact. |
| Slide 05 | Single Injection | [PASS] | Accurate box fit over `FirstJavaProgram`. |
| Slide 06 | Single Injection | [WARN] | Box right edge is within 18 px of explanatory text. |
| Slide 07 | Mixed Injection | [PASS] | In-slide code replaced; terminal output intact. |
| Slide 08 | Mixed Injection | [WARN] | Box inflated to 90% width; empty right-hand space. |
| Slide 09 | Mixed Injection | [WARN] | Box inflated to 90% width; empty right-hand space. |
| Slide 10 | Multi-Box 4-Q | [WARN] | Hardcoded margins cause slight inter-box asymmetry. |
| Slide 11 | Multi-Box | [FAIL] | PaymentsTester shifted to `x=0.40`; exposed code. |
| Slide 12 | Multi-Box | [WARN] | Misclassified: only 1 box exists (Single Injection). |
| Slide 13 | Adjacent Format | [FAIL] | Tofu tabs (115 boxes); tiny slide (53% dead space). |
| Slide 14 | Adjacent Format | [FAIL] | 16:9 slide shrunk to 45%; 765 px vertical dead space. |
| Slide 15 | Adjacent Format | [FAIL] | Tofu tabs (138 boxes); 28 lines silently truncated. |

---

## Architectural Remediation Plan

### 1. Robust Bounding Box Detection Protocol

Never rely on manual percentage guessing. Use a two-tier deterministic coordinate resolution engine:

```text
+-----------------------------------------------------------------------------+
| TWO-TIER DETERMINISTIC BOUNDING BOX RESOLUTION                              |
+-----------------------------------------------------------------------------+
  Tier 1: Poppler Vector Text Layout (Primary)
  - Execute `pdftotext -bbox-layout -f <p> -l <p> <pdf> -`
  - Match code tokens / class signatures in XML output.
  - Calculate exact bounding box: union of matched lines + 12 pt padding.
  - Scale from PDF coordinates (960x540) to raster DPI (200 DPI = 2.778x).
  - Accuracy: 100.0% mathematical precision.

  Tier 2: OpenCV Contour / Color Mask Detection (Fallback / Validation)
  - Detect existing slide code box rectangles via edge and color thresholding.
  - Cross-verify Tier 1 coordinates against OpenCV contour bounds.
+-----------------------------------------------------------------------------+
```

#### Correct Coordinates for Slide 11 (`Slide13_InheritancePart2.pdf`, Page 4):
At 200 DPI (`sw = 2667, sh = 1500`):
* **CardPayment (Top Left):** `x = int(sw * 0.018)`, `y = int(sh * 0.140)`, `w = int(sw * 0.465)`, `h = int(sh * 0.395)`
* **Payment (Top Right):** `x = int(sw * 0.495)`, `y = int(sh * 0.140)`, `w = int(sw * 0.485)`, `h = int(sh * 0.395)`
* **PaymentsTester (Bottom Left):** `x = int(sw * 0.018)`, `y = int(sh * 0.550)`, `w = int(sw * 0.560)`, `h = int(sh * 0.425)`
* **Terminal Output (Bottom Right):** Untouched at `x = int(sw * 0.590)`, `y = int(sh * 0.560)`.

---

### 2. Complete Tab Sanitization & Monospace Glyph Pipeline

Update `render_catppuccin_code_box()`:

```python
# 1. Expand tabs before processing
code_text = code_text.expandtabs(4)

# 2. Use true monospace font (NEVER Propo)
FONT_PATH = '/usr/share/fonts/TTF/JetBrainsMonoNerdFontMono-Bold.ttf'

# 3. Use getlength() instead of getbbox() for exact horizontal advance
cur_x += font.getlength(val)
```

---

### 3. Multi-Column Code Engine to Eliminate Code Truncation

When code exceeds the vertical capacity of a single column (e.g. `Room.java` with 97 lines, or `FileTester.java` with 57 lines):
* Do **NOT** shrink font below readable sizes (minimum 22 pt on 1440p).
* Do **NOT** silently drop lines via `break`.
* Automatically split long code into **Two Balanced Columns** side-by-side within the code container.
  - Column 1: Lines 1 through 48
  - Column 2: Lines 49 through 97
* This maintains a readable font size of 24–28 pt with 100% complete source rendering.

---

### 4. Aspect-Ratio-Aware Adjacent Layout Rules

* **Rule 1: Portrait Documents (Exams / Handouts):**
  Use Side-by-Side Adjacent Format (Left: Document, Right: Solution Code). Both panes share natural portrait aspect ratios (~0.77 to ~0.88).
* **Rule 2: Landscape 16:9 Slides with External Code:**
  Do **NOT** force a 50/50 horizontal split that destroys the 16:9 slide.
  Instead, use **Sequential Full-Size Presentation**:
  - **Slide A:** The 16:9 lecture slide presented at full 2560 x 1440 resolution.
  - **Slide B:** The full companion source file (`FileTester.java` or `LinkedList.java`) presented as a dedicated **Full-Canvas Code Compendium Slide** with a 2-column Catppuccin Mocha container at 28 pt font.

---

## Action Items for Implementation

1. **Update `render_catppuccin_code_box()`**:
   - Add `code_text = code_text.expandtabs(4)`.
   - Switch font to `/usr/share/fonts/TTF/JetBrainsMonoNerdFontMono-Bold.ttf`.
   - Replace `cur_x += (bbox[2] - bbox[0])` with `cur_x += font.getlength(val)`.
   - Add two-column support for files exceeding 45 lines.
   - Throw an explicit assertion error if any line is clipped rather than silently dropping code.
2. **Correct Slide 11 Coordinates**:
   - Move `PaymentsTester` from `x = sw * 0.40` to `x = sw * 0.018, y = sh * 0.550`.
3. **Correct Slides 8 & 9 Widths**:
   - Reduce code box width from `0.90` to `0.52` to preserve slide balance.
4. **Redesign Slides 13 & 14**:
   - Replace unbalanced half-slide squashing with sequential full-size presentation or 2-column code compendiums.
5. **Recompile & Validate**:
   - Re-run `pdftoppm` and re-generate all 15 PNGs.
   - Verify zero tofu boxes, zero truncated lines, and perfect bounding box alignment across all slides.
