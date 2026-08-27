# ENC 3250 — Course Planning & Document Infrastructure Guide (`GEMINI.md`)

This document serves as the persistent architectural standard and style guide for all writing assignments and document generation tasks in **ENC 3250: Professional & Technical Writing** at the University of Central Florida (UCF).

---

## 1. Purpose of Course Assignments

The assignments in ENC 3250 train students to analyze and apply rhetorical and communication theories to technical and professional workplace scenarios. Key objectives include:

- **Theoretical Synthesis**: Summarizing complex readings on rhetorical theory, technical communication, usability, reader-centric writing, and professional ethics.
- **Evidence-Based Evaluation**: Supporting analytical claims by integrating direct quotations and paraphrased concepts using standard **MLA 9th Edition** conventions.
- **Critical Reflection**: Connecting theoretical heuristics (e.g., audience analysis, user-centered design, delivery systems) to practical workplace and dynamic organizational systems.
- **Professional Presentation**: Producing clean, university-grade documents that adhere strictly to academic formatting and professional writing standards.

---

## 2. Document Heading & Metadata Specifications

Every generated assignment document must include standard MLA 9 header information.

### Identification Block (Top-Left of First Page, Double-Spaced)
```text
Owen Lopez
Professor Faulconer
ENC 3250
[Day Month Year] (e.g., 27 August 2026)
```

### Student Information
- **Name**: Owen Lopez
- **NID**: `ow281867@ucf.edu`
- **UCF ID**: `5699462`
- **Instructor**: Professor Faulconer
- **Course**: ENC 3250 (Section 0064)

### Running Head (Top-Right of Every Page)
- Positioned **0.5 inches** (36 pt) from the top edge and flush with the **1.0-inch** right margin.
- Format: `Lopez [Page#]` (e.g., `Lopez 1`, `Lopez 2`, `Lopez 3`).
- Font: 12pt Times-Roman (matching body text).

---

## 3. Discrete Professional Style & Formatting Rules

All output PDFs must strictly follow **MLA 9th Edition** formatting:

| Element | MLA 9 Standard | ReportLab / Typesetting Parameter |
| :--- | :--- | :--- |
| **Paper Size** | Standard US Letter (`8.5" × 11"`) | `pagesizes.letter` (`612 × 792 pt`) |
| **Margins** | Exactly `1.0 inch` on all four sides | `leftMargin=72`, `rightMargin=72`, `topMargin=72`, `bottomMargin=72` |
| **Typography** | Times New Roman / Times-Roman, 12 pt | `fontName="Times-Roman"`, `fontSize=12` |
| **Line Spacing** | Exact double spacing throughout | `leading=24`, `spaceBefore=0`, `spaceAfter=0` |
| **Alignment** | Left-aligned (ragged right, not justified) | `alignment=TA_LEFT` |
| **Paragraph Indent** | First line indented `0.5 inches` | `firstLineIndent=36` (0.5 in) |
| **Document Title** | Centered, 12pt, standard capitalization | `alignment=TA_CENTER`, `firstLineIndent=0` |
| **Section Scope** | Only the `# Response` and Works Cited | Exclude assignment prompt instructions from output PDF |
| **Works Cited Page** | Standalone page at the end of the essay | `PageBreak()`, centered heading `Works Cited`, `0.5 in` hanging indent |

---

## 4. Master Course Bibliography & MLA 9 Citation Library

Below are verified, complete MLA 9 citations and in-text citation formats for all required course materials and resources in ENC 3250.

### 1. James E. Porter (Book Chapter)
- **Works Cited Entry**:
  ```text
  Porter, James E. "How Can Rhetoric Theory Inform the Practice of Technical Communication?" Solving Problems in Technical Communication, edited by Johndan Johnson-Eilola and Stuart A. Selber, University of Chicago Press, 2013, pp. 125–41.
  ```
- **In-Text Parenthetical**: `(Porter 128)` or `(128)` if author is named in the signal phrase.
- **Key Concepts**: Theory as conceptual framework / heuristic, rhetorical situation, audience usability, workflow vs. document focus.

---

### 2. Janet Mizrahi (Book)
- **Works Cited Entry**:
  ```text
  Mizrahi, Janet. Writing for the Workplace: Business Communication for Professionals. Business Expert Press, 2015.
  ```
