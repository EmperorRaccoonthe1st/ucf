# Prompt Architecture Review: CHM_GEMINI.md

## 1. Core Role and System Architecture
The prompt establishes a **Master Orchestrator Persona**, defining the primary agent as an elite manager rather than a worker. It employs a **Role-Based (Pipeline) Swarm Architecture**, where tasks are distributed among specialized subagents (Topic Analyzer, Skill Extractor, LaTeX Draftsman, etc.). This ensures that the high-level orchestrator maintains strategic oversight while delegating "brute-force" execution to smaller, focused units.

## 2. Context Preservation Strategy
To prevent context saturation and hallucinations, the architecture utilizes:
- **Intermediate Markdown Files:** Subagents record findings in discrete `.md` files (`topics.md`, `skills.md`), which serve as the "memory" of the project.
- **Summarized Reading:** The Orchestrator is instructed to read only these summarized outputs rather than raw data.
- **Task Granularity:** Large tasks are broken down (e.g., assigning specific page ranges to different agents) to ensure no single agent is overwhelmed.
- **Model Selection:** Directs the use of high-reasoning models for technical tasks and standard models for formatting.

## 3. Document & Tooling Specifications
The system is anchored in a professional technical stack:
- **Typesetting:** LaTeX is the mandatory engine.
- **Compiler:** **Tectonic** is specified for its automated dependency management and streamlined CLI interface.
- **Chemistry-Specific Packages:**
  - `mhchem`: For chemical formulas and equations.
  - `chemfig`: For Lewis structures and molecular geometry (native code only, no external images).
  - `siunitx`: For precise unit and significant figure handling.
  - `pgfplots`/`tikz`: For native graphical data.

## 4. Detailed Execution Phases
The workflow is divided into three rigorous phases:
- **Phase 1: Topic Extraction:** Involves scanning source PDFs, extracting specific skills, and a dedicated verification round to ensure 100% coverage.
- **Phase 2: Source Code Generation:** Includes creating a `plan.md` and `style.md` before spawning a swarm of LaTeX Draftsmen to write individual chapters. It concludes with an integration and compilation test.
- **Phase 3: Final Style Review & Polish:** Features a baseline stylistic evaluation, an "Ocular Review Swarm" for rendered output, and a final remediation/verification loop.

## 5. Rules of Engagement and Failure Modes
- **Rule of Autonomy:** The Orchestrator has full authority to spawn subagents without user intervention.
- **Rule of Explicitness:** Mandates the manual injection of context (`style.md`, `plan.md`) into subagent prompts to overcome lack of shared state.
- **Hallucination Mitigation:** Specific checks for chemical validity (e.g., "Texas Carbon" check) are integrated into the verification steps.
- **Iterative Refinement:** Establishes a "success or retry" loop for compilation and style checks.

## 6. Strengths and Weaknesses Observed

### Strengths
- **Rigorous Modularity:** The separation of concerns between extraction, drafting, and review is exceptionally clear.
- **Remediation Excellence:** The inclusion of a remediation phase was a massive success. The use of a Python script (`fix_latex_comprehensive.py`) to programmatically ensure consistency across chapters prevented context drift.
- **Technical Tooling:** Mandating `mhchem`, `chemfig`, and `siunitx` directly resulted in professional-grade chemical visualizations and precise unit handling.
- **Ocular Review Swarm:** This phase successfully identified semantic and stylistic issues (like box distinction and solubility rules) that automated linters would miss.

### Weaknesses
- **Directory Path Failure:** The "CRITICAL" instruction regarding the hardcoded `.js` path failed. This path was ignored in the actual implementation, likely due to its unconventional nature and the agent's preference for local project roots.
- **Orchestration Complexity:** Managing fragments (topics vs. skills) required a heavy "Planning" phase to re-assemble. This led to a deviation from the modular chapter file structure into a single `main.tex`.
- **Prompt Sensitivity:** Success relied heavily on the Orchestrator's ability to accurately pass context; any slip in "The Rule of Explicitness" could have broken the pipeline.

## 7. Evidence-Backed Insights (Artifact Linkage)
- **Scripted Remediation vs. Quality:** The use of `fix_latex_comprehensive.py` (stemming from Phase 3 instructions) ensured that Chapters 4-8 were as polished as Chapter 1, proving that programmatic remediation is superior to manual agent edits for large documents.
- **Directory Rigidness:** The failure to use the specified `.js` directory path suggests that prompts should avoid overly complex or unconventional file paths unless the environment is pre-configured to handle them.
- **Symbolic Precision:** The prompt's focus on "rules and algorithms" for chemistry resulted in a high-utility reference guide, whereas a more narrative approach might have missed the procedural "Skills" that the extraction phase captured so well.
