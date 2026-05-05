# Phase 2: Surgical Extraction Directive (Expanded)

## 1. Objective
Surgically extract theoretical content (definitions, formulas, rules) from the `documents/` directory. The goal is to build a "lean" knowledge base where every entry has a direct utility to the practice final exam.

## 2. Step 1: Automated & Manual Search Protocol
- **Action:** Spawn a `generalist` sub-agent.
- **Instruction:** "Using the `target_topics.md` as your keyword list, perform the following search operations:"
    - **Grepping:** Run `grep_search` on the `documents/` directory to identify every file and page where a target topic is discussed.
    - **Contextual Reading:** Use `read_file` on identified ranges to extract the full context.
    - **Prioritization:** If a concept is found in both the `.docx` notes and the `.pdf` notes, prioritize the version that provides the most clear **Step-by-Step Procedure** or "Calculator Hint."
- **Output:** A raw log of extracted snippets categorized by target topic.

## 3. Step 2: Content Refinement & Filtering
- **Action:** Refine the raw snippets into "Study Guide Modules."
- **Instruction:** "For every target topic, generate a content block following this **Study Module Format**:"
    - **Target ID:** [e.g., Maps to Practice Exam Q3]
    - **Concept Name:** [e.g., Hypothesis Testing for Proportions]
    - **Core Definition:** A 1-2 sentence standard UCF definition.
    - **The Formula:** The exact formula as it appears in the instructor's notes.
    - **Requirements/Assumptions:** (e.g., "$np \geq 10$ and $n(1-p) \geq 10$").
    - **Calculator Steps:** Explicit buttons to press on a TI-83/84 (if present in source).
- **Constraint:** "AGGRESSIVE FILTERING: If a chapter in the source notes contains peripheral topics (e.g., 'Historical Context of Stats'), IGNORE THEM. Only include what is strictly necessary to solve the practice exam."

## 4. Step 3: Sequential Assembly
- **Action:** Combine all Study Modules into `final/plan/STA_PLAN/intermediate/study_content.md`.
- **Instruction:** "Maintain the chronological order of the exam. If the exam moves from 'Probability' to 'Normal Distribution' and back to 'Probability', the study guide should follow that same path to ensure the user's focus remains aligned with the test flow."

## 5. Step 4: Verification of Scope
- **Action:** Spawn a verification agent to audit the `study_content.md`.
- **Audit Criteria:** 
    - Is there any content here that *cannot* be used to solve a question on the practice test? (If yes, delete it).
    - Is there any question on the practice test that *cannot* be solved using ONLY the content in this guide? (If yes, return to Step 1).
- **Remediation:** Adjust content until the guide is 100% matched to the exam.
