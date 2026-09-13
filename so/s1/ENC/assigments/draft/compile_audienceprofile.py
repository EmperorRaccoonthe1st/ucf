#!/usr/bin/env python3
"""
Compiles audienceprofile.md into an MLA 9th Edition formatted PDF.
Directly converts the user's # Response section into an MLA PDF
without modifying the user's original writing.
"""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Spacer
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
    # Escape & if not already an entity
    text = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', text)
    # Bold: **text** or __text__
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
    # Italics: *text* or _text_
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    text = re.sub(r'_(.+?)_', r'<i>\1</i>', text)
    return text

def parse_markdown(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract # Response section
    response_match = re.search(r'# Response\s*\n(.*)', content, re.DOTALL)
    if not response_match:
        response_text = content
    else:
        response_text = response_match.group(1)

    # Check for Works Cited section if present
    works_cited_match = re.search(r'#+ Works Cited\s*\n(.*)', response_text, re.DOTALL | re.IGNORECASE)
    works_cited_entries = []
    if works_cited_match:
        works_cited_raw = works_cited_match.group(1)
        response_text = response_text[:works_cited_match.start()]
        # Split works cited entries by blank lines or bullet points
        raw_entries = [e.strip() for e in works_cited_raw.split('\n\n') if e.strip()]
        for entry in raw_entries:
            clean_entry = re.sub(r'^[-*]\s+', '', entry).replace('\n', ' ')
            if clean_entry:
                works_cited_entries.append(md_to_reportlab(clean_entry))

    # Split response paragraphs by double newlines
    raw_paragraphs = [p.strip() for p in response_text.split('\n\n') if p.strip()]
    paragraphs = []
    for p in raw_paragraphs:
        # Join any intra-paragraph single line breaks into continuous text
        lines = [line.strip() for line in p.split('\n') if line.strip()]
        p_joined = ' '.join(lines)
        if p_joined:
            paragraphs.append(md_to_reportlab(p_joined))

    return paragraphs, works_cited_entries

def build_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, "audienceprofile.md")
    output_dir = os.path.abspath(os.path.join(base_dir, "..", "final"))
    os.makedirs(output_dir, exist_ok=True)
    output_pdf_path = os.path.join(output_dir, "audienceprofile.pdf")

    paragraphs, works_cited_entries = parse_markdown(md_path)

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
        leftIndent=36,       # 0.5 in hanging indent
        firstLineIndent=-36
    )

    story = []

    # Student Identification Block
    heading_lines = [
        "Owen Lopez",
        "Professor Faulconer",
        "ENC 3250",
        "5 September 2026"
    ]
    for line in heading_lines:
        story.append(Paragraph(line, mla_heading))

    # Paper Title
    story.append(Paragraph("Audience Profile", mla_title))

    # Body Paragraphs directly from user's Markdown
    for p in paragraphs:
        story.append(Paragraph(p, mla_body))

    # Standalone Works Cited Page (if entries exist)
    if works_cited_entries:
        story.append(PageBreak())
        story.append(Paragraph("Works Cited", mla_wc_head))
        for entry in works_cited_entries:
            story.append(Paragraph(entry, mla_wc_entry))

    doc.build(story, canvasmaker=MLACanvas)
    print(f"Successfully compiled: {output_pdf_path}")

if __name__ == "__main__":
    build_pdf()
