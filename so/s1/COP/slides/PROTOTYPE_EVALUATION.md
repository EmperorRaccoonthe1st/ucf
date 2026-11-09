# COP 3330: Slide Format Prototypes - Evaluation Dossier

**Deliverable PDF:** [PROTOTYPE_SLIDES.pdf](file:///home/owen/ucf/so/s1/COP/slides/PROTOTYPE_SLIDES.pdf)  
**Generation Script:** [generate_prototypes.py](file:///home/owen/ucf/so/s1/COP/slides/generate_prototypes.py)  
**Target Viewer:** Viewable in terminal via `glow PROTOTYPE_EVALUATION.md` or via PDF viewer `xdg-open PROTOTYPE_SLIDES.pdf`  

---

## Executive Summary

Based on your feedback, the presentation architecture has been adjusted to eliminate superfluous desktop chrome, borders, and AI summaries. The format engine now operates under three rules:

1. **Standalone Slides (Format 1):**
   * Slides featuring pure text, conceptual diagrams, or single-line code snippets use the entire page and maximize screen coverage.
   * No alterations are made to the slide content.
   * Slides rest on a dark neutral surface background (`#12131a`).

2. **In-Slide Code Snippet Injection (Format 2):**
   * Multi-line unformatted code boxes are replaced directly in-place on the slide with Dracula dark-mode syntax-highlighted containers.
   * Surrounding slide content (bullet points, explanation text, error callouts, and terminal output boxes) remains untouched.
   * Supports single-box, mixed text/output, and multi-box slides.

3. **Adjacent Format (Format 3):**
   * Reserved strictly for situations where an external code file outside the PDF must be integrated (e.g., `FileTester.java`, `Room.java` suite, `COP3330_linked_list_notes.pdf`).
   * Slide describing the concept on the left, syntax-highlighted source code on the right, both resting on a dark surface background.

---

## Prototype Verification Table

| Prototype ID | Format Type | Source Material | Image Deliverable |
| --- | --- | --- | --- |
| Prototype 1 | Standalone Text (Full Page) | `Slide03_JavaBasics2.pdf` (Page 19) | [proto_1_standalone_text.png](file:///home/owen/ucf/so/s1/COP/slides/proto_1_standalone_text.png) |
| Prototype 2 | Single Code Injection | `bufferProblem.pdf` (Page 3) | [proto_2_single_injection.png](file:///home/owen/ucf/so/s1/COP/slides/proto_2_single_injection.png) |
| Prototype 3 | Mixed Code & Output Injection | `Slide03_JavaBasics2.pdf` (Page 20) | [proto_3_mixed_injection.png](file:///home/owen/ucf/so/s1/COP/slides/proto_3_mixed_injection.png) |
| Prototype 4 | Multi-Box Code Injection | `Slide12_InheritancePart1.pdf` (Page 4) | [proto_4_multi_injection.png](file:///home/owen/ucf/so/s1/COP/slides/proto_4_multi_injection.png) |
| Prototype 5 | Adjacent External Integration | `Slide16` + `FileTester.java` | [proto_5_adjacent_format.png](file:///home/owen/ucf/so/s1/COP/slides/proto_5_adjacent_format.png) |

---

## Detailed Specifications

### Prototype 1: Standalone Text Slide
* **Slide:** "Typecasting"
* **Characteristics:** Pure text with bullet points explaining implicit vs explicit casting.
* **Rendering:** Maximized to fill 96% of the screen dimensions. No injected boxes, no artificial borders, no summaries.

### Prototype 2: Single Code Box Injection
* **Slide:** "Full code of the problem case"
* **Characteristics:** Contains a single large code box on the left, and explanation on the right ("The test.java is inside testjava package. Scanner is imported.").
* **Rendering:** The code box is cleanly overlaid with a dark Dracula-themed container (`#282a36`), JetBrains Mono typography, and accurate syntax highlighting. The right-hand text is preserved.

### Prototype 3: Mixed Code & Warning/Output Box Injection
* **Slide:** "Typecasting examples"
* **Characteristics:** Contains a Java code snippet on the left, accompanied by warning text, two black terminal output boxes ("5 / 5.0", "3 / 3.2"), and a compiler error box on the right.
* **Rendering:** Only the multi-line Java code box is replaced. All terminal output boxes and compiler messages on the right remain in their original positions.

### Prototype 4: Multi-Box Code Injection
* **Slide:** "Inheritance example"
* **Characteristics:** Contains four distinct code boxes (`Car extends Vehicle`, `Vehicle`, `vehiclesTester`, and `go()` override).
* **Rendering:** All four boxes are individually replaced with Dracula dark-mode syntax-highlighted containers tailored to their respective bounding dimensions.

### Prototype 5: Adjacent Format (External Integration)
* **Slide & Code:** Slide 16 Page 6 (Writing to a file) + `FileTester.java` (external demo from zip).
* **Characteristics:** The slide explains the file stream concept; the external source file demonstrates the full implementation.
* **Rendering:** Slide on the left, full syntax-highlighted source code on the right with line numbers, resting on a dark surface background.

---

## Verification Commands

To view the generated 5-page prototype PDF:
```bash
xdg-open PROTOTYPE_SLIDES.pdf
```

To view individual prototype slide images:
```bash
xdg-open proto_1_standalone_text.png
xdg-open proto_2_single_injection.png
xdg-open proto_3_mixed_injection.png
xdg-open proto_4_multi_injection.png
xdg-open proto_5_adjacent_format.png
```
