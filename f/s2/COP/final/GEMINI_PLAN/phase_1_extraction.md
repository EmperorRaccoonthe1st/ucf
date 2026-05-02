# Phase 1: Knowledge Extraction Directive

## 1. Objective
Extract all relevant technical knowledge, algorithmic logic, and code implementations from the `documents/` and code directories into modular Markdown summaries.

## 2. Step 1: Inventory & Assignment
- **Orchestrator Action:** Map all files in `documents/` to specific topics (e.g., "17 AVL Trees.pdf" -> Topic: AVL Trees).
- **Orchestrator Action:** Assign each topic to a `generalist` subagent.

## 3. Step 2: Swarm Extraction
For each assigned topic, the subagent must:
1.  **Read:** The relevant PDF(s) and any corresponding C files in `pa/`, `lab/`, or `prac/`.
2.  **Extract:**
    - **Theoretical Core:** Definitions and mathematical properties (Big-O).
    - **Algorithmic Tracing:** Step-by-step logic for operations (e.g., "Inserting 15 into a Min-Heap").
    - **Code Implementation:** A polished C snippet demonstrating the core logic.
    - **Skills & Pitfalls:** A list of "Common Mistakes" and "Must-Know Skills".
3.  **Write:** The result to `GEMINI/intermediate/summaries/topic_name.md`.

## 4. Step 3: Verification Round (Coverage)
- **Agent:** "Coverage Verifier".
- **Instruction:** "Compare the list of generated `.md` files against the Foundation Exam syllabus and the `documents/` folder. Identify any missing concepts (e.g., Tries, Bitwise operations)."
- **Remediation:** Spawn additional extraction agents for any gaps found.

## 5. Constraints
- **Grounding:** All content MUST be grounded in local files.
- **Context Preservation:** Do not read more than 3 PDFs in a single subagent turn.
