# Lesson: Technical Extraction & Context Preservation

## 1. Preserving Logical Interdependency
When extracting CS1 algorithms (e.g., AVL rotations), the logic must be extracted as a **unit.**
- **Failure:** Extracting the "rotation rules" to a skill file and the "AVL definition" to a topic file can cause the agent to lose the implementation context.
- **Fix:** Instruct extraction agents to "Extract the concept, the algorithm, and the C implementation as a single coherent block."

## 2. Context Stewardship (The "Rule of Explicitness")
- **Mandate:** Never assume a subagent knows the "Master Plan."
- **Technique:** Every subagent prompt MUST include the specific formatting rules (from `style.md`) and the section constraints (from `plan.md`).
- **Intermediate State:** The Markdown (`.md`) file is the only reliable "long-term memory" for a project of this scale.

## 3. High-Fidelity Extraction (Code vs. Theory)
- **Rule:** For CS1, code *is* the theory. 
- **Action:** Extraction agents must prioritize **tracing code snippets** (e.g., step-by-step stack frame changes in recursion) over high-level narrative descriptions.
- **Grounding:** Use `read_file` on specific line ranges of lab/PA code to ensure the study guide uses the *user's* actual coding style where appropriate.
