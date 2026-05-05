# Chapter 4 Review: Sequential Logic Design

## 1. Graphical & Header Malformations
- **Header Image Obstruction:** The header image `chapter_head_2.pdf` is scaled to `\paperwidth`, resulting in a calculated height of approximately 448pt based on its 4:3 aspect ratio. Since the chapter content is only offset by `\vspace*{400pt}` (approx. 14.1cm), the bottom 48pt (approx. 1.7cm) of the image obstructs the first 3-4 lines of the chapter text.
- **Title Alignment:** The chapter title "4. Sequential Logic Design" is placed in a semi-transparent box at 9cm from the top. While centered in its own frame, the overall layout feels top-heavy due to the image height mismatch.

## 2. Spacing & Layout Issues
- **List Formatting:**
  - **Line 14:** `\begin{itemize}` for memory elements follows the introductory sentence without a blank line. This causes the list to render with insufficient vertical separation from the preceding paragraph.
  - **Line 116:** `\begin{itemize}` follows the `\section{Counters & Registers}` header without a blank line, causing a cramped transition.
- **Environment Spacing:**
  - **Line 26:** The `definition` box for "Latch" is placed immediately after the `\section{Latches}` header. This results in the "orange outline too close to bolded header" error, where the top border of the environment box almost touches the section title.
  - **Line 100:** The `vocabulary` box for "Duty Cycle" starts immediately after the `\section{Timing Methodologies}` header, repeating the crowding issue.
- **Orange Outlines:** The orange border of the `definition` box on line 10 is too close to the "Sequential Circuits" bolded term inside, lacking internal padding (consistent with `inner sep` observations in `structure.tex`).

## 3. Centering & Alignment
- **Table Offsets:** The truth table for the NOR-based S-R Latch (line 32) uses `\centering`, but because it is placed inside a `table[h]` environment without sufficient vertical buffers, it appears misaligned relative to the surrounding `proposition` and `remark` boxes.

## 4. Page Break Malformations
- **Box Cuts:** The `example` environment (1001 Overlapping Pattern Recognizer) on line 131 contains a multi-step `enumerate` list. Given its length and position toward the end of the chapter, it is highly susceptible to being cut across pages, which breaks the visual continuity of the "example" box.
