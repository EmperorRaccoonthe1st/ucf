# COP3502 Study Guide: Prompt Style & Constraints

## 1. LaTeX Framework & Tooling
- **Engine:** LaTeX with **Tectonic** for local compilation (`tectonic main.tex`).
- **Template:** "The Legrand Orange Book".
- **Modularity:** 
    - Master file: `GEMINI/main/main.tex`.
    - Included files: `\input{chapters/filename}`.
    - Style file: `StyleInd.ist`, `bibliography.bib`.

## 2. Structural Environments (Mandatory)
Every chapter MUST utilize these environments to structure information:
- `\begin{definition}[Name]`: For core data structures or terms.
- `\begin{theorem}[Name]`: For mathematical formulas (Summations, Recurrences).
- `\begin{example}[Name]`: For tracing algorithms (e.g., "Tracing Quick Sort on Array A").
- `\begin{remark}`: For "Pitfalls & Pointers" (e.g., "Don't forget to free the temp node").
- `\begin{exercise}`: For practice problems derived from labs/exams.

## 3. C Code Styling
- **Package:** `minted` or `lstlisting` (as configured in the template).
- **Standard:** Use clean, readable C code. Prioritize manual logic over complex library calls to match the student's learning level.
- **Comments:** Keep code comments minimal but high-impact (e.g., "Base case", "Recursive step").

## 4. Tone & Voice
- **Persona:** A patient, rigorous Senior Teaching Assistant.
- **Style:** Precise, technical, but accessible. Avoid fluff; use bullet points and bold text for key takeaways.
- **Language:** Grounded in UCF CS1 terminology (e.g., "PAs", "Labs", "Foundation Exam prep").

## 5. Naming Conventions
- All intermediate summaries: `topic_name.md`.
- All chapter files: `chapter_n_topic.tex`.
- Final output: `COP3502_FINAL_REVIEW.pdf`.
