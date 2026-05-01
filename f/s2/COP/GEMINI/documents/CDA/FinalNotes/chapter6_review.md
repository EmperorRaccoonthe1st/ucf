# Chapter 6 Review: MIPS Instruction Set Architecture (ISA)

## 1. Graphical & Header Malformations
- **Header Image Obstruction:** Like Chapter 4, the `chapter_head_2.pdf` image height (calculated at 448pt) exceeds the 400pt `\vspace` limit, causing the top portion of the "Register File" section to be partially obscured by the image.
- **Centering Misalignment:** The chapter title frame on the header page appears slightly offset to the right, likely due to the `oneside` configuration not correctly balancing the `\Gm@lmargin` in the `tikzpicture` node.

## 2. Spacing & Layout Issues
- **List Formatting:**
  - **Lines 56, 72, 105, 118:** Multiple `itemize` lists follow headers or text without blank lines. 
  - **Line 59:** The sub-list for "Hi and Lo" registers lacks proper indentation and vertical spacing, making it difficult to distinguish from the primary list item.
- **Environment Spacing:**
  - **Line 11:** `\begin{definition}[Register File]` is too close to `\section{Register File}`.
  - **Line 31:** The `table[h]` containing the MIPS Register Convention is placed immediately after a `subsection` header. The proximity of the table's `\toprule` to the section text is visually jarring.
  - **Line 68:** `\begin{definition}[Word Alignment]` follows `\section{Memory Layout}` too closely.
- **Orange Outlines:** The orange outlines around definitions (Lines 11, 68) are too close to the bolded titles "Register File" and "Word Alignment."

## 3. Centering & Alignment
- **Table Centering:** The Instruction Format tables (Lines 107, 120, 131) are centered but lack sufficient vertical padding, making the 32-bit field boxes appear crowded between the preceding text and the following bullet points.

## 4. Page Break Malformations
- **Table Cuts:** The "MIPS Register Convention" table (line 31) is large. If it does not fit on the page after the section header, it may be pushed to the next page, leaving a significant white gap (orphaned header) on the previous page.
- **Box Cuts:** The `Addressing Modes` enumeration (line 134) is long and lacks a containing box, but its proximity to the bottom of the chapter suggests it may be split awkwardly across the final pages.
