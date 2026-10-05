#!/usr/bin/env python3
"""
Compiles ethics assignment into MLA 9th Edition formatted PDFs.
Produces both:
  1. Verbatim edition (compiling user's exact ethics.md response)
  2. Enhanced edition (complete 300-400 word essay with full MLA citations & Works Cited)
"""

import os
import re
import shutil
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
    text = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
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
        raw_entries = [e.strip() for e in works_cited_raw.split('\n\n') if e.strip()]
        for entry in raw_entries:
            clean_entry = re.sub(r'^[-*]\s+', '', entry).replace('\n', ' ')
            if clean_entry:
                works_cited_entries.append(md_to_reportlab(clean_entry))

    raw_paragraphs = [p.strip() for p in response_text.split('\n\n') if p.strip()]
    paragraphs = []
    for p in raw_paragraphs:
        lines = [line.strip() for line in p.split('\n') if line.strip()]
        p_joined = ' '.join(lines)
        if p_joined:
            paragraphs.append(md_to_reportlab(p_joined))

    return paragraphs, works_cited_entries

def create_pdf(output_pdf_path, title_text, paragraphs, works_cited_entries=None, date_str="30 September 2026"):
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
        date_str
    ]
    for line in heading_lines:
        story.append(Paragraph(line, mla_heading))

    # Paper Title
    story.append(Paragraph(title_text, mla_title))

    # Body Paragraphs
    for p in paragraphs:
        story.append(Paragraph(p, mla_body))

    # Works Cited Page
    if works_cited_entries:
        story.append(PageBreak())
        story.append(Paragraph("Works Cited", mla_wc_head))
        for entry in works_cited_entries:
            story.append(Paragraph(entry, mla_wc_entry))

    doc.build(story, canvasmaker=MLACanvas)
    print(f"Compiled successfully: {output_pdf_path}")

def build_all():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_verbatim_path = os.path.join(base_dir, "ethics.md")
    md_enhanced_path = os.path.join(base_dir, "ethics_enhanced.md")
    
    final_dir = os.path.abspath(os.path.join(base_dir, "..", "final"))
    os.makedirs(final_dir, exist_ok=True)
    
    work_dir = "/home/owen/Downloads/tmp/ethics"

    # --- 1. Verbatim Build ---
    v_paras, v_wc = parse_markdown(md_verbatim_path)
    # If verbatim has no citations in markdown, supply default MLA Works Cited entry for Beilfuss
    if not v_wc:
        v_wc = [
            md_to_reportlab(
                'Beilfuss, Michael. "Chapter 4: Ethics." _Technical and Professional Writing Genres: A Study in Theory and Practice_, '
                'edited by Eric Howerton, Oklahoma State University Libraries / Open Textbook Library, 2020, '
                'open.umn.edu/opentextbooks/textbooks/721. Accessed 30 Sept. 2026.'
            )
        ]
    
    # Compile ethics.md directly to ethics.pdf (standard assignment target)
    pdf_final = os.path.join(final_dir, "ethics.pdf")
    pdf_draft = os.path.join(base_dir, "ethics.pdf")
    create_pdf(pdf_final, "Ethical Conundrums in Software Development", v_paras, v_wc)
    shutil.copyfile(pdf_final, pdf_draft)

    # Copy output to active working directory
    if os.path.exists(work_dir):
        shutil.copyfile(pdf_final, os.path.join(work_dir, "ethics.pdf"))
        print(f"Copied ethics.pdf to {work_dir}")

if __name__ == "__main__":
    build_all()
