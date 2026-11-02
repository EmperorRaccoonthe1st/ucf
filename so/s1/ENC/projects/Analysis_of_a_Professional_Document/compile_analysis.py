#!/usr/bin/env python3
"""
compile_analysis.py
Compiles draft.md into an MLA 9th Edition formatted PDF (analysis.pdf).

Conforms strictly to MLA 9 guidelines and ENC 3250 infrastructure (summaries/GEMINI.md):
- Paper size: US Letter (8.5" x 11")
- Margins: 1.0 inch (72 pt) on all four sides
- Typography: Times-Roman, 12 pt
- Line spacing: Exact double spacing throughout (leading=24 pt)
- Paragraph indent: 0.5 inches (36 pt)
- Running head: Lopez [Page#] at 0.5 inches (36 pt) from top, flush with 1.0 in right margin
- Student identification block: top-left on first page (double-spaced)
- Centered title: 12 pt, unbolded, double-spaced
- Standalone Works Cited page: centered heading, 0.5 in hanging indent
"""

import os
import sys
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, PageBreak, Image, KeepTogether, Spacer, Table, TableStyle
)
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

def md_inline_mla(text):
    """Converts inline markdown formatting (_italic_, **bold**) and XML entities to ReportLab tags."""
    # Escape & if not already an entity
    text = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    text = re.sub(r'(?<!_)_([^_]+)_(?!_)', r'<i>\1</i>', text)
    return text

