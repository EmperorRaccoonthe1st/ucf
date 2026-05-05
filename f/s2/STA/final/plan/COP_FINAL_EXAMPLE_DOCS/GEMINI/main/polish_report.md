# Phase 3: Ocular Review & Polish Report

This report identifies stylistic, structural, and typesetting issues within the LaTeX source code of the COP3502 Final Exam Study Guide.

## 1. Critical Structural Errors

### 1.1 Global Chapter Image Switch
- **File:** `GEMINI/main/main.tex`
- **Issue:** The `\usechapterimagefalse` command is called before the Table of Contents but is never reset. This disables all chapter header images throughout the document.
- **Fix:** Add `\usechapterimagetrue` immediately after `\tableofcontents` or before the first `\part`.

### 1.2 Incorrect Chapter Image Placement
- **Requirement:** Every `\chapter{}` must be preceded by `\chapterimage{}`.
- **Affected Files:**
    - `GEMINI/main/chapters/chapter5_lists_stacks_queues.tex`: `\chapter` is on line 1, `\chapterimage` is on line 2.
    - `GEMINI/main/chapters/chapter6_trees.tex`: `\chapter` is on line 1, `\chapterimage` is on line 2.
- **Fix:** Swap the lines so `\chapterimage` comes first.

## 2. Typesetting Refinements (Overfull \hbox)

These issues cause text to bleed into the margins.

### 2.1 Chapter 5: Lists, Stacks, and Queues
- **Location:** Line 148 (Paragraph 148-149)
- **Problem:** `\texttt{ptr != NULL}` and `\texttt{ptr->next}` are non-breakable and exceed the margin by 8.1pt.
- **Fix:** Rephrase or inject breaks: `\texttt{ptr} \texttt{!= NULL}` and `\texttt{ptr->}\allowbreak\texttt{next}`.

### 2.2 Chapter 8: Tries and Hashing
- **Location:** Line 12 (Paragraph 12-13)
- **Problem:** `\texttt{is\_end\_of\_word}` is a long monolithic string, causing a 31.6pt overflow.
- **Fix:** Use `\texttt{is\_end\_}\allowbreak\texttt{of\_word}` to allow a hyphenation-free break.

### 2.3 Chapter 11: Exam Prep
- **Location:** Line 19 (Paragraph 18-19)
- **Problem:** The item "BST & Tries" exceeds the margin by 1.5pt.
- **Fix:** Slightly rephrase to: `\item \textbf{BST \& Tries:} Implementing recursion for counting or searching.` (removes "traversals" or "recursive").

## 3. Page Layout & Vertical Spacing (Underfull \vbox)

"Laddering" or large white space gaps occur where LaTeX cannot break large environments across pages.

### 3.1 Chapter 7: Heaps
- **Location:** Lines 22, 59, 78.
- **Issue:** The large mathematical proof for $O(n)$ Build-Heap and the Trace example are too tall to fit on remaining page space, causing massive gaps on preceding pages.
- **Fix:** Consider splitting the `theorem` block into "Theorem" and "Proof" (separate blocks) or using the `breakable` option if supported by the template's `tcolorbox` definition.

### 3.2 Chapter 1: C & DMA
- **Location:** Lines 22, 47.
- **Issue:** Large `definition` and `example` blocks at the end of sections are being pushed to new pages.
- **Fix:** Balance the text by moving implementation snippets or adding `\newpage` to manually control the break if the gap is visually jarring.

### 3.3 Chapter 3: Algorithm Analysis
- **Location:** Lines 16, 44.
- **Issue:** Clustered `definition` blocks for Big-O, Omega, and Theta are causing vertical stretching.
- **Fix:** Ensure there is enough body text between definitions to allow for flexible spacing.

## 4. Final Verification Checklist
- [ ] Run `tectonic main.tex` and verify `Overfull \hbox` is 0.0pt.
- [ ] Visually inspect PDF for chapter images on all 11 chapters.
- [ ] Check `\part` pages for consistency.
