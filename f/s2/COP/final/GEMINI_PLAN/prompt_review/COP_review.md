# Prompt Review: COP_GEMINI.md

## 1. Core Role and Objectives
- **Persona:** Lead Technical Author and Study Guide Designer specializing in Computer Science 1 (COP3502).
- **Primary Objective:** To synthesize a vast repository of course materials (lecture slides, practice problems, labs, and C code examples) into a high-quality, comprehensive, and succinct LaTeX study guide for UCF's COP3502 course.
- **Goal Alignment:** The prompt focuses on transforming raw academic data into a polished, pedagogically sound educational resource.

## 2. Context Management
- **Strategic Delegation:** Mandates the use of the `generalist` sub-agent for high-volume data processing (PDF extraction and summarization), preserving the orchestrator's context window for high-level strategy and verification.
- **Modular Processing:** Enforces a topic-by-topic breakdown (e.g., "AVL Trees", "Algorithm Analysis") to prevent context overflow and ensure depth for each subject area.
- **Intermediate State Management:** Utilizes Markdown (`.md`) as a bridge between raw source material and final LaTeX output, ensuring data is validated and structured before typesetting begins.

## 3. Document Formatting
- **Template Standard:** Strictly adheres to "The Legrand Orange Book" LaTeX template.
- **Custom Environments:** Specifies precise use of custom LaTeX environments to enhance readability and educational value:
    - `definition`, `theorem`, `proposition` for theory.
    - `example` for working through problems (essential for CS1 logic).
    - `exercise` and `vocabulary` for student engagement.
    - `remark` for "common pitfalls" (e.g., memory leaks, segfaults), which are critical for novice C programmers.
- **Modularity:** Requires a master `main.tex` with modular `\input` commands for chapter files, facilitating easier debugging and collaborative drafting.
- **Code Presentation:** Employs `minted` or `lstlisting` for high-quality C code snippets.

## 4. Source Material Handling
- **Grounding Strategy:** Demands strict grounding in provided documents and local code directories (`pa/`, `lab/`, `prac/`, `q/`).
- **Technical Fidelity:** Explicitly warns against losing technical nuances of complex algorithms (Heap operations, Quick Sort partitioning, Trie traversal) during the summarization process.
- **Code-Theory Bridge:** Requires the inclusion of relevant C code snippets alongside theoretical explanations to provide a complete learning experience.

## 5. Workflow Phases
1.  **Inventory & Planning:** Mapping topics and creating a `STUDY_GUIDE_PLAN.md`.
2.  **Sub-Agent Extraction:** Parallelized extraction of details from PDFs and C files into topic-specific Markdown summaries.
3.  **LaTeX Generation:** Converting validated summaries into styled LaTeX source code.
4.  **Local Compilation:** Automated rendering using the **Tectonic** engine for a streamlined build process.

## 6. Strengths and Weaknesses
### Strengths
- **Rigorous Structure:** The three-tier approach (Source -> MD Summary -> LaTeX) is extremely robust for maintaining accuracy.
- **Domain Specificity:** Custom environments like `remark` for memory leaks are confirmed high-value additions for C programming education.
- **Workflow Efficiency:** Tectonic integration simplifies the toolchain, allowing the agent to focus on content rather than build environment issues.
- **Modular Success:** Similar to CDA, the modular chapter approach ensures that complex logic (like AVL rotations) can be isolated and verified.

### Weaknesses
- **Summarization Risk:** High dependency on the `generalist` agent for subtle logic (e.g., Quick Sort partitioning) is a single point of failure without a dedicated verification agent.
- **Missing Remediation Protocol:** Unlike the CHM prompt, COP lacks an explicit remediation script or "Ocular Review" phase, which could lead to missed layout or code-formatting errors.
- **Asset Blind Spots:** The lack of a strategy for generating or sourcing figures for chapter headers is a recurring weakness across the "Legrand Orange" prompts.

## 7. Evidence-Backed Insights (Artifact Linkage)
- **Modularity as Quality Control:** Lessons from the CDA/CHM projects show that modularity is the most effective way to prevent "hallucination cascade" in large documents. Breaking the guide into chapters prevents the agent from losing the "thread" of complex C logic.
- **The Need for "Ocular" Verification:** Artifact reviews for CHM proved that semantic verification (Review Swarms) catches errors that technical grounding might miss. COP's prompt would benefit from an "Ocular Review" phase specifically for C code snippet correctness.
- **Integrated Narrative vs. Procedural Matrix:** Evidence suggests that COP's modular chapter approach (shared with CDA) will produce a better "learning flow" for programming concepts than the decoupled topic/skill matrix used in CHM.
