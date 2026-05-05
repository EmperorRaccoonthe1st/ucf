# Phase 3: Isolated Module Generation Directive (Expanded)

## 1. Objective
Draft the LaTeX source code for the Answer Key and Study Guide in small, "layout-protected" modules. This phase ensures that the fundamental building blocks of the documents are structurally sound before assembly.

## 2. Step 1: Mapping the Modules
- **Action:** The Orchestrator divides `draft_answers.md` and `study_content.md` into discrete LaTeX components.
- **Instruction:** "Assign each unique question or topic its own `.tex` file in `final/plan/STA_PLAN/isolated_tests/modules/` (e.g., `ans_Q1.tex`, `guide_NormalDist.tex`)."

## 3. Step 2: The "Structural Binding" Generation Loop
- **Action:** Spawn a "LaTeX Draftsman" sub-agent for each module.
- **Instruction:** "Generate the LaTeX for your assigned module. You MUST apply the following **Human-Grade Layout Rules**:"
    - **Rule 1: Prevent Page Splits.** Wrap the entire module in a `\bindcontent{...}` macro (as defined in `style_guide.tex`) or a `minipage` environment. The question header, the steps, and the answer MUST be treated as a single, atomic unit.
    - **Rule 2: List Padding.** Use `enumitem` within the module. Every `itemize` or `enumerate` block must have explicit vertical space before it (`\vspace{0.5em}`) to prevent the "AI crowding" effect.
    - **Rule 3: Formula Clarity.** Every key formula must be enclosed in the `\begin{formula}{Title} ... \end{formula}` environment. Use `\displaystyle` for fractions to ensure legibility.
    - **Rule 4: Dynamic Spacing.** End every module with a `\vspace{\fill}` (if not using minipage) to allow LaTeX to balance the content across the page later.
- **Output:** Individual validated `.tex` snippets.

## 4. Step 4: Bottom-Up Logic Initialization
- **Instruction to Agent:** "Do not assume you are part of a larger file. Write the module so it can be compiled on its own. Use `\section*` or `\subsection*` for headers so that combined numbering can be handled by the master document or manual overrides."

## 5. Constraints
- **Style Alignment:** Strictly use the packages and definitions provided in `final/plan/STA_PLAN/style_guide.tex`.
- **No Orphaned Lines:** If a module is naturally longer than half a page, the agent must check if it's better to split it into two *logical* minipages (e.g., Question and Steps 1-2, then Steps 3-4 and Answer) or keep it as one.
