# STA 2023 Final Exam Project: Master Outline

## 1. Project Overview
This project transforms raw course materials and a practice final exam into a professional, human-grade Answer Key and targeted Study Guide. It utilizes a **Chronological-Modular Architecture** with a **Bottom-Up Validation** loop to ensure layout perfection and mathematical accuracy.

## 2. Global Directory Structure
```text
STA_PLAN/
├── master_outline.md       # This document (Strategic Roadmap)
├── style_guide.tex         # Unified LaTeX preamble and styling (No Legrand Orange)
├── phase_n.md              # Explicit instructions for each phase
├── intermediate/           # Source of Truth (Markdown)
│   ├── draft_answers.md    # Sequential math solutions
│   ├── target_topics.md    # Filtered topic list from exam
│   └── study_content.md    # Extracted theory/formulas
├── isolated_tests/         # Bottom-Up Ocular Review Workspace
│   └── modules/            # Standalone .tex components
└── output/                 # Final PDF artifacts
```

## 3. Operational Phases

### Phase 1: Sequential Analysis & Solving
- **Goal:** Solve the practice final and map the "Spine" of the study guide.
- **Artifacts:** `draft_answers.md`, `target_topics.md`.
- **Constraint:** Must follow the exact order of the practice exam.

### Phase 2: Surgical Extraction
- **Goal:** Extract relevant formulas and theory from `documents/` based on Phase 1 targets.
- **Artifacts:** `study_content.md`.
- **Constraint:** Exclude any topic not appearing on the practice final.

### Phase 3: Isolated Module Generation
- **Goal:** Draft small, protected LaTeX modules for each question/topic.
- **Artifacts:** `isolated_tests/modules/*.tex`.
- **Constraint:** Use `minipage` and `needspace` to prevent internal page splits.

### Phase 4: Bottom-Up Ocular Assessment
- **Goal:** Render and verify every module in isolation.
- **Artifacts:** Isolated PDFs and remediated `.tex` snippets.
- **Methodology:** Work from the bottom up, ensuring no large gaps or crowded elements.

### Phase 5: Master Integration & Final Global Review
- **Goal:** Combine modules into the final documents and perform a global page-flow check.
- **Final Artifacts:** `STA_Final_Answer_Key.pdf`, `STA_Final_Study_Guide.pdf`.

## 4. Technical Guardrails
- **Class:** `article` (Clean, standard, reliable).
- **Binding:** `minipage` for question/answer units.
- **Spacing:** `\vspace{\fill}` and `needspace` for human-grade layout.
- **Math:** `amsmath` and `tcolorbox` (unbreakable) for definitions.
