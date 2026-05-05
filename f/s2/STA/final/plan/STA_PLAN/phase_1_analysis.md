# Phase 1: Sequential Analysis & Solving Directive (Expanded)

## 1. Objective
Perform an exhaustive, chronological analysis of `final/STA_2023_Final_Exam_Practice.pdf` to produce a high-fidelity mathematical solution set and a granular map of required knowledge. This document serves as the absolute "Source of Truth" for all subsequent phases.

## 2. Step 1: Meticulous Question Solving
- **Action:** Spawn a `generalist` sub-agent with high mathematical reasoning.
- **Instruction:** "Process `final/STA_2023_Final_Exam_Practice.pdf` page by page. For every question and sub-question (e.g., Question 1a, 1b, 2...), you must generate a solution using the following **Standard Solution Template**:"
    - **Given:** List every numerical value and variable provided in the prompt (e.g., $\mu = 50$, $\sigma = 5$, $n = 30$).
    - **Find:** State exactly what the question is asking for (e.g., "The probability that the sample mean is $> 55$").
    - **Formula Selection:** Identify and write the exact formula required (e.g., $Z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}$).
    - **Substitution:** Show the formula with the 'Given' values plugged in.
    - **Calculation:** Show the intermediate arithmetic steps.
    - **Rounding:** Strictly follow rounding instructions found on Page 1 of the practice test (e.g., "Round all probabilities to four decimal places").
    - **Final Answer:** Clearly bold the final result with appropriate units.
- **Output:** Write the results to `final/plan/STA_PLAN/intermediate/draft_answers.md`.

## 3. Step 2: Granular Topic & Skill Mapping
- **Action:** Extract a targeted list of conceptual dependencies.
- **Instruction:** "For every question solved in Step 1, create a mapping entry in the following format:"
    - **Question Number:** [e.g., Q4b]
    - **Primary Concept:** [e.g., Binomial Distribution]
    - **Specific Skill:** [e.g., Calculating 'at least' probabilities using the complement rule $1 - P(\text{none})$]
    - **Formula Needed:** [e.g., $P(X=k) = \binom{n}{k} p^k q^{n-k}$]
    - **Source Dependency:** [e.g., Chapter 5 notes / Z-Table]
- **Output:** Write a numbered, chronological list to `final/plan/STA_PLAN/intermediate/target_topics.md`.

## 4. Step 3: Rigorous Verification Round
- **Action:** Spawn a second `generalist` agent to act as a "Grader."
- **Instruction:** "Perform a 'Blind Recalculation' of 25% of the questions in `draft_answers.md`. Then, cross-check the entire document against the PDF. Verify:"
    - **Completeness:** Is every sub-question (a, b, c, d...) accounted for?
    - **Logic:** Does the formula choice align with the 'Find' statement?
    - **Precision:** Are the rounding rules applied correctly?
    - **OCR Check:** Ensure no numbers were misread from the PDF (e.g., reading a '5' as a '6').
- **Remediation:** Any error found triggers a full re-solve of that specific question.

## 5. Constraints
- **Ordering:** The output MUST maintain a 1:1 chronological mapping to the practice exam.
- **Notation:** Use standard LaTeX math notation in the Markdown (e.g., use `$ ... $` and `$$ ... $$`) to facilitate later conversion.
