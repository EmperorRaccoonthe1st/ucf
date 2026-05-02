# Chapter 9 Review: Exceptions and Interrupts

## 1. Header and Title Layout
- **Header Image Obstruction**: The image `chapter_head_1.pdf` is correctly placed at the top, but the title box ("9. Exceptions and Interrupts") is positioned at a fixed `-9cm` from the top margin. While not directly "obstructed" in terms of legibility, the lack of dynamic scaling means the circuit board graphic is partially hidden by the semi-transparent white box.
- **Excessive Spacing**: The `\par\vspace*{400\p@}` command in `structure.tex` creates a massive vertical gap (approx. 14cm) between the chapter title and the first section (9.1). This pushes the actual content too far down the page, leaving nearly 60% of the first page empty.

## 2. Environment Malformations
- **Vocabulary Consistency**: Vocabularies 9.1 through 9.7 (Overflow, NEWPC, FENCE, etc.) are rendered as plain bold text with no surrounding box. This deviates from the professional "boxed" look of the Definition environments (e.g., 9.1.1).
- **Proximity Errors**: Definitions 9.3.2 (Cause Register) and 9.3.3 (Status Register) are placed very close to their preceding subsection headers. The `skipabove` parameter in `mdframed` is partially negated by the lack of blank lines in the source file.
- **Orange Outline Alignment**: In the Definition boxes, the orange vertical line (linewidth 4pt) is only 5pt (`innerleftmargin`) away from the bolded "Definition" header. This makes the text feel cramped against the border.

## 3. List Formatting and Spacing
- **Missing Newlines**: In Definition 9.2.1 (Interrupt Handler Vector), the `itemize` list is preceded by a colon, but in the PDF, the first bullet point is not sufficiently separated from the introductory text due to the `enumitem` configuration combined with the `mdframed` environment.
- **Source Code Omissions**: Several environments (e.g., Remark in Section 9.4.1) are missing a blank line before the `\begin{enumerate}` block in `chapter9.tex`. This prevents LaTeX from treating the list as a new paragraph, leading to compressed vertical spacing.

## 4. Page Layout and Breaks
- **Pagination**: Section 9.3.3 (Handler Actions) begins at the bottom of page 65. The numbered list (1-4) is split across pages 65 and 66, which is acceptable but visually disruptive given the large void on page 63.
- **Margin Consistency**: Section numbers (9.1, 9.2, etc.) are correctly placed in the left margin using `\llap`, matching the template's style.
