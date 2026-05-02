# Chapter 6: Local Fix Plan

## Objective
Fix localized layout issues in `main/chapters/chapter6.tex`.

## Actionable Steps
1. **List Padding:** 
   - Lines 56, 72, 105, 118: Add blank lines before `itemize` blocks.
   - Line 59: Add blank line before the nested `itemize` for "Hi and Lo" to fix the indentation/merging issue.

2. **Environment Proximity:**
   - Line 11: Add blank line before `\begin{definition}[Register File]`.
   - Line 31: Add `\vspace{15pt}` before `\begin{table}[h]` to separate the Register Convention table from the subsection header.
   - Line 68: Add blank line before `\begin{definition}[Word Alignment]`.

3. **Table Padding:**
   - Lines 107, 120, 131: Add `\vspace{5pt}` before and after the tabular blocks inside the I-Type and J-Type sections to improve vertical rhythm.

4. **Page Break Prevention:**
   - Line 31: Add `\needspace{5cm}` before the Register Convention table to prevent it from being orphaned on a new page.