- **In-Text Parenthetical**: `(Mizrahi)` or `(Mizrahi [page#])`.
- **Key Concepts**: Workplace communication essentials, professional genres, audience expectations, business writing clarity.

---

### 3. Lori Melonçon, Tanya Zarlengo, and J. Griffith (Open-Access Textbook / RAWWr)
- **Works Cited Entry**:
  ```text
  Melonçon, Lori, Tanya Zarlengo, and J. Griffith. RAWWr: A Rhetorical Approach to Workplace Writing. 10th ed., Write Professionally, 2023, writeprofessionally.org/tech-comm/files/2023/08/Ed10_RAWWr_full-version.pdf.
  ```
- **In-Text Parenthetical**: `(Melonçon et al. [page#])` or `(Melonçon et al.)`.
- **Key Concepts**: Rhetorical approach to workplace genres, situational awareness, ethics, document design, collaborative writing.

---

### 4. Lumen Learning / Open SUNY Textbooks (Course Module)
- **Works Cited Entry**:
  ```text
  "Rhetorical Nature of Technical and Professional Writing." Technical Writing, Lumen Learning / Open SUNY Textbooks, courses.lumenlearning.com/suny-professionalcommunication/chapter/rhetorical-nature-of-technical-and-professional-writing/.
  ```
- **In-Text Parenthetical**: `("Rhetorical Nature")`.
- **Key Concepts**: Reader-centric writing, legal status of workplace documents, inverted pyramid structure, usability, professional ethics.

---

### 5. Julie Gerdes (Writing Commons Online Article)
- **Works Cited Entry**:
  ```text
  Gerdes, Julie. "Professional and Technical Communication: An Overview." Writing Commons, writingcommons.org/article/professional-and-technical-communication-an-overview/.
  ```
- **In-Text Parenthetical**: `(Gerdes)`.
- **Key Concepts**: Distinctions among workplace, professional, business, and technical writing; communicative roles; ethics and context awareness.

---

## 5. Reusable PDF Compilation Engine (`ReportLab`)

Use this standard Python template to generate any future assignment PDF.

```python
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
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

def build_mla_document(output_pdf_path, title_text, date_str, paragraphs, works_cited_entries):
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

    mla_body = ParagraphStyle(
        'MLABody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=0,
        firstLineIndent=36  # 0.5 in indent
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
        leftIndent=36,       # Hanging indent
        firstLineIndent=-36
    )

    story = []

    # Student Identification Block
    heading_lines = [
        "Owen Lopez",
        "Professor Faulconer",
        "ENC 3250",
        date_str
    ]
    for line in heading_lines:
        story.append(Paragraph(line, mla_heading))

    # Paper Title
    story.append(Paragraph(title_text, mla_title))

    # Body Paragraphs
    for p in paragraphs:
        story.append(Paragraph(p, mla_body))

    # Standalone Works Cited Page
    story.append(PageBreak())
    story.append(Paragraph("Works Cited", mla_wc_head))
    for entry in works_cited_entries:
        story.append(Paragraph(entry, mla_wc_entry))

    doc.build(story, canvasmaker=MLACanvas)
    print(f"Generated: {output_pdf_path}")
```

---

## 6. Execution Workflow & Quality Assurance Checklist

For every upcoming assignment:

1. **Source Draft (`summary_X.md`)**:
   - Organize markdown files with `# Prompt`, `# Response`, and `## Works Cited` sections.
2. **Word Count & Evidence Check**:
   - Verify word count against the specific assignment prompt (e.g. 250–350 words).
   - Ensure all quotes and paraphrases have exact in-text MLA citations without informal "pg" abbreviations.
3. **PDF Generation**:
   - Compile using the Python ReportLab builder.
   - Ensure output is placed in the designated directory as `summary_X.pdf`.
4. **Visual Inspection**:
   - Render pages to PNG using `pdftoppm -png -r 150 <file>.pdf /tmp/page` and inspect with `view_file`.
   - Confirm margins (1-inch), running headers (`Lopez X`), line height (double-spaced), paragraph indents (0.5-inch), and clean hanging indents on the Works Cited page.
