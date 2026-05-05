# Intermediate Investigation Report: CDA vs. CHM

## 1. Structural Comparison & Technical Depth
| Feature | CDA (Modular Chapters) | CHM (Categorized Matrix) |
| :--- | :--- | :--- |
| **Organization** | Integrated narrative (Concept + Logic + Flow) | Procedural split (Topics vs. Skills vs. Formulas) |
| **Technical Depth** | High conceptual depth; explains *mechanisms* | High procedural depth; defines *algorithms* |
| **Ease of Reading** | Better for understanding a system | Better for quick reference/lookup |

**Finding:** CDA's structure produced a more cohesive technical narrative. The Datapath summary (Chapter 8) successfully linked control signals to hardware state, which is harder to achieve when skills and topics are decoupled as in CHM.

## 2. Handling Complex Logic & Data
### CDA: MIPS Datapath
- **Method:** Utilized dense truth tables and instruction-specific data flow descriptions.
- **Success:** Successfully captured the nuances of single-cycle timing and the "don't care" conditions in control logic.
- **Inferred Prompting:** Focused on "How does this instruction move through the hardware?"

### CHM: Chemical Formulas & Rules
- **Method:** Rule-based distillation and LaTeX-math extraction.
- **Success:** Captured precise mathematical relationships and "If-Then" solubility rules.
- **Inferred Prompting:** Focused on "What are the rules, and what are the steps to apply them?"

**Finding:** CDA handled **logical interdependencies** better (e.g., how the opcode determines the ALUOp), while CHM handled **symbolic data** (formulas/nomenclature) with higher precision.

## 3. Facilitation of LaTeX Generation
- **Modular (CDA):** Directly maps to a `\include{chapter}` workflow. Reduced the complexity of the "Final Orchestrator" turn as each module was pre-structured for its final location.
- **Unified (CHM):** Required a "Planning" phase (`plan.md`) to re-assemble the fragments. While more complex to assemble, it allowed for better global styling (e.g., all formulas could be extracted from one source to ensure consistent LaTeX formatting).

## 4. Final Conclusion
- **Use CDA's Structure** when the goal is to explain a **complex system** where the parts cannot be easily understood in isolation.
- **Use CHM's Structure** when the goal is to create a **high-utility reference** where the user needs to find specific "tools" (formulas) or "manuals" (skills) quickly.
