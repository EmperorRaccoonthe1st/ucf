# Phase 3: Final Polish & Compilation Directive

## 1. Objective
Execute final Tectonic compilation, perform semantic "Ocular" reviews, and apply global remediation to ensure a perfect final study guide.

## 2. Step 1: Initial Compilation Test
- **Orchestrator Action:** Run `tectonic main.tex` from the `GEMINI/main/` directory.
- **Error Handling:** If compilation fails, spawn a "Debugging Agent" to parse the `.log` and fix the specific `.tex` line error.

## 3. Step 2: Ocular Review Swarm
- **Agent:** "Ocular Reviewer".
- **Instruction:** "Review the rendered document structure (or the semantic mapping of the LaTeX). Check for: 
    - Text overflowing margins.
    - Box collision or 'laddering'.
    - Consistency in header capitalization.
    - Consistency in C code indentation."
- **Output:** Log specific issues with file and line numbers to `GEMINI/main/polish_report.md`.

## 4. Step 3: Programmatic Remediation
- **Agent:** "Global Remediation Agent".
- **Instruction:** "Read `polish_report.md`. Implement fixes across all chapter files. Ensure all `remark` boxes have consistent vertical spacing and all `example` traces are properly formatted."
- **Optional Scripting:** The agent may write a Python script to automate search-and-replace for global styling fixes.

## 5. Step 4: Final Verification
- **Orchestrator Action:** Perform one final Tectonic build.
- **Confirmation:** Ensure the resulting `COP3502_FINAL_REVIEW.pdf` is located in the root `GEMINI/` folder.
