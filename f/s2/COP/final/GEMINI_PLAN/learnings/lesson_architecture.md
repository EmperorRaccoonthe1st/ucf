# Lesson: Modular Architecture vs. Categorized Matrix

## 1. Modular Chapters (The CDA/COP Model)
**Core Concept:** Information is organized into linear, narrative chapters (e.g., "Linked Lists", "Sorting").
- **Strengths:**
    - **Narrative Flow:** Essential for concepts where logic builds sequentially (e.g., teaching recursion before trees).
    - **Logical Interdependency:** Keeps theory and implementation (C code) together, preventing "fragmentation."
    - **Orchestration Efficiency:** Directly maps to `\include{chapter}` in LaTeX, reducing the complexity of the final assembly.
- **When to Use:** Use for teaching **systems and algorithms** (CS1, Computer Architecture).

## 2. Categorized Matrix (The CHM Model)
**Core Concept:** Information is decoupled into discrete files like `topics.md`, `skills.md`, and `formulas.md`.
- **Strengths:**
    - **Reference Utility:** Creates a powerful "lookup" resource for procedural tasks (e.g., "How to balance this equation").
    - **Global Consistency:** Allows for batch-processing of all formulas or terms to ensure styling is identical throughout.
- **When to Use:** Use for **rule-heavy, procedural subjects** (Chemistry, Mathematics).

## 3. The Hybrid Recommendation for COP3502
For the CS1 study guide, a **hybrid approach** is optimal:
- **Base Structure:** Modular chapters (CDA/COP model) to maintain the "flow" of programming concepts.
- **Matrix Element:** A "Skills & Pitfalls" extraction phase (CHM model) to create specific "Cheat Sheet" summary boxes for each chapter (e.g., Big-O table for all sorts, common Segfault triggers for lists).
