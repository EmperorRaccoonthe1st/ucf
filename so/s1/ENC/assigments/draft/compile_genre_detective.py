#!/usr/bin/env python3
"""
Compiles genre_detective.md into an MLA 9th Edition formatted PDF.
Follows the specifications in summaries/GEMINI.md.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Spacer, Image, KeepTogether, Table, TableStyle
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

def build_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Output to ../final/genre_detective.pdf
    output_dir = os.path.abspath(os.path.join(base_dir, "..", "final"))
    os.makedirs(output_dir, exist_ok=True)
    output_pdf_path = os.path.join(output_dir, "genre_detective.pdf")

    img_path = os.path.join(base_dir, "CSS_Framework_Outline.png")

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
        spaceAfter=12,
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
        leftIndent=36,       # Hanging indent
        firstLineIndent=-36
    )

    story = []

    # Student Identification Block
    heading_lines = [
        "Owen Lopez",
        "Professor Faulconer",
        "ENC 3250",
        "3 September 2026"
    ]
    for line in heading_lines:
        story.append(Paragraph(line, mla_heading))

    # Paper Title
    story.append(Paragraph("Genre Detective: Architecture Decision Records", mla_title))

    # Paragraph 1
    story.append(Paragraph(
        "An important type of document utilized within software development is the ADR, which is short for "
        "<i>Architecture Decision Record</i>. This genre of document records both project architectural decisions "
        "and their surrounding context in order to preserve the rationale behind an individual decision over the course "
        "of a project's life cycle. They are dense technical documents that capture a consequential architecture decision "
        "in its entirety, explicitly describing how it will affect the project, other alternatives that were considered, "
        "and provide instructions for maintaining the decision in the future.",
        mla_body
    ))

    # Paragraph 2
    story.append(Paragraph(
        "As the ADR closely follows its subject matter and can be found throughout many differing technical domains, "
        "the exact form and audience can vary greatly. This analysis will trace two documents: \"Architecture Decision "
        "Record: CSS Framework\" and \"Environment Variable Configuration.\" They were written by members of a "
        "development team for use within their respective projects throughout the planning and development processes.",
        mla_body
    ))

    # Paragraph 3
    story.append(Paragraph(
        "Depending on an organization's structure, ADRs are not only written for their technical team, but also serve "
        "as a record for those who are supporting the development of the project. As a result, they must both be highly "
        "specific and informative while still being approachable for the relative layman who may not be as familiar with "
        "the project as the authors. The sources are written in a clear declarative style which utilizes plain English, "
        "littered with technical terms where necessary, to describe architecture choices and the rationale behind them. "
        "They assume a basic knowledge of the overall project as it relates to the subject of the record as well as an "
        "understanding of the domain-specific verbiage required to communicate about the subject.",
        mla_body
    ))

    # Paragraph 4
    story.append(Paragraph(
        "The sources share the inherent goal of properly documenting their specific architectural decision; to that "
        "end, their practical goals differ slightly due to their circumstances. \"Architecture Decision Record: CSS "
        "Framework\" records the choice of a CSS framework for a dynamic multi-platform web application, and \"Environment "
        "Variable Configuration\" records the decision for a framework to store application environment variables across "
        "differing deployment conditions. These decisions require variation in the information presented in order to "
        "fully document their situation, but nonetheless the message is designed to convey an understanding of the "
        "environment in which the decision was reached and to capture the logic behind it.",
        mla_body
    ))

    # Paragraph 5
    story.append(Paragraph(
        "ADRs are broken into multiple different sections that are separated by a bolded header which outlines the topic "
        "of a section. Within each section can be either a chart, diagram, bullet point, code snippet, or text. They are "
        "purposely designed to be simple, iterative documents often residing alongside source code, and depending on the "
        "practices of an organization are managed by the same version control system. A proper ADR system should allow "
        "for quick and efficient creation of new ADRs whenever a new architectural decision must be made. They must also "
        "be accessible to the entire development team as the decisions that they record dictate the actions and future "
        "decisions of the whole team. The document attempts to present its contents as succinctly and quickly as possible "
        "through the clear division of information, allowing access to its audience in a rapidly evolving environment.",
        mla_body
    ))

    # Paragraph 6
    story.append(Paragraph(
        "Both examples share an architecture designed to present an overview of the decision and its surrounding "
        "environment, then dive into the unique details of the ADR. They explain the goals of the decisions, their "
        "constraints between differing choices, the options that were considered, and then convey the argument behind "
        "the final decision recorded in the document (\"Architecture Decision Record: CSS Framework\"; \"Environment "
        "Variable Configuration\"). After establishing the primary rationale, the sources then evaluate the results, "
        "both positive and negative, of the architectural decision. An ADR does not necessarily require an exact format "
        "between projects, but they all share one very similar to the examples provided in this analysis. The nature of an "
        "ADR allows for variation across the genre in the presentation of information, but every instance retains the "
        "same tone of efficient, detailed transfer of information.",
        mla_body
    ))

    # Figure 1: Comparative Image flowable
    img1_path = os.path.join(base_dir, "CSS_Framework_Outline_clean.png")
    img2_path = os.path.join(base_dir, "Environment_Variable_Configuration_Outline_clean.png")

    if os.path.exists(img1_path) and os.path.exists(img2_path):
        # Height 200 pt, width proportional
        h = 200
        w1 = 200 * (305 / 515)  # ~118 pt
        w2 = 200 * (275 / 514)  # ~107 pt
        im1 = Image(img1_path, width=w1, height=h)
        im2 = Image(img2_path, width=w2, height=h)

        table_data = [[im1, im2]]
        fig_table = Table(table_data, colWidths=[w1 + 20, w2 + 20])
        fig_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ]))

        fig_elements = [
            fig_table,
            Paragraph(
                "<i>Fig. 1</i>. Structural outlines of <i>Architecture Decision Record: CSS Framework</i> (left) and "
                "<i>Environment Variable Configuration</i> (right), illustrating shared organizational conventions.",
                mla_caption
            )
        ]
        story.append(KeepTogether(fig_elements))

    # Paragraph 7 (Conclusion)
    story.append(Paragraph(
        "Like the many other document genres utilized throughout the complex processes of software development, the "
        "ADR is primarily utilitarian. This is observed through the tone, content, and scope of the document. I have "
        "previously been unfamiliar with creating and consuming such a brisk, informative manner of writing. Through "
        "analyzing and learning about the ADR, I have grown accustomed to the style that is required within a software "
        "development environment. When authoring the document for the \"Professional Information Product,\" I will model "
        "my work after the professional documents that I have reviewed for this study and ensure that it would be suitable "
        "for a software development environment.",
        mla_body
    ))

    # Standalone Works Cited Page
    story.append(PageBreak())
    story.append(Paragraph("Works Cited", mla_wc_head))

    works_cited_entries = [
        "\"Architecture Decision Record: CSS Framework.\" <i>Architecture Decision Record</i>, GitHub, "
        "<br/>github.com/architecture-decision-record/architecture-decision-record/tree/main/"
        "<br/>locales/en/examples/css-framework.",
        "\"Environment Variable Configuration.\" <i>Architecture Decision Record</i>, GitHub, "
        "<br/>github.com/architecture-decision-record/architecture-decision-record/tree/main/"
        "<br/>locales/en/examples/environment-variable-configuration."
    ]

    for entry in works_cited_entries:
        story.append(Paragraph(entry, mla_wc_entry))

    doc.build(story, canvasmaker=MLACanvas)
    print(f"Successfully compiled: {output_pdf_path}")

if __name__ == "__main__":
    build_pdf()
