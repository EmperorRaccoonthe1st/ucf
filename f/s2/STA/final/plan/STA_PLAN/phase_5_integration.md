# Phase 5: Master Integration & Final Global Review Directive (Expanded)

## 1. Objective
Synthesize the certified, "layout-perfected" modules into the final PDFs. This phase focuses on the global synergy of the document, ensuring that the transitions between perfected units are fluid and consistent.

## 2. Step 1: Sequential Assembly
- **Action:** Generate the master LaTeX source files (`Answer_Key.tex` and `Study_Guide.tex`) in the `final/plan/STA_PLAN/output/` directory.
- **Instruction:** "The assembly must be algorithmic. Use `\input{...}` commands in the precise order specified by the `master_outline.md` and the original practice exam structure."
- **Check:** Ensure the `style_guide.tex` preamble is correctly linked at the very top of both files.

## 3. Step 2: Global Environment Audit
- **Action:** Spawn a "Global Consistency Agent."
- **Instruction:** "Walk through the master `.tex` files. Perform these **Global System Checks**:"
    - **Numbering Synergy:** Does Question 2 follow Question 1 correctly? Ensure no duplicate section numbers exist.
    - **Header Continuity:** Ensure that section headers do not accidentally appear at the absolute bottom of a page (orphan headers). Use `\newpage` or `\needspace` globally to fix these rare occurrences.
    - **Index/TOC Check:** Ensure the Table of Contents (if required) correctly maps to the combined modules.
- **Output:** A finalized set of `.tex` source code.

## 4. Step 3: The "Final Rendering" Quality Gate
- **Action:** Run `tectonic Answer_Key.tex` and `tectonic Study_Guide.tex`.
- **Quality Criteria:** 
    - 0.0pt overfull `\hbox` (no text bleeding into margins).
    - No split mathematical environments.
    - No split tables.
    - All diagrams/figures (if any) are correctly anchored and captioned.

## 5. Step 4: Final Ocular Pass (Multi-Stage Professional Audit)
This is the most critical quality-control gate. The agent must adopt the persona of a **Senior Graphic Designer and Lead Typesetter**. The goal is to move the document from "AI-Generated" to "Published Manual" quality.

### Stage A: Page-by-Page Visual Rhythm Check
- **Instruction:** "Inspect the document at 100% zoom. Evaluate the **Visual Rhythm** of every page transition."
- **Audit Criteria:** 
    - **Consistent Padding:** Check the vertical space between section headers and the first paragraph. It must be identical throughout.
    - **List Cohesion:** Ensure no bulleted list is 'split' where the bullet starts on one page and the text continues on another. 
    - **Margin Discipline:** Scan the right-hand margin. If any math equation or table header is even 1pt over the margin, mark for remediation.

### Stage B: Structural Integrity & "Ghost Gaps"
- **Instruction:** "Identify and eliminate 'Ghost Gaps' (massive white spaces that serve no purpose)."
- **Remediation Protocol:** 
    - If a page has more than 15% empty space at the bottom, the agent must check if a `minipage` from the *next* page can be moved up.
    - Use `\enlargethispage{\baselineskip}` if a single line is being pushed to a new page.
    - Adjust `\vspace{\fill}` values to ensure that if a page *must* be short, the content is centered vertically rather than squashed at the top.

### Stage C: The "Math Stress-Test"
- **Instruction:** "Perform a surgical review of all equations and variables."
- **Audit Criteria:**
    - **Font Consistency:** Ensure all variables (e.g., $n, p, \sigma$) are consistently in math mode. 
    - **Display Math Balance:** Ensure multi-line equations (aligned by `=`) are not 'hugged' by text above or below. Add `\medskip` if necessary.
    - **Box Symmetry:** Ensure every `tcolorbox` (formula box) has identical internal margins and border weights.

### Stage D: Final Human-Grade Verification
- **Goal:** "Does this look like it was created by a UCF Professor?"
- **Final Check:** Verify the header and footer alignment on every page. Ensure the "Page X of Y" (if used) is correct. Check for any 'LaTeX Artifacts' like literal `_` or `&` characters that were not escaped correctly.

## 6. Step 5: Final Packaging
- **Action:** Move the final `.pdf` artifacts to the root `STA/` directory (or specified final destination) and delete all temporary `.aux` or log files if any were generated.
