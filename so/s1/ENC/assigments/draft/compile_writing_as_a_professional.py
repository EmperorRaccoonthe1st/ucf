#!/usr/bin/env python3
"""
Compiles writing_as_a_professional.md into a unified MLA 9th Edition PDF.
Follows the requirements:
- Document 1: Professional Email (workplace email format)
- Document 2: Professional Memo (workplace memo format)
- Document 3: Rhetorical Rationale (MLA academic paper format)
All in one unified .pdf deliverable with MLA running head (Lopez <Page#>)
and student identification block.
"""

import os
import re
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    PageBreak,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    HRFlowable
)
from reportlab.graphics.shapes import Drawing, Line
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

def md_to_reportlab(text):
    """Convert inline markdown formatting (_italic_, **bold**) and XML entities to ReportLab tags."""
    # Escape standalone ampersands
    text = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
    # Italics
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    text = re.sub(r'_(.+?)_', r'<i>\1</i>', text)
    # Curly quotes / clean quotes
    text = text.replace("“", "&ldquo;").replace("”", "&rdquo;")
    return text

def parse_source(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get content after # Response
    response_idx = content.find('# Response')
    if response_idx != -1:
        resp_text = content[response_idx + len('# Response'):]
    else:
        resp_text = content

    return resp_text

def build_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, "writing_as_a_professional.md")
    output_dir = os.path.abspath(os.path.join(base_dir, "..", "final"))
    os.makedirs(output_dir, exist_ok=True)
    output_pdf_path = os.path.join(output_dir, "writing_as_a_professional.pdf")
    draft_pdf_path = os.path.join(base_dir, "writing_as_a_professional.pdf")

    # Document Geometry: Standard Letter, 1-inch margins (72 pt)
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=72
    )

    styles = getSampleStyleSheet()

    # --- MLA Styles ---
    mla_id = ParagraphStyle(
        'MLAIdBlock',
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
        spaceAfter=18,
        firstLineIndent=0
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=12,
        leading=22,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=12,
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

    # --- Workplace Document Styles ---
    # Email styles
    email_hdr_label = ParagraphStyle(
        'EmailHdrLabel',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=11,
        leading=16,
        alignment=TA_LEFT
    )

    email_hdr_val = ParagraphStyle(
        'EmailHdrVal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11,
        leading=16,
        alignment=TA_LEFT
    )

    email_body = ParagraphStyle(
        'EmailBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11,
        leading=16,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=10,
        firstLineIndent=0
    )

    # Memo styles
    memo_title_style = ParagraphStyle(
        'MemoTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=18,
        leading=22,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=14
    )

    memo_hdr_label = ParagraphStyle(
        'MemoHdrLabel',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=11,
        leading=16,
        alignment=TA_LEFT
    )

    memo_hdr_val = ParagraphStyle(
        'MemoHdrVal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11,
        leading=16,
        alignment=TA_LEFT
    )

    memo_body = ParagraphStyle(
        'MemoBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11,
        leading=16,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=10,
        firstLineIndent=0
    )

    story = []

    # =========================================================================
    # PAGE 1: MLA Identification Block, Title, and Document 1: Professional Email
    # =========================================================================
    # MLA Heading block
    id_lines = [
        "Owen Lopez",
        "Professor Faulconer",
        "ENC 3250",
        "5 November 2026"
    ]
    for line in id_lines:
        story.append(Paragraph(line, mla_id))

    story.append(Spacer(1, 12))
    story.append(Paragraph("Writing as a Professional: Email, Memo, and Rhetorical Rationale", mla_title))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Document 1: Professional Email", section_heading))

    # Email Box Container
    # Email Header table
    email_hdr_data = [
        [Paragraph("<b>To:</b>", email_hdr_label), Paragraph("Mr. John", email_hdr_val)],
        [Paragraph("<b>From:</b>", email_hdr_label), Paragraph("Owen Lopez", email_hdr_val)],
        [Paragraph("<b>Date:</b>", email_hdr_label), Paragraph("November 5, 2026", email_hdr_val)],
        [Paragraph("<b>Subject:</b>", email_hdr_label), Paragraph("Compeletion of Primary Deck for Upcoming Product Launch", email_hdr_val)]
    ]

    email_hdr_table = Table(email_hdr_data, colWidths=[65, 375])
    email_hdr_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))

    # Inner email flowables
    email_inner_story = [
        email_hdr_table,
        Spacer(1, 6),
        HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#CCCCCC'), spaceBefore=4, spaceAfter=10),
        Paragraph("Good Afternoon Mr.John,", email_body),
        Paragraph(
            "Currently the primary deck for the upcoming product launch is lacking the penulitmate segment "
            "detailing the future development plans of organization. The contents of this section have been "
            "discussed at length between the development and marketing leads. The agreed upon talking points "
            "can be found in the folder &lsquo;launch/presentation/future_development_plans&rsquo; in the "
            "company Microsoft Sharepoint. The presentation should adapt the majority of the items mentioned "
            "within the document, providing a detailed explination of our future goals and upcoming "
            "supplementary products. As the presentation is occuring on November 6th, exactly two days from now, "
            "please have the deck completed and submitted for review by tonight.",
            email_body
        ),
        Spacer(1, 4),
        Paragraph("Respectully,<br/>Owen Lopez", email_body)
    ]

    # Wrap in framed table container
    email_container_data = [[email_inner_story]]
    email_container_table = Table(email_container_data, colWidths=[468])
    email_container_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CCCCCC')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FBFBFB')),
        ('TOPPADDING', (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 14),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ]))

    story.append(email_container_table)

    # =========================================================================
    # PAGE 2: Document 2: Professional Memo
    # =========================================================================
    story.append(PageBreak())

    story.append(Paragraph("Document 2: Professional Memo", section_heading))
    story.append(Spacer(1, 4))

    # Memo Title
    story.append(Paragraph("MEMORANDUM", memo_title_style))

    # Memo Header Block
    memo_hdr_data = [
        [Paragraph("<b>TO:</b>", memo_hdr_label), Paragraph("James Smith, CTO, Head of Marketing", memo_hdr_val)],
        [Paragraph("<b>FROM:</b>", memo_hdr_label), Paragraph("Owen Lopez, Head of Operations", memo_hdr_val)],
        [Paragraph("<b>DATE:</b>", memo_hdr_label), Paragraph("November 5, 2026", memo_hdr_val)],
        [Paragraph("<b>SUBJECT:</b>", memo_hdr_label), Paragraph("Product Launch Presentation Delay", memo_hdr_val)]
    ]

    memo_hdr_table = Table(memo_hdr_data, colWidths=[75, 393])
    memo_hdr_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))

    story.append(memo_hdr_table)
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#222222'), spaceBefore=4, spaceAfter=14))

    # Memo Body
    story.append(Paragraph(
        "The primary presentation for the upcoming product launch is currently not complete, as it it missing "
        "the final segment detailing our future goals. This is an integral component of our presentation, "
        "one which would prevent us from being able to deliver it if it were to remain in the current unfinished state.",
        memo_body
    ))

    story.append(Paragraph(
        "To resolve this issue in a timely matter, lead of the project has recieved instructions to complete "
        "this segment of the presentation by 5 PM today. Once the entire presentation is finished, we on the "
        "product launch team will have time to tweak the it and finalize the document for the upcoming launch on Friday.",
        memo_body
    ))

    story.append(Paragraph(
        "Please reach out to me for review of the current presention if you require it.",
        memo_body
    ))

    # =========================================================================
    # PAGE 3: Document 3: Rhetorical Rationale (MLA Academic Paper)
    # =========================================================================
    story.append(PageBreak())

    story.append(Paragraph("Document 3: Rhetorical Rationale", section_heading))

    rhetorical_paragraphs = [
        "Each document, the email and memo, required a meticulous arrangement of tone, formatting, and content in "
        "order to properly suit the purpose of their audiences. The memo was directed at leadership staff with the "
        "purpose of informing them about a potential scheduling delay, and the email communicated with a coworker to "
        "establish a deadline for a specific segment of the upcoming product launch. These two related but fundamentally "
        "different goals dictated the exact combination of tone and content which each document was developed with. "
        "The group nature of informing management suited the broad dispersion of a memo, while the interpersonal "
        "communication required to inform the employee best suited the personal structure of an email.",

        "When authoring the email the primary goal was to establish the deadline. Such an immediate subject required "
        "clear and effect communication of the exact requirements and scope of the tasking being assigned. This "
        "included specific details on where to locate the information for the presentation. The memo also "
        "necessitated this urgency, but to a much lesser extent. Thus the central content of the email focused on "
        "providing clear instructions followed by the time in which they must be completed.",

        "In contrast, the memo which only simply needed to inform management of the situation focused primarily on "
        "the current condition of the overall product launch, rather then delving down into the specifics required "
        "to complete the presentation. It continued to discuss how the contribution, when eventually finished, would "
        "integrate with the launch and lead to a successful event. This supplementary was only necessary for "
        "management and not the employee who was instructed to finish the presentation.",

        "The overall most challenging aspect of drafting these two documents (other than the creativity required to "
        "establish the scenario) was ensuring that each piece of communication remained both formal and respectful while "
        "presented as succinctly as possible. In order to achieve these goals the documents were written with a clear "
        "formal tone which lacks common <i>slang</i> or other examples of unprofessional language. Additionally, "
        "ensuring that the email was an efficient call-to-action for the employee while remaining respectful was a "
        "particularly difficult challenge. In industry is is vital that one remains professional and respectful "
        "throughout all situations and all employees, even if through unfortunate situations like admonishment."
    ]

    for i, p in enumerate(rhetorical_paragraphs):
        # Keep the final paragraph intact on page 4 so it does not awkwardly split mid-sentence
        if i == len(rhetorical_paragraphs) - 1:
            story.append(KeepTogether([Paragraph(p, mla_body)]))
        else:
            story.append(Paragraph(p, mla_body))

    # Build Document
    doc.build(story, canvasmaker=MLACanvas)
    print(f"Compiled successfully: {output_pdf_path}")

    shutil.copyfile(output_pdf_path, draft_pdf_path)
    print(f"Draft mirrored: {draft_pdf_path}")

if __name__ == "__main__":
    build_pdf()
