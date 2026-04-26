# Chapter 3 Layout Review: Combinational Logic

## 1. Graphical Malformations
- **Incorrect Asset Usage:** Chapter 3 incorrectly uses `chapter_head_1.pdf` (the same image as Chapter 1). This is a major visual inconsistency compared to the template's requirement for unique chapter-specific graphics.
- **Title Box Misalignment:** The title "3. Combinational Logic" uses `\@makeschapterhead` logic which, in `structure.tex`, calculates the box width as `\paperwidth-\Gm@lmargin`. This extends the orange border all the way to the right edge of the page, rather than stopping at the right margin, creating a massive visual offset compared to Chapters 1 and 2.

## 2. Spacing & Layout Issues
- **Table Centering:** The truth table in Section 1.1 is enclosed in a `center` environment. However, because the section numbers are in the margin via `\llap`, the "center" of the text area is shifted. This causes the table to appear slightly off-center to the right relative to the page as a whole.
- **Box Crowding:** Section 5 (Standard Combinational Hardware) contains a rapid succession of `definition` boxes (Adders, Decoders, MUX, PLA). The `skipabove=25pt` and `skipbelow=25pt` values create large gaps of white space between boxes, while the internal `innertopmargin=5pt` remains too tight.

## 3. List Formatting
- **Procedure Lists:** In Section 6 ("Logic Design Procedure"), the `enumerate` list (Lines 233-241) is placed immediately after a `remark` environment. The lack of a `\clearpage` or sufficient `\vspace` causes the numbered list to crowd the orange "R" circle of the preceding remark.

## 4. Environment Continuity
- **Large Box Splitting:** The "Algorithm for Minimal Sum of Products" example (Section 4.2) is a large `example` environment containing a multi-step `enumerate` list. This box is highly likely to be cut across pages, which breaks the visual containment of the orange border.
