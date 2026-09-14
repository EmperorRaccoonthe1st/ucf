# gmcli Kit Architecture and Courseware Review: UCF BSC Block 1

This review examines the development history of `gmcli`, kit architecture standards, the current practice kits in [`kits/`](file:///home/owen/ucf/so/s1/BSC/block1/kits), and the course materials in [`documents/`](file:///home/owen/ucf/so/s1/BSC/block1/documents). It provides concrete recommendations and an expansion roadmap to optimize your study workflow.

---

## 1. Executive Summary

Based on a detailed review of your previous development session (`gmcli_development`, conversation `9cbe10f8-2e32-4315-97b6-bc47c64e5b9a`) and the source code in [`/home/owen/Projects/ai_projects/gmcli`](file:///home/owen/Projects/ai_projects/gmcli):

1. **`gmcli` Engine Capabilities**:
   - Supports both Multiple Choice (`mc`) and Text Input (`text`).
   - Text input supports `exact` and `contains` match modes, toggled in builder mode via `<ctrl-o>` (which persists across questions).
   - In-game question editing is available via `<ctrl-o>` during play.
   - Text evaluation features Damerau-Levenshtein typo tolerance, case-insensitivity, whitespace collapsing, and leading article stripping.
   - Structural sign preservation strictly matches chemical formulas containing signs (`-`, `=`, `>`, `+`) such as `-OH`, `>C=O`, and `-COOH`.
   - Kits support multiple alternative correct answers in `text` mode to allow synonyms, acronyms, or varied notation.

2. **Current State of Practice Kits**:
   - [`kits/chapter_4.json`](file:///home/owen/ucf/so/s1/BSC/block1/kits/chapter_4.json): Strong functional group and isomer drill kit (27 questions). Minor spelling typos and grammatical errors in prompt/answer strings should be corrected.
   - [`kits/exam_1.json`](file:///home/owen/ucf/so/s1/BSC/block1/kits/exam_1.json): Rapid prototype kit (11 questions) with questions spanning Chapters 1, 2, and 3. Needs expansion and unique answer IDs.
   - **Missing Coverage**: No dedicated kits currently exist for Chapter 1 (Scientific Method & Taxonomy), Chapter 2 (Atomic Structure & Chemical Bonds), or Chapter 3 (Water Properties & pH Calculations).

---

## 2. gmcli Kit Technical Specification

Every kit in `gmcli` is stored as a JSON object validated by [`run/script/loader.go`](file:///home/owen/Projects/ai_projects/gmcli/run/script/loader.go).

```text
┌─────────────────────────────────────────────────────────────┐
│                       Kit JSON Schema                       │
├─────────────────────────────────────────────────────────────┤
│ {                                                           │
│   "id": "unique-kit-slug",                                  │
│   "title": "Human Readable Title",                          │
│   "creator": "owen",                                        │
│   "questions": [                                            │
│     {                                                       │
│       "id": "q1",                                           │
│       "text": "Question prompt text",                       │
│       "type": "text" | "mc",                                │
│       "answers": [                                          │
│         {                                                   │
│           "id": "q1-a1",                                    │
│           "text": "Correct answer string",                  │
│           "correct": true,                                  │
│           "textType": "exact" | "contains"                  │
│         }                                                   │
│       ]                                                     │
│     }                                                       │
│   ]                                                         │
│ }                                                           │
└─────────────────────────────────────────────────────────────┘
```

### Best Practices for Kit Construction

* **Multiple Correct Answers for Text Input**:
  In [`run/script/eval.go`](file:///home/owen/Projects/ai_projects/gmcli/run/script/eval.go), `EvaluateTextAnswer` tests against every answer marked `"correct": true`. You can supply both full terms and shorthand:
  ```json
  "answers": [
    { "id": "q1-a1", "text": "Domain Kingdom Phylum Class Order Family Genus Species", "correct": true, "textType": "contains" },
    { "id": "q1-a2", "text": "dkpcofgs", "correct": true, "textType": "exact" }
  ]
  ```
* **Match Type Selection**:
  - Use `exact` for single-word commands, chemical structures (`-OH`, `>C=O`), specific values (`2 8 18`), or concise definitions.
  - Use `contains` for multi-word conceptual explanations or when user phrasing may vary (`more ordered`, `surface tension`).
* **Multiple Choice (`mc`) for Exam Simulation**:
  Course practice exams from UCF are predominantly multiple choice. Adding MC questions trains test recognition alongside fill-in recall.

---

## 3. Review of Existing Kits

### A. [`kits/chapter_4.json`](file:///home/owen/ucf/so/s1/BSC/block1/kits/chapter_4.json) (27 Questions)

* **Coverage**: Isomers (structural, cis, trans, enantiomer) and all 7 Functional Groups (hydroxyl, carbonyl, carboxyl, amino, sulfhydryl, phosphate, methyl).
* **Strengths**:
  - Leverages the strict sign matching engine for Lewis representations (`-OH`, `>C=O`, `-COOH`, `-NH2 NH3`, `-SH`, `-OPO3`, `-CH3`).
  - Systematically tests Lewis structure, polar vs nonpolar, and hydrophilic vs hydrophobic for each group.
* **Audit Findings & Needed Fixes**:
  - `q7`: Prompt typo: `"Hydryoxyl Polar/NonPolar"` -> `"Hydroxyl Polar/NonPolar"`.
  - `q9`: Prompt typo: `"Carbonyl Hydrophilic/Hyrophobic"` -> `"Carbonyl Hydrophilic/Hydrophobic"`.
  - `q14`: Answer typo: `"Hyrdrophilic"` -> `"Hydrophilic"`.
  - `q17`: Answer is `"-NH2 NH3"`. Adding an alternate answer for `"-NH2"` and `"-NH3+"` ensures players aren't forced to type both forms in one line.
  - `q23`: Answer is `"-OPO3"`. Adding alternate answer `"-OPO3^2-"` or `"-OPO4"` supports standard textbook conventions.
  - `q27`: Prompt grammar: `"Which element has Ketone's & Aldehyde's"` -> `"Which functional group forms Ketones and Aldehydes?"` (Carbonyl is a functional group, not an element).
  - Missing course concepts: ATP reaction mechanism, variation in carbon skeletons (length, branching, double bond position, rings), and hydrocarbons.

### B. [`kits/exam_1.json`](file:///home/owen/ucf/so/s1/BSC/block1/kits/exam_1.json) (11 Questions)

* **Coverage**: Broad sampling across early chapters.
  - Ch 1: Hypotheses (testable, null, alternative), taxonomy mnemonic.
  - Ch 2: Essential elements (CHON), electron shell capacities (2 8 18).
  - Ch 3: Ice density, cohesion, adhesion, hydrophilic/hydrophobic behavior.
* **Audit Findings & Needed Fixes**:
  - Reused IDs: Answers across different questions share identical IDs (e.g. `q6-a1` is used in `q4`, `q6`, and `q10`). While valid JSON, each answer should have a distinct identifier.
  - Strict capitalization: `q11` answer has `"Bonds w/nonpolar"` with capital B; normalized input handles this, but consistency improves readability.
  - Opportunity: Expand from an 11-question sample into a full cumulative review kit once chapter-specific kits are completed.

---

## 4. Course Material Alignment & Content Gap Analysis

Reviewing [`documents/Chapter_1_Study_Guide.pdf`](file:///home/owen/ucf/so/s1/BSC/block1/documents/Chapter_1_Study_Guide.pdf) and the four chapter practice problem PDFs reveals major syllabus topics that currently lack kit coverage:

```text
┌─────────────────────────────────────────────────────────────┐
│                 Block 1 Syllabus Coverage                   │
├─────────────┬─────────────────────────────────┬─────────────┤
│ Chapter     │ Key Curriculum Topics           │ Kit Status  │
├─────────────┼─────────────────────────────────┼─────────────┤
│ Chapter 1   │ - Taxonomic hierarchy (DKPCOFGS)│ Partial     │
│             │ - Relatedness at taxon levels   │ (in Exam 1) │
│             │ - Null vs Alternative hypotheses│             │
│             │ - Scientific theory criteria    │             │
│             │ - Graph & variable analysis     │             │
├─────────────┼─────────────────────────────────┼─────────────┤
│ Chapter 2   │ - Essential elements (CHON)     │ Missing     │
│             │ - Mass # vs Atomic #            │             │
│             │ - Isotopes & neutrons           │             │
│             │ - Electron shell energies       │             │
│             │ - Valence electrons vs Valence #│             │
│             │ - HONC 1234 bonding patterns    │             │
│             │ - Covalent vs Ionic (ions)      │             │
│             │ - Electronegativity & polarity  │             │
├─────────────┼─────────────────────────────────┼─────────────┤
│ Chapter 3   │ - 4 emergent properties of water│ Missing     │
│             │ - Hydrogen bonding dynamics     │             │
│             │ - Ice lattice & density         │             │
│             │ - Solvation (hydrophilic/phobic)│             │
│             │ - pH & pOH calculations         │             │
│             │ - [H+] and [OH-] concentrations │             │
│             │ - Acid vs Base definitions      │             │
├─────────────┼─────────────────────────────────┼─────────────┤
│ Chapter 4   │ - Carbon tetravalence           │ Covered     │
│             │ - Carbon skeleton variations    │ (Needs      │
│             │ - Structural, Cis-Trans, Enantio│  polish)    │
│             │ - 7 Functional groups & Lewis   │             │
│             │ - ATP structure and function    │             │
└─────────────┴─────────────────────────────────┴─────────────┘
```

---

## 5. Expansion Roadmap and Recommendations

To prepare comprehensively for Exam 1, the following modular plan is recommended:

### Phase 1: Polish Existing Kits
- Fix typos and clean IDs in [`kits/chapter_4.json`](file:///home/owen/ucf/so/s1/BSC/block1/kits/chapter_4.json).
- Add secondary alternate answers for chemical groups (`-NH2`, `-NH3+`, `-OPO3^2-`).

### Phase 2: Create Modular Chapter Kits
Generate dedicated kits directly in [`kits/`](file:///home/owen/ucf/so/s1/BSC/block1/kits) matching the practice questions and study guide:
1. `chapter_1.json`: Scientific method, hypotheses, taxonomy, and experimental reasoning.
2. `chapter_2.json`: Atomic structure, electron shells, isotopes, HONC 1234, and bond types.
3. `chapter_3.json`: Water chemistry, emergent properties, hydrogen bonds, and pH calculations.

### Phase 3: Comprehensive Exam Kit
- Assemble an expanded `exam_1.json` incorporating high-yield questions from all four chapters, mixing both `text` and `mc` question formats.
