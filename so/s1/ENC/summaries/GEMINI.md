# ENC 3250 — Course Planning & Document Infrastructure Guide (`GEMINI.md`)

This document serves as the persistent architectural standard, style guide, and technical blueprint for all writing assignments and document generation tasks in **ENC 3250: Professional & Technical Writing** at the University of Central Florida (UCF).

---

## 1. Course Context & Assignment Objectives

The assignments in ENC 3250 train students to analyze and apply rhetorical and communication theories to technical and professional workplace scenarios. Key objectives across all assignment types include:

- **Theoretical Synthesis**: Summarizing and evaluating complex readings on rhetorical theory, technical communication, usability, reader-centric writing, and professional ethics.
- **Evidence-Based Evaluation**: Grounding all analytical claims in textual evidence by integrating direct quotations and paraphrased concepts using standard **MLA 9th Edition** conventions.
- **Genre & Audience Analysis**: Investigating workplace document genres (e.g., Architecture Decision Records, SOPs, white papers, technical guides) to understand how conventions serve specific organizational audiences and purposes.
- **Professional Presentation**: Producing clean, publication-grade academic and technical documents formatted strictly to MLA 9 standards.

---

## 2. Directory Structure & Workspace Conventions

The course repository is structured into dedicated operational directories:

```text
/home/owen/ucf/so/s1/ENC/
├── assigments/
│   ├── draft/      # Source Markdown drafts, raw assets/screenshots, and compilation scripts
│   └── final/      # Compiled university-grade MLA 9 PDF documents (e.g., 1.pdf, genre_detective.pdf)
├── log/            # Reflective practice logs and compilation tools (e.g., bestworstpracticeslog.md/.pdf)
├── posts/          # Discussion board contributions and collaborative drafts
├── projects/       # Major course deliverables and Professional Information Products (PIPs)
├── summaries/      # Persistent course infrastructure guides and standards (GEMINI.md)
└── texts/          # Primary reading library and course PDFs (Henze, Porter, etc.)
```

### Document Storage & Terminal Viewer Rule
- Always maintain clean, readable Markdown source files directly in the active working directory for immediate viewing in terminal markdown viewers such as `glow`.
- All final compiled PDF deliverables must be placed into their designated output directories (e.g., `assigments/final/`, `log/`).

---

## 3. Assignment Typologies & Document Scopes

ENC 3250 coursework encompasses four primary assignment typologies:

### A. Reading Summaries & Theoretical Syntheses (e.g., `1.md`)
- **Structure**: `# Prompt`, `# Response`, and `## Works Cited`.
- **Target Length**: Typically 250–350 words (or as specified in the prompt).
- **Scope for PDF Output**: Exclude the assignment prompt; compile only the `# Response` and the standalone `Works Cited` page.

### B. Genre Analyses & Detective Reports (e.g., `genre_detective.md`)
- **Structure**: Multi-part comparative analysis addressing *Audience*, *Purpose*, *Content*, *Organization*, *Language & Tone*, *Design*, *Genre Conventions*, and *Conclusion*.
- **Visual Evidence**: Integration of cleaned figure screenshots, structural outlines, or tables labeled with MLA 9 figure captions (`Fig. 1. Description...`).
- **Scope for PDF Output**: Compiled essay response with embedded figures and standalone Works Cited page.

### C. Reflective Practice Logs (e.g., `log/bestworstpracticeslog.md`)
- **Structure**: Bold section headings (e.g., `Best Practices`, `Worst Practices`) detailing concrete rhetorical and grammatical self-evaluations.
- **Typography**: Uses bold section subheadings (`MLASection`) while maintaining MLA 9 double spacing and running heads.

### D. Professional Information Products (PIPs) & Workplace Documents
- **Structure**: Real-world technical documentation (e.g., ADRs, technical specifications, user manuals, project proposals).
- **Conventions**: Utilitarian tone, modular section headers, code snippets, diagrams, and reader-focused navigation.

---

## 4. Student Identification & MLA 9 Metadata

Every generated academic paper and assignment PDF must include standard MLA 9 identification details.

