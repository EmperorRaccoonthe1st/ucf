# Phase 2: LaTeX Structural Drafting Directive

## 1. Objective
Transform the validated Markdown summaries from `GEMINI/intermediate/summaries/` into styled LaTeX chapter files.

## 2. Step 1: Template Setup
- **Orchestrator Action:** Ensure `GEMINI/main/main.tex` and `structure.tex` are initialized with the Legrand Orange Book settings.
- **Orchestrator Action:** Verify `StyleInd.ist` and `bibliography.bib` are present.

## 3. Step 2: Swarm Drafting
For each `.md` summary, spawn a "LaTeX Architect" subagent:
1.  **Context Injection:** Provide the agent with the `GEMINI_PLAN/prompt_style.md` content.
2.  **Instruction:** "Convert `summary_name.md` into `chapter_n_name.tex`. Use the mandatory environments (`definition`, `example`, `remark`). Ensure all C code is wrapped in `minted` or `lstlisting`."
3.  **Output:** Write to `GEMINI/main/chapters/chapter_n_name.tex`.

## 4. Step 3: Structural Verification
- **Agent:** "Structural Reviewer".
- **Instruction:** "Read the generated `.tex` file. Check for: 1. Correct environment usage. 2. Proper escaping of LaTeX special characters in code. 3. Adherence to chapter image requirements."
- **Remediation:** Fix errors immediately using the `replace` tool.

## 5. Step 4: Master Integration
- **Orchestrator Action:** Update `main.tex` with `\input{chapters/chapter_n_name}` for all generated chapters.
- **Orchestrator Action:** Ensure chapters are in logical pedagogical order.
