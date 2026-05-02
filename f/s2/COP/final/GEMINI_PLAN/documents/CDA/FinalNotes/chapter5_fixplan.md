# Chapter 5: Local Fix Plan

## Objective
Fix localized layout issues in `main/chapters/chapter5.tex`.

## Actionable Steps
1. **CRITICAL Asset Fix:**
   - Line 1: Uncomment `\chapterimage{chapter_head_1.pdf}` (Asset now exists).

2. **List Padding (High Priority):** 
   - Lines 17, 25, 48, 73, 101, 116, 133: Ensure blank lines exist before and after ALL nested `itemize` and `enumerate` blocks within definition/proposition boxes.

3. **Box Crowding:**
   - Line 15-39: Insert `\medskip` or blank lines between the four consecutive `definition` boxes (Half Adder through Carry-Lookahead) to prevent them from merging into one visual block.

4. **Page Break Prevention:**
   - Line 70: Apply `nobreak=true` to the "Restoring Division Algorithm" box.
   - Line 98: Apply `nobreak=true` to the "Booth's Step-by-Step" box.

5. **Math Delimiters:**
   - Ensure all instances of `$result$` are changed to `$\text{result}$`.