### Identification Block (Top-Left of First Page, Double-Spaced)
```text
Owen Lopez
Professor Faulconer
ENC 3250
[Day Month Year] (e.g., 3 September 2026)
```

### Student Information Record
- **Name**: Owen Lopez
- **NID**: `ow281867@ucf.edu`
- **UCF ID**: `5699462`
- **Instructor**: Professor Faulconer
- **Course**: ENC 3250 (Section 0064) — *Professional & Technical Writing*

### Running Head (Top-Right of Every Page)
- **Position**: Exactly **0.5 inches** (36 pt) from the top edge (`792 - 36 = 756 pt`) and flush with the **1.0-inch** right margin (`612 - 72 = 540 pt`).
- **Format**: `Lopez [Page#]` (e.g., `Lopez 1`, `Lopez 2`, `Lopez 3`).
- **Font**: 12pt Times-Roman (matching body text).

---

## 5. Discrete Professional Style & Formatting Rules

All output assignment PDFs must strictly adhere to **MLA 9th Edition** layout specifications:

| Element | MLA 9 Standard | ReportLab / Typesetting Parameter |
| :--- | :--- | :--- |
| **Paper Size** | Standard US Letter (`8.5" × 11"`) | `pagesizes.letter` (`612 × 792 pt`) |
| **Margins** | Exactly `1.0 inch` on all four sides | `leftMargin=72`, `rightMargin=72`, `topMargin=72`, `bottomMargin=72` |
| **Typography** | Times New Roman / Times-Roman, 12 pt | `fontName="Times-Roman"`, `fontSize=12` |
| **Line Spacing** | Exact double spacing throughout | `leading=24`, `spaceBefore=0`, `spaceAfter=0` |
| **Alignment** | Left-aligned (ragged right, not justified) | `alignment=TA_LEFT` |
| **Paragraph Indent** | First line indented `0.5 inches` | `firstLineIndent=36` (0.5 in) |
| **Document Title** | Centered, 12pt, standard capitalization | `alignment=TA_CENTER`, `firstLineIndent=0` |
| **Section Headings** | Bold, 12pt, left-aligned (when required) | `fontName="Times-Bold"`, `leading=24`, `firstLineIndent=0` |
| **Figures & Captions** | Centered image; 10pt caption below | `alignment=TA_CENTER`, `fontSize=10`, `leading=14` |
| **Section Scope** | Only `# Response` / Body & Works Cited | Exclude assignment prompt directions from output PDF |
| **Works Cited Page** | Standalone page at the end of the essay | `PageBreak()`, centered heading `Works Cited`, `0.5 in` hanging indent |

---

## 6. Figure, Table & Visual Media Guidelines

When technical or genre assignments require screenshots, diagrams, or tables:

1. **Image Pre-Processing**:
   - Crop stray border pixels, white borders, or background artifacts before rendering.
   - Maintain original aspect ratio and scale images to fit comfortably within the 6.5-inch printable width (typically width $\le$ 450 pt, height $\le$ 220 pt).
2. **Comparative Side-by-Side Displays**:
   - When presenting multiple related screenshots (e.g., comparing two ADR outlines), place them inside a two-column ReportLab `Table` with centered alignment.
3. **MLA 9 Figure Numbering & Captions**:
   - Place figures as close as possible to the referencing paragraph using `KeepTogether`.
   - Number sequentially: `Fig. 1.`, `Fig. 2.`, etc.
   - Caption format: `Fig. 1. Title or description of the figure ("Source Title" or Author Page).`
4. **Tables**:
   - Number sequentially: `Table 1`, `Table 2`, with a title above the table and source notes below if needed.

---

## 7. Master Course Bibliography & MLA 9 Citation Library

Verified MLA 9 citations and in-text parenthetical formats for core course materials and external technical genres:

### 1. James E. Porter (Book Chapter)
- **Works Cited Entry**:
  ```text
  Porter, James E. "How Can Rhetoric Theory Inform the Practice of Technical Communication?" Solving Problems in Technical Communication, edited by Johndan Johnson-Eilola and Stuart A. Selber, University of Chicago Press, 2013, pp. 125–41.
  ```
