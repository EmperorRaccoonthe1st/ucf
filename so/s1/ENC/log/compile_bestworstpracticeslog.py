#!/usr/bin/env python3
"""
Compiles log/bestworstpracticeslog.md into an MLA 9th Edition formatted PDF.
Maintains newest entry at the top, standard MLA running heads, exact double spacing,
1.0-inch margins, and 12pt Times-Roman typography.
Follows the specifications in summaries/GEMINI.md.
"""

import os
import re
from datetime import datetime
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
    """Convert inline markdown formatting (_italic_, *italic*, **bold**) and entities to ReportLab tags."""
    text = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    text = re.sub(r'_(.+?)_', r'<i>\1</i>', text)
    return text

def format_date_str(raw_date):
    """Format date string like 11/08/26 to 8 November 2026."""
    raw_date = raw_date.strip()
    match = re.match(r'(\d{1,2})/(\d{1,2})/(\d{2,4})', raw_date)
    if match:
        m, d, y = match.groups()
        if len(y) == 2:
            y = "20" + y
        dt = datetime(int(y), int(m), int(d))
        return dt.strftime("%-d %B %Y")
    return raw_date

def build_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, "bestworstpracticeslog.md")
    output_pdf_path = os.path.join(base_dir, "bestworstpracticeslog.pdf")

    if not os.path.exists(md_path):
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

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

    mla_entry_date = ParagraphStyle(
        'MLAEntryDate',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=0,
        firstLineIndent=0,
        keepWithNext=True
    )

    mla_section = ParagraphStyle(
        'MLASection',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=0,
        firstLineIndent=0,
        keepWithNext=True
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

    story = []

    # Parse entries separated by `# <date>`
    raw_entries = re.split(r'\n(?=#\s+)', md_content.strip())

    # Get the latest date for the student header block
    first_entry_match = re.search(r'#\s*([0-9/]+)', raw_entries[0] if raw_entries else "")
    latest_date_str = format_date_str(first_entry_match.group(1)) if first_entry_match else "8 November 2026"

    # Student Identification Block
    heading_lines = [
        "Owen Lopez",
        "Professor Faulconer",
        "ENC 3250",
        latest_date_str
    ]
    for line in heading_lines:
        story.append(Paragraph(line, mla_heading))

    # Document Title
    story.append(Paragraph("Best and Worst Practices Log", mla_title))

    # Process each log entry
    for entry in raw_entries:
        lines = [line.strip() for line in entry.strip().split('\n') if line.strip()]
        if not lines:
            continue

        for line in lines:
            if line.startswith('# '):
                raw_date = line[2:].strip()
                formatted_date = format_date_str(raw_date)
                entry_header_text = f"Log Entry &mdash; {formatted_date}"
                story.append(Paragraph(entry_header_text, mla_entry_date))
            elif line.startswith('## '):
                sec_title = line[3:].strip()
                story.append(Paragraph(sec_title, mla_section))
            elif line.startswith('- '):
                item_text = line[2:].strip()
                converted_text = md_to_reportlab(item_text)
                story.append(Paragraph(converted_text, mla_body))
            else:
                converted_text = md_to_reportlab(line)
                story.append(Paragraph(converted_text, mla_body))

    doc.build(story, canvasmaker=MLACanvas)
    print(f"Successfully compiled: {output_pdf_path}")

if __name__ == "__main__":
    build_pdf()
