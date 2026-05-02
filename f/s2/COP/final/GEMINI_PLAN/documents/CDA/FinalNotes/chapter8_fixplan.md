# Chapter 8: Local Fix Plan

## Objective
Fix localized layout issues in `main/chapters/chapter8.tex`.

## Actionable Steps
1. **CRITICAL Table Fix:**
   - Line 103 (approx): Convert Table 8.2 (Control Signal Truth Table) to use the `tabularx` environment with `X` columns to force text wrapping and prevent margin overflow.
   - Line 140 (approx): Apply `\centering` and `\small` to Table 8.3.

2. **List Padding:** 
   - Lines 127, 136, 148, 158: Add blank lines before and after every `itemize` block.
   - Line 158: Fix indentation consistency for "Combinational Elements" list to match "State Elements."

3. **Box Padding:**
   - Lines 36-65: Insert `\vspace{-10pt}` or similar between the sequence of 9 vocabulary boxes to reduce the "ladder" gap and improve page utilization. (Or consider merging into one box).

4. **Environment Proximity:**
   - Ensure blank lines exist between section headers and the first content boxes.