- **In-Text Parenthetical**: `(Porter 128)` or `(128)` if author is named in the signal phrase.
- **Key Concepts**: Theory as conceptual heuristic, rhetorical situation, audience usability, workflow vs. document focus.

---

### 2. Brent Henze (Book Chapter)
- **Works Cited Entry**:
  ```text
  Henze, Brent. "Genre and Technical Communication." Solving Problems in Technical Communication, edited by Johndan Johnson-Eilola and Stuart A. Selber, University of Chicago Press, 2013, pp. 45–66.
  ```
- **In-Text Parenthetical**: `(Henze 48)` or `(Henze)`.
- **Key Concepts**: Genre as social action, stabilized-for-now communication, conventions, dynamic workplace adaptation.

---

### 3. Janet Mizrahi (Book)
- **Works Cited Entry**:
  ```text
  Mizrahi, Janet. Writing for the Workplace: Business Communication for Professionals. Business Expert Press, 2015.
  ```
- **In-Text Parenthetical**: `(Mizrahi)` or `(Mizrahi [page#])`.
- **Key Concepts**: Workplace communication essentials, professional genres, audience expectations, business writing clarity.

---

### 4. Lori Melonçon, Tanya Zarlengo, and J. Griffith (Open-Access Textbook / RAWWr)
- **Works Cited Entry**:
  ```text
  Melonçon, Lori, Tanya Zarlengo, and J. Griffith. RAWWr: A Rhetorical Approach to Workplace Writing. 10th ed., Write Professionally, 2023, writeprofessionally.org/tech-comm/files/2023/08/Ed10_RAWWr_full-version.pdf.
  ```
- **In-Text Parenthetical**: `(Melonçon et al. [page#])` or `(Melonçon et al.)`.
- **Key Concepts**: Rhetorical approach to workplace genres, situational awareness, ethics, document design, collaborative writing.

---

### 5. Lumen Learning / Open SUNY Textbooks (Course Module)
- **Works Cited Entry**:
  ```text
  "Rhetorical Nature of Technical and Professional Writing." Technical Writing, Lumen Learning / Open SUNY Textbooks, courses.lumenlearning.com/suny-professionalcommunication/chapter/rhetorical-nature-of-technical-and-professional-writing/.
  ```
- **In-Text Parenthetical**: `("Rhetorical Nature")`.
- **Key Concepts**: Reader-centric writing, legal status of workplace documents, inverted pyramid structure, usability, professional ethics.

---

### 6. Julie Gerdes (Writing Commons Online Article)
- **Works Cited Entry**:
  ```text
  Gerdes, Julie. "Professional and Technical Communication: An Overview." Writing Commons, writingcommons.org/article/professional-and-technical-communication-an-overview/.
  ```
- **In-Text Parenthetical**: `(Gerdes)`.
- **Key Concepts**: Distinctions among workplace, professional, business, and technical writing; communicative roles; ethics and context awareness.

---

### 7. Online Technical Artifacts & Software Documentation Repositories
- **Works Cited Entries**:
  ```text
  "Architecture Decision Record: CSS Framework." Architecture Decision Record, GitHub, github.com/architecture-decision-record/architecture-decision-record/tree/main/locales/en/examples/css-framework.

  "Environment Variable Configuration." Architecture Decision Record, GitHub, github.com/architecture-decision-record/architecture-decision-record/tree/main/locales/en/examples/environment-variable-configuration.
  ```
- **In-Text Parentheticals**: `("Architecture Decision Record: CSS Framework")` and `("Environment Variable Configuration")`.
- **Key Concepts**: Architecture Decision Records (ADRs), technical governance, version-controlled documentation, rationale capture.

---

## 8. Reusable Universal PDF Compilation Engine (`ReportLab`)

This modular Python script serves as the standardized engine for compiling any ENC 3250 assignment into an MLA 9 PDF.