def build_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_pdf_path = os.path.join(base_dir, "analysis.pdf")

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

    mla_caption = ParagraphStyle(
        'MLACaption',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        spaceBefore=4,
        spaceAfter=14,
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
        "25 October 2026"
    ]
    for line in heading_lines:
        story.append(Paragraph(line, mla_heading))

    # 2. Paper Title
    title_text = "Rhetorical Analysis of a Rust RFC within a Collaborative Community"
    story.append(Paragraph(title_text, mla_title))

    # 3. Paragraph 1 (Introduction)
    p1 = (
        "Within the field of software development, design documents are utilized to coordinate complex "
        "projects and preserve technical decisions across an organization. The Request for Comments, or "
        "RFC, is a long-standing proposal format used to establish technical standards. As Dr. Julian Edwards "
        "explains in his history of early networking protocols, \"RFC number one was by Steve Crocker who was "
        "one of the very early movers in the internet\" (Edwards). The document being analyzed is "
        "\"pattern-binding-modes\" from <i>The Rust RFC Book</i>, which records an architectural decision "
        "made during the ongoing development of the Rust programming language. The document was utilized by "
        "the open source community that develops Rust alongside the Rust Foundation, which serves as \"an "
        "independent nonprofit committed to a safe, secure, and sustainable future powered by the Rust "
        "programming language\" (\"About the Rust Foundation\"). It represents a specialized design document "
        "that guides the architecture of a modern programming language. RFCs are compact technical documents "
        "that encapsulate an architectural choice, function as a collective decision making tool within an "
        "organization, and actively invite their audience to provide feedback."
    )
    story.append(Paragraph(p1, mla_body))

    # 4. Paragraph 2 (Purpose)
    p2 = (
        "The primary purpose of \"pattern-binding-modes\" is to detail a singular decision and present it to the "
        "organization for review. The authors wanted to improve the ease of use of a specific feature in the "
        "language, essentially allowing developers to better match patterns in code. To justify this change, "
        "the document reviews current issues with the system, noting that \"Currently, matching on references "
        "requires a bit of a dance using ref and &amp; patterns:\" (\"pattern-binding-modes\"). By capturing "
        "the origins behind the decision, the text demonstrates why the existing syntax is inefficient. "
        "Additionally, the document preserves the decision for the future. This ensures that future developers "
        "can look back at the record and understand both how and why the decision was made."
    )
    story.append(Paragraph(p2, mla_body))

    # 5. Paragraph 3 (Audience)
    p3 = (
        "An RFC can be viewed by anyone within an organization, but readers are expected to be mostly familiar "
        "with the project and the technology utilized within it. In this environment, each member acts as an "
        "active reviewer of the proposed change. Specifically, \"pattern-binding-modes\" was written for the "
        "designers of the Rust language, proposing a modification for review by those who manage the specific "
        "semantics of the language. Different members of the audience view the document for distinct reasons. "
        "Direct technical coworkers evaluate the proposal because syntax adjustments directly affect their daily "
        "work, while managers review the change to ensure the project remains on schedule. Additionally, "
        "domain-specific staff inspect the document for specialized issues like security, and future maintainers "
        "rely on the text to understand the exigence behind past decisions."
    )
    story.append(Paragraph(p3, mla_body))

    # 6. Paragraph 4 (Structure & Macro-organization)
    p4 = (
        "RFCs are organized into brief, focused sections that allow each reader to navigate the document based "
        "on their specific needs. As seen in the document's outline, \"pattern-binding-modes\" is divided into "
        "distinct sections: Summary, Motivation, Detailed Design, How We Teach This, Drawbacks, Alternatives, and "
        "Unresolved Questions (see fig. 1). This structure allows different members of the audience to interact "
        "with the text efficiently. Readers who are less involved in compiler development do not need the granular "
        "mechanics in the \"Detailed Design\" section, and can instead focus on high-level changes. The document is "
        "structured to introduce the decision first, build technical detail, and then open the topic for "
        "collaborative development once the core idea has been established."
    )
    story.append(Paragraph(p4, mla_body))

    # Figure 1: Sections Outline (src/sections.png)
    img1_path = os.path.join(base_dir, "src", "sections.png")
    if os.path.exists(img1_path):
        from PIL import Image as PILImage
        with PILImage.open(img1_path) as im1_pil:
            orig_w1, orig_h1 = im1_pil.size
        w1 = 100
        h1 = w1 * (orig_h1 / orig_w1)
        im1 = Image(img1_path, width=w1, height=h1)
        im1.hAlign = 'CENTER'
        fig1_elements = [
            Spacer(1, 2),
            im1,
            Paragraph("<i>Fig. 1</i>. Structural section outline of RFC 2005 (\"Pattern-Binding Modes\").", mla_caption),
            Spacer(1, 2)
        ]
        story.append(KeepTogether(fig1_elements))

    # 7. Paragraph 5 (Micro-Structure, Code Example & Discussion Sections)
    p5 = (
        "A quick overview of the decision begins the document, allowing the audience to immediately understand "
        "the proposal through an example of the change utilized in code (see fig. 2). Following this summary, "
        "the text details the exigence behind the decision by highlighting issues within the current system and "
        "explaining how they affect developers. The authors focus specifically on the friction experienced by newer "
        "programmers, noting that \"using match expressions and borrowed data together can be frustrating: "
        "getting the correct combination of *, &amp;, and ref to satisfy the type and borrow checkers is a "
        "common problem\" (\"pattern-binding-modes\"). After the technical design section, the document provides "
        "multiple sections that encourage discussion regarding how the change should be implemented. Segments "
        "such as \"How We Teach This\" outline how to educate newcomers on the new feature, while the \"Drawbacks\" "
        "section explicitly identifies potential complications and trade-offs."
    )
    story.append(Paragraph(p5, mla_body))

    # Figure 2: Summary Code Example (src/summary_example.png)
    img2_path = os.path.join(base_dir, "src", "summary_example.png")
    if os.path.exists(img2_path):
        from PIL import Image as PILImage
        with PILImage.open(img2_path) as im2_pil:
            orig_w2, orig_h2 = im2_pil.size
        w2 = 225
        h2 = w2 * (orig_h2 / orig_w2)
        im2 = Image(img2_path, width=w2, height=h2)
        im2.hAlign = 'CENTER'
        fig2_elements = [
            Spacer(1, 2),
            im2,
            Paragraph(
                "<i>Fig. 2</i>. Code example from \"Pattern-Binding Modes\" contrasting existing syntax with proposed match ergonomics.",
                mla_caption
            ),
            Spacer(1, 2)
        ]
        story.append(KeepTogether(fig2_elements))

    # 8. Paragraph 6 (Communication & Community Collaboration)
    p6 = (
        "RFCs are fundamentally designed to encourage communication throughout an organization. Rather than "
        "presenting a finalized mandate, sections covering alternatives and drawbacks allow the audience to "
        "interact directly with the proposal and debate potential complications. In \"pattern-binding-modes,\" "
        "the authors explicitly highlight that the change \"complicates the pattern-matching logic,\" "
        "acknowledging the architectural consequences while detailing why the trade-off is worthwhile "
        "(\"pattern-binding-modes\"). This format enables group coordination within online forums, which is "
        "necessary for large open-source communities, technology corporations, and standards bodies. Because "
        "the Rust language group is distributed globally and primarily communicates online—only gathering in "
        "person at special events such as \"RustConf\"—RFCs are essential to their collaborative design process "
        "(Matsakis). A proposal initiates discussions that build over time through layers of comments and responses "
        "from interested contributors. After extensive deliberation and revision, the change is finalized, "
        "preserving the entire collaborative decision for future use."
    )
    story.append(Paragraph(p6, mla_body))

    # 9. Paragraph 7 (Conclusion & Evaluation)
    p7 = (
        "Overall, RFCs serve as effective tools for guiding technical discourse and establishing consensus "
        "within software organizations. By centralizing, preserving, and formalizing the decision-making process, "
        "the genre provides a structured framework that accommodates participants from many different areas of a "
        "project. The modular format remains accessible to all interested parties, allowing contributors to "
        "review high-level motivations or inspect granular mechanics where their expertise is most relevant. An "
        "RFC initiates a discussion over an actionable change, providing a clear beginning and conclusion that "
        "results in decisive action from the organization. Ultimately, documents like \"pattern-binding-modes\" "
        "advance project goals in an orderly manner, fostering cohesion and equitable discussion for the benefit "
        "of the entire community."
    )
    story.append(Paragraph(p7, mla_body))

    # 10. Standalone Works Cited Page
    story.append(PageBreak())
    story.append(Paragraph("Works Cited", mla_wc_head))

    works_cited = [
        "\"About the Rust Foundation.\" <i>Rust Foundation</i>, 2024, rustfoundation.org. Accessed 25 Oct. 2026.",
        "Edwards, Julian. \"RFC (Request For Comment) Explained.\" <i>YouTube</i>, uploaded by Computerphile, 29 May 2013, youtu.be/8IXLpoN8Xj0.",
        "Matsakis, Nicholas. \"Rust Roadmap 2.0.\" <i>YouTube</i>, uploaded by RustConf, 18 Sept. 2024, www.youtube.com/watch?v=7YjomcXNvTk.",
        "\"Pattern-Binding Modes.\" <i>The Rust RFC Book</i>, GitHub, rust-lang.github.io/rfcs/2005-match-ergonomics.html. Accessed 25 Oct. 2026."
    ]

    for entry in works_cited:
        story.append(Paragraph(entry, mla_wc_entry))

    doc.build(story, canvasmaker=MLACanvas)
    print(f"[OK] Successfully compiled MLA 9 PDF: {output_pdf_path}")

if __name__ == "__main__":
    build_pdf()
