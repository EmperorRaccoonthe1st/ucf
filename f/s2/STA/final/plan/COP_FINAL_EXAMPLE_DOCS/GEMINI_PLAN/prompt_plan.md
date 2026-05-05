# COP3502 Study Guide: Strategic Prompt Plan

## 1. Hybrid Orchestration Architecture
The project will follow a **Modular-Hybrid Architecture**:
- **Primary Structure:** Modular Chapters (CDA model) for narrative continuity of algorithmic logic.
- **Secondary Structure:** Specialized extraction of "Skills & Pitfalls" (CHM model) to populate high-value reference boxes within each chapter.

## 2. Multi-Phase Swarm Pipeline
### Phase 1: Modular Extraction & Skill Matrix
- **Agent:** `generalist` (Topic Extractors).
- **Task:** Process source PDFs and C files for a specific topic (e.g., "AVL Trees").
- **Output:** A comprehensive `.md` summary containing:
    - Theoretical Concept.
    - Algorithmic Logic (step-by-step).
    - C Implementation snippets.
    - "Skills & Pitfalls" list (Big-O, memory management).
- **Storage:** `GEMINI/intermediate/summaries/`.

### Phase 2: Orchestrated LaTeX Drafting
- **Agent:** `generalist` (LaTeX Architects).
- **Task:** Transform validated Markdown summaries into modular LaTeX files.
- **Constraints:** Strict adherence to `style.md` and Legrand Orange Book environments.
- **Storage:** `GEMINI/main/chapters/`.

### Phase 3: Verification & Ocular Remediation
- **Agent:** `generalist` (Ocular Reviewers).
- **Task:** Compile via Tectonic and review the rendered output.
- **Remediation:** A final "Global Fixer" agent (or script) to resolve cross-chapter styling inconsistencies and layout collisions.

## 3. Context Protection & Delegation
- **Context Preservation:** No single agent reads the entire `documents/` directory. Each subagent is scoped to a specific file set.
- **Intermediate State:** The `.md` summaries act as the "Source of Truth" to prevent hallucination during the complex LaTeX generation phase.
- **The Rule of Explicitness:** Every delegation prompt MUST contain the relevant snippets of `style.md` and the chapter's specific goals.