```python
#!/usr/bin/env python3
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Image, KeepTogether, Table, TableStyle
from reportlab.pdfgen import canvas

class MLACanvas(canvas.Canvas):
    """Two-pass canvas that dynamically stamps standard MLA running heads (Lopez <Page#>)"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header()
            super().showPage()
        super().save()

    def draw_header(self):
        self.saveState()
        self.setFont("Times-Roman", 12)
        # 0.5 in from top (792 - 36 = 756 pt), flush right with 1.0 in margin (612 - 72 = 540 pt)
        text = f"Lopez {self._pageNumber}"
        self.drawRightString(612 - 72, 792 - 36, text)
        self.restoreState()

def build_mla_document(output_pdf_path, title_text, date_str, elements_flowable, works_cited_entries=None):
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=72
    )

    styles = getSampleStyleSheet()

    mla_heading = ParagraphStyle(
        'MLAHeading',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=0,
        firstLineIndent=0
    )

    mla_title = ParagraphStyle(
        'MLATitle',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=24,
        alignment=TA_CENTER,
        spaceBefore=0,
        spaceAfter=0,
        firstLineIndent=0
    )

    mla_wc_head = ParagraphStyle(
        'MLAWorksCitedHead',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=24,
        alignment=TA_CENTER,
        spaceBefore=0,
        spaceAfter=0,
        firstLineIndent=0
    )

    mla_wc_entry = ParagraphStyle(
        'MLAWorksCitedEntry',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=0,
        leftIndent=36,       # 0.5 in hanging indent
        firstLineIndent=-36
    )

    story = []

    # 1. Identification Block
    heading_lines = [
        "Owen Lopez",
        "Professor Faulconer",
        "ENC 3250",
        date_str
    ]
    for line in heading_lines:
        story.append(Paragraph(line, mla_heading))

    # 2. Document Title
    story.append(Paragraph(title_text, mla_title))

    # 3. Main Document Elements (Paragraphs, Sections, Figures)
    for elem in elements_flowable:
        story.append(elem)

    # 4. Standalone Works Cited Page (if applicable)
    if works_cited_entries:
        story.append(PageBreak())
        story.append(Paragraph("Works Cited", mla_wc_head))
        for entry in works_cited_entries:
            story.append(Paragraph(entry, mla_wc_entry))

    doc.build(story, canvasmaker=MLACanvas)
    print(f"Successfully generated: {output_pdf_path}")
```

---

## 9. End-to-End Execution Workflow & Quality Assurance Checklist

Follow this procedure for every ENC 3250 assignment:

1. **Source Drafting (`<assignment_name>.md`)**:
   - Draft the content in Markdown with clear sections (`# Prompt`, `# Response`, `## Works Cited`).
   - Maintain the Markdown file in the active directory for terminal review (`glow`).
2. **Textual & Citation Integrity**:
   - Verify that claims are backed with textual evidence and accurate MLA 9 parenthetical citations.
   - Proofread for grammar, active voice, conciseness, subject-verb agreement, and correct terminology (e.g., *rationale*, *its* vs. *it's*, *affect* vs. *effect*).
3. **Visual Media & Figure Preparation**:
   - Clean/crop raw screenshots to remove UI noise or border artifacts.
   - Attach numbered MLA captions (`Fig. X. ...`) referencing the source.
4. **PDF Generation**:
   - Execute the ReportLab builder script to generate the output PDF in the designated `final/` folder.
5. **Visual Rasterization & QA Verification**:
   - Convert PDF pages to high-resolution PNGs:
     ```bash
     pdftoppm -png -r 150 <path_to_pdf>.pdf /tmp/page_review
     ```
   - Inspect all pages:
     - [ ] 1.0-inch margins on all four sides.
     - [ ] Running head `Lopez [Page#]` at 0.5 inches from top, flush right.
     - [ ] Strict double spacing (`leading=24`) with 0.5-inch paragraph indentation.
     - [ ] Proper figure integration with `KeepTogether` to prevent orphan captions.
     - [ ] Standalone Works Cited page with centered heading and clean hanging indents.
