# Phase 4: Bottom-Up Ocular Assessment Directive (Expanded)

## 1. Objective
Execute a rigorous visual audit of every individual LaTeX module. This phase eliminates common AI-generated document failures (uneven spacing, fragmented content, poor real-estate usage) before they can propagate into the final document.

## 2. Step 1: Isolated Rendering & Wrap-Around
- **Action:** For every `.tex` module in `isolated_tests/modules/`, wrap it in a temporary `standalone_wrap.tex` that includes the full `style_guide.tex` preamble.
- **Instruction:** "Run `tectonic standalone_wrap.tex` for each module."

## 3. Step 2: The "Human Designer" Checklist
- **Instruction to Ocular Review Agent:** "Inspect the rendered PDF of your specific module. You are validating based on these **Human-Designed Standards**:"
    - **Standard 1: Horizontal Balance.** Is all content (especially math and tables) properly centered or aligned to the margin? Look for "jagged" left-hand lines.
    - **Standard 2: Vertical Density.** Is there a massive void below the header? Is the term being defined squeezed against the box border?
    - **Standard 3: List Cohesion.** Do lists start on a fresh line? Is the indentation consistent with the paragraph text?
    - **Standard 4: Page Break Resistance.** Does any part of the question bleed onto a second page? If yes, it is a critical failure.
- **Output:** A pass/fail status for each module.

## 4. Step 3: Precise Remediation Commands
- **Action:** If a module fails, the agent must perform the following **Micro-Fixes**:
    - **Fix Crowding:** Add `\vspace{1em}` or `\medskip`.
    - **Fix Overflow:** Use `\allowbreak` or adjust the `minipage` width.
    - **Fix Gaps:** Add `\vfill` after the content block to force it to distribute.
    - **Fix Splits:** Enforce `needspace{X\baselineskip}` where X is the number of lines needed to keep the unit together.

## 5. Step 4: Final Certification
- **Action:** The agent must re-render the module. Once all Checklist Standards are met, the module is moved to a `final/plan/STA_PLAN/isolated_tests/certified/` directory.

## 6. Constraints
- **Focus:** No module is allowed to proceed to integration if it has even one visual artifact.
- **Tooling:** Use Tectonic for all verification builds.
