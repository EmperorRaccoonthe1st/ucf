# Lesson: Verification, Ocular Reviews, and Remediation

## 1. The Verification Gap
The CDA project proved that **grounding is not enough.** Even if agents are told to use source materials, layout collisions (overlapping boxes) and "laddering" (text overflows) will occur in complex LaTeX documents.

## 2. Ocular Review Swarms (The CHM Breakthrough)
- **Concept:** Spawning subagents specifically to "look" at the rendered structure (semantic review) rather than just the code logic.
- **Implementation:** Instructing agents to check for margin overflows, font consistency, and "visual hierarchy" (e.g., are headers distinct from subheaders?).
- **Outcome:** Catches "invisible" errors that technical extraction misses.

## 3. Programmatic Remediation
- **The Python "Fixer":** CHM utilized a Python script (`fix_latex_comprehensive.py`) to enforce global rules across multiple files.
- **Benefit:** Programmatic enforcement is **idempotent and 100% consistent**, whereas asking 10 different subagents to "fix their files" introduces variability.
- **Recommendation:** Always include a step for a "Global Remediation Script" or a single "Remediation Agent" that has the final say on styling and formatting.

## 4. Failure Mode: The "Don't Care" Error
CDA lacked an explicit remediation protocol, leading to "good enough" artifacts that still had minor layout friction. COP must include a **Phase 3: Final Polish** specifically modeled after CHM's remediation swarm.
