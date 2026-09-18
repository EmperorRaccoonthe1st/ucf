# ENC 3250 Document Pipeline Evaluation: Professional Information Product (PIP)

* **Evaluation Target:** [`summaries/GEMINI.md`](file:///home/owen/ucf/so/s1/ENC/summaries/GEMINI.md)
* **Project Specification:** [`projects/Professional_Infromation_Produc/prompt.txt`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/prompt.txt)
* **Active Working Directory:** [`projects/Professional_Infromation_Produc/`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/)
* **Evaluator:** Antigravity AI Partner
* **Status:** Complete Architecture Assessment

---

## 1. Executive Summary

This evaluation examines the document creation pipeline documented in [`summaries/GEMINI.md`](file:///home/owen/ucf/so/s1/ENC/summaries/GEMINI.md) against the requirements for the **Professional Information Product (PIP)** defined in [`prompt.txt`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/prompt.txt). 

The existing pipeline provides an outstanding academic publication foundation for MLA 9 essays, reflective logs, and genre studies. However, the PIP introduces a structural and typological challenge: it requires merging a **workplace technical document** (which demands modular, scannable, non-academic graphic design) with a **formal academic rationale** (which strictly demands MLA 9 double-spaced formatting and bibliography) and a **prototype artifact** into a **single unified submission file**.

```text
┌────────────────────────────────────────────────────────────────────────┐
│               ENC 3250 PIP COMPOSITE DELIVERABLE ENGINE                │
├────────────────────────────────┬───────────────────────────────────────┤
│ Deliverable Component          │ Layout / Typography Standard          │
├────────────────────────────────┼───────────────────────────────────────┤
│ 1. Professional Product (PIP)  │ Technical / Scannable Guide (Modular) │
│ 2. Rhetorical Rationale        │ Strict MLA 9 Academic (Double-Spaced) │
│ 3. Prototype Review Artifact   │ Annotated Draft / Visual Evidence     │
│ 4. Works Cited Page            │ Standalone MLA 9 Hanging Indent       │
└────────────────────────────────┴───────────────────────────────────────┘
```

Below is the component-by-component audit, gap analysis, and blueprint for adapting the pipeline.

---

## 2. Pipeline Readiness & Rubric Alignment Audit

The table below measures the current pipeline against the explicit submission criteria in [`prompt.txt`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/prompt.txt).

| Prompt Requirement | Pipeline Capability | Status & Diagnostic |
| :--- | :--- | :--- |
| **Deliverable Packaging** | Single-file multi-part build | `[WARN]` Pipeline assumes single-genre documents. |
| **PIP Design & Layout** | Scannable workplace technical format | `[WARN]` Engine defaults to academic double spacing. |
| **Rationale Scope** | 750–1,000 word MLA 9 essay | `[PASS]` Full ReportLab MLA 9 framework available. |
| **Rationale Topics (7)** | 7 distinct rhetorical categories | `[PASS]` Well aligned with course analytical habits. |
| **Module 1 Citations** | Minimum 2 readings (Porter, Henze) | `[PASS]` Master bibliography contains full entries. |
| **Wheeler Citation** | Citation from Dr. Wheeler materials | `[FAIL]` Missing from GEMINI.md Section 7. |
| **Prototype Inclusion** | Retain original prototype | `[INFO]` Requires asset staging and compilation hook. |
| **Terminal Viewing** | Clean source Markdown for `glow` | `[PASS]` Compliant with user configuration. |

---

## 3. Critical Gap Analysis

### Gap 1: Dual-Layout Typology Conflict

The primary architectural mismatch between [`summaries/GEMINI.md`](file:///home/owen/ucf/so/s1/ENC/summaries/GEMINI.md) and [`prompt.txt`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/prompt.txt) lies in layout density:

* **Current Pipeline Assumption:** Standardizes on homogeneous MLA 9 typesetting: 1.0-inch margins, double line spacing (`leading=24`), 0.5-inch paragraph indentation, Times-Roman 12pt throughout.
* **Project Need (Deliverable 1):** The "VS Code Vim Quickstart / How-To Guide" is a workplace document. Workplace technical writing principles (Mizrahi, Melonçon et al.) mandate scannability, tables, code blocks, keyboard badges (`<Esc>`, `dd`, `:w`), and tight visual hierarchy. If compiled as an MLA 9 double-spaced essay, the product fails the prompt mandate to "demonstrate intentional visual/design choices" and "be easy to scan and navigate."
* **Project Need (Deliverables 2 & 3):** The Rhetorical Rationale and Works Cited must strictly adhere to academic MLA 9.

> **Important:** The compilation engine must support **hybrid styling**: switching styles between the technical product section (compact leading, headers, tabular cheat sheets, callouts) and the academic rationale section (double spacing, first-line indents, running headers).

---

### Gap 2: Single-File Unified Packaging

The prompt stipulates:
> *"All three deliverables should be contained in one document/file."*

Currently, our compilation scripts (`compile_infoinventory.py`, `compile_genre_detective.py`) compile standalone assignments. The PIP project requires a multi-stage compilation engine:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        COMPOSITE PIP FLOWABLE                          │
│                                                                        │
│   [ Part 1: PIP Technical Guide ]                                      │
│        └── Modular headers, tables, shortcut boxes, callouts           │
│   [ PageBreak() ]                                                      │
│   [ Part 2: Rhetorical Rationale ]                                     │
│        └── MLA identification block, Lopez running head, 750-1000 w    │
│   [ PageBreak() ]                                                      │
│   [ Part 3: Prototype Artifact & Review Feedback ]                     │
│        └── Comparative figures, prototype draft, peer notes            │
│   [ PageBreak() ]                                                      │
│   [ Part 4: Standalone Works Cited ]                                   │
│        └── Module 1 readings + Dr. Wheeler course materials            │
└────────────────────────────────────────────────────────────────────────┘
```

---

### Gap 3: Missing Dr. Stephanie Wheeler Citation Standard

[`prompt.txt`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/prompt.txt) explicitly requires:
> *"Include at least one citation from Dr. Stephanie Wheeler's course materials."*

Section 7 of [`summaries/GEMINI.md`](file:///home/owen/ucf/so/s1/ENC/summaries/GEMINI.md) provides citation templates for Porter, Henze, Mizrahi, Melonçon et al., Lumen Learning, and Gerdes, but does not yet specify the citation format for Dr. Stephanie Wheeler.

To fulfill this requirement, we must standardize the citation entry based on course lecture materials or module overviews:

* **Works Cited Entry Template:**
  ```text
  Wheeler, Stephanie. "Module 1: Rhetorical Foundations and Workplace Genres." ENC 3250: Professional and Technical Writing, University of Central Florida, 2026. Webcourses@UCF.
  ```
* **In-Text Parenthetical:** `(Wheeler)` or `(Wheeler, "Module 1")`.

---

### Gap 4: Prototype Preservation & Iteration Tracking

The project guidelines require submitting:
1. The Final Professional Information Product
2. The Rhetorical Rationale
3. The Original Prototype
4. Evidence of incorporating feedback from the prototype review

In our local workspace:
* [`infoinventory.pdf`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/infoinventory.pdf) provides the preliminary Information Inventory and "So What?" table.
* [`assigments/draft/audienceprofile.md`](file:///home/owen/ucf/so/s1/ENC/assigments/draft/audienceprofile.md) provides the target audience definition (UCF CS students using VS Code).
* We need dedicated staging for the initial prototype version (e.g., [`prototype.md`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/prototype.md)) and an outline of prototype review feedback received.

---

### Gap 5: Course GenAI Policy Compliance

[`prompt.txt`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/prompt.txt) contains the following notice:
> *"This project is not eligible for support from GenAI to draft, construct, or write any component of."*

> **Warning:** Academic integrity guidelines require that all final text, substantive arguments, rhetorical justifications, and original drafting originate from the student (Owen Lopez). 
> 
> The Antigravity environment and pipeline should be utilized strictly for:
> * Pipeline engineering and automation (`ReportLab` layout scripting).
> * Verification of MLA 9 styling, margin geometry, and font metrics.
> * Structural checks against the 7 prompt criteria.
> * Document collation and build orchestration into terminal-viewable formats (`glow`) and final PDF.

---

## 4. Proposed Pipeline Architecture for the PIP

To adapt [`summaries/GEMINI.md`](file:///home/owen/ucf/so/s1/ENC/summaries/GEMINI.md) seamlessly for this project, we establish the following file and compilation organization:

### Workspace Staging in `projects/Professional_Infromation_Produc/`

```text
projects/Professional_Infromation_Produc/
├── prompt.txt                     # Official assignment brief
├── pipeline_evaluation.md         # This evaluation report (glow-optimized)
├── document.md                    # Deliverable 1: Final Product (Vim Guide)
├── rational.md                    # Deliverable 2: Rhetorical Rationale (750-1000 w)
├── prototype.md                   # Deliverable 3: Prototype version & feedback log
├── compile_pip_package.py         # Unified multi-part ReportLab compiler
└── final_pip_package.pdf          # Final composite 3-in-1 university submission
```

---

## 5. Rhetorical Rationale Alignment Matrix

The Rhetorical Rationale must span **750–1,000 words** and address 7 specific prompts. The table below outlines how Owen's established project topic aligns with the required readings:

| Rationale Section | Key Argument / Topic Focus | Theoretical Anchor & Citations |
| :--- | :--- | :--- |
| **1. Audience** | UCF CS students proficient in VS Code/CLion, novice to modal editing. | Porter: User workflow vs. static document focus; Wheeler. |
| **2. Purpose** | Eliminate mouse dependency; build foundational mental model of modal editing. | Porter: Conceptual framework / theory as heuristic. |
| **3. Genre** | Technical Quickstart / "How-To" Reference Card for VSCodeVim. | Henze: Stabilized-for-now genres; Gerdes: Utilitarian role. |
| **4. Content** | Scoped strictly to core navigation (`hjkl`, `wb`), modal switching, and basic edits. | Information Inventory & "So What?" test results. |
| **5. Organization** | Progressive disclosure: Concept -> Movement -> Editing -> File operations. | Lumen Learning: Inverted pyramid and reader-centricity. |
| **6. Design** | High-contrast tables, shortcut badges, chunked sections, visual anchor cues. | Melonçon et al. (RAWWr): Visual usability and cognitive load. |
| **7. Tone & Language** | Pragmatic, direct, technical without condescension or command-line friction. | Mizrahi: Workplace precision and audience expectations. |

---

## 6. Actionable Implementation Plan

1. **Update Citation Library:**
   Add Dr. Stephanie Wheeler's course materials to the citation index in [`summaries/GEMINI.md`](file:///home/owen/ucf/so/s1/ENC/summaries/GEMINI.md).
2. **Draft Markdown Sources in Terminal Format:**
   * Author [`document.md`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/document.md) using clean headings, scannable tables, and keystroke backticks.
   * Author [`rational.md`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/rational.md) targeting 750–1,000 words with in-text MLA 9 citations (`Porter`, `Henze`, `Wheeler`).
   * Author [`prototype.md`](file:///home/owen/ucf/so/s1/ENC/projects/Professional_Infromation_Produc/prototype.md) capturing the prototype draft and peer review revisions.
3. **Construct Composite Compiler (`compile_pip_package.py`):**
   * Section 1: Professional Information Product using custom styling (10.5pt/14pt leading, styled cheat-sheet tables).
   * Section 2: Page break transitioning into strict MLA 9 formatting (`leading=24`, double spaced, 0.5 in indents).
   * Section 3: Prototype artifact section.
   * Section 4: Standalone Works Cited page.
4. **Visual Verification & QA:**
   Execute `pdftoppm -png -r 150` on the compiled PDF to verify header placement (`Lopez [Page#]`), line geometry, and clean visual break points.
