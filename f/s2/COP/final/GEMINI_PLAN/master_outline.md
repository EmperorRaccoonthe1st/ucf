# COP3502 Study Guide: Master Pipeline Architecture

## 1. Overview
This architecture defines a rigorous, three-phase swarm pipeline to transform raw Computer Science 1 materials into a professional LaTeX study guide. It utilizes a **Modular-Hybrid approach**, combining narrative continuity with procedural skill extraction.

## 2. Global Directory Structure
```text
GEMINI/
├── GEMINI.md               # The master project instructions
├── intermediate/
│   └── summaries/          # Topic-specific Markdown summaries
└── main/
    ├── main.tex            # Master LaTeX entry point
    ├── chapters/           # Individual .tex chapter files
    ├── structure.tex       # Template structural definitions
    ├── bibliography.bib    # Citations
    └── StyleInd.ist        # Index style
```

## 3. Operational Phases
### [Phase 1: Knowledge Extraction](phase_1_extraction.md)
- **Goal:** Exhaustive extraction of theory, code, and skills from PDFs and C files.
- **Agents:** Swarm of `generalist` Topic Extractors.
- **Verification:** Cross-check agents to ensure 100% coverage of Foundation Exam topics.

### [Phase 2: LaTeX Structural Drafting](phase_2_latex.md)
- **Goal:** Conversion of validated `.md` summaries into styled LaTeX source.
- **Agents:** `generalist` LaTeX Architects.
- **Verification:** Structural review agents to ensure adherence to the Legrand Orange Book template.

### [Phase 3: Final Polish & Compilation](phase_3_polish.md)
- **Goal:** Tectonic compilation, ocular review, and programmatic remediation.
- **Agents:** `generalist` Ocular Reviewers & Remediation Swarm.
- **Outcome:** A pristine, multi-chapter `COP3502_FINAL_REVIEW.pdf`.
