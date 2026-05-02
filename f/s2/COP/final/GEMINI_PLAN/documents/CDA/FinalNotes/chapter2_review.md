# Chapter 2 Layout Review: Number Systems and Binary Representation

## 1. Graphical Malformations
- **Header Image Scaling:** The `chapter_head_2.pdf` image shows the same vertical positioning issue as Chapter 1. The title "2. Number Systems and Binary Representation" is anchored at -9cm, which frequently overlaps with the lower third of the header graphic, causing a cluttered appearance.

## 2. Spacing & Layout Issues
- **Orange Outlines & Headers:** Bolded headers for `example` environments (e.g., Example 2.1, 2.2) are placed within a `blacknumex` style that does not have sufficient `skipabove` when following another environment. This results in the orange line of a previous `remark` box being too close to the subsequent `example` header.
- **Vocabulary Box Spacing:** The `vocabulary` box for "Sign Bit" (Section 3) suffers from the same `5pt` tight `innertopmargin` as seen in Chapter 1, creating a cramped visual flow.

## 3. List Formatting
- **Manual Indentation Issues:** In Section 3.4 ("Sign Extension"), the nested `itemize` blocks for "Unsigned" and "Signed" (Lines 112-116) lack consistent preceding blank lines. This results in the bullet points appearing too high relative to their introductory text.
- **Arithmetic Steps:** In the "Decimal to Binary" example, the list of division steps (Lines 45-51) is correctly separated, but the `topsep` set in `structure.tex` (`8pt`) makes the list feel detached from the "Convert (19)_10 to binary" prompt.

## 4. Environment Continuity
- **Broken Equations:** In the "Base b Expansion" theorem (Section 1), if the theorem box is placed near the bottom of a page, the math expansion $n = a_k b^k + \dots$ can be cut off from the theorem header, leaving the orange frame incomplete on the first page.
