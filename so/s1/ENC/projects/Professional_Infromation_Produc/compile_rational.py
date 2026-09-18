#!/usr/bin/env python3
"""
compile_rational.py
Compiles rational.md into an MLA 9th Edition formatted PDF (rational.pdf).
Also provides functionality to merge document.pdf and rational.pdf into prototype.pdf.

Formatting standards strictly comply with MLA 9th Edition and summaries/GEMINI.md:
- Paper size: US Letter (8.5" x 11")
- Margins: 1.0 inch (72 pt) on all four sides
- Typography: Times-Roman, 12 pt
- Line spacing: Exact double spacing throughout (leading=24 pt)
- First-line paragraph indent: 0.5 inches (36 pt)
- Running head: Lopez [Page#] at 0.5 inches (36 pt) from top, flush with 1.0 in right margin
- Student identification block: top-left, double-spaced on first page
- Paper title: Centered, 12 pt, standard capitalization
"""

import os
import sys
import re
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Spacer
from reportlab.pdfgen import canvas
from pypdf import PdfWriter

class MLACanvas(canvas.Canvas):
    """Two-pass canvas that stamps standard MLA running heads (Lopez <Page#>)"""
    def __init__(self, *args, start_page=1, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []
        self._start_page_offset = start_page - 1

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
        page_num = self._pageNumber + self._start_page_offset
        text = f"Lopez {page_num}"
        self.drawRightString(612 - 72, 792 - 36, text)
        self.restoreState()

def md_inline_mla(text):
    """Converts inline markdown formatting (_italic_, **bold**) and XML entities to ReportLab tags."""
    # Escape & if not part of an existing entity
    text = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', text)
    # Escape bare angle brackets
    text = text.replace('<', '&lt;').replace('>', '&gt;')
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    text = re.sub(r'(?<!_)_([^_]+)_(?!_)', r'<i>\1</i>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<font face="Courier">\1</font>', text)
    return text

def parse_rational_markdown(md_path):
    """Parses rational.md into structured sections, paragraphs, and optional Works Cited."""
    if not os.path.exists(md_path):
        return [], []

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for Works Cited section
    works_cited_match = re.search(r'#+ Works Cited\s*\n(.*)', content, re.DOTALL | re.IGNORECASE)
    works_cited_entries = []
    if works_cited_match:
        wc_raw = works_cited_match.group(1)
        content = content[:works_cited_match.start()]
        entries = [e.strip() for e in wc_raw.split('\n\n') if e.strip()]
        for entry in entries:
            clean = re.sub(r'^[-*]\s+', '', entry).replace('\n', ' ')
            if clean:
                works_cited_entries.append(md_inline_mla(clean))

    # Split by double newline into block elements
    raw_blocks = [b.strip() for b in content.split('\n\n') if b.strip()]
    flowable_items = []

    for block in raw_blocks:
        lines = [l.strip() for l in block.split('\n') if l.strip()]
        if not lines:
            continue

        first_line = lines[0]
        # Heading 1 (# ...)
        if first_line.startswith("# "):
            title_text = first_line[2:].strip()
            flowable_items.append(("title", md_inline_mla(title_text)))
            continue

        # Section Heading 2 (## ...)
        if first_line.startswith("## "):
            sec_text = first_line[3:].strip()
            flowable_items.append(("h2", md_inline_mla(sec_text)))
            if len(lines) > 1:
                body_text = ' '.join(lines[1:])
                flowable_items.append(("body", md_inline_mla(body_text)))
            continue

        # Section Heading 3 (### ...)
        if first_line.startswith("### "):
            sec_text = first_line[4:].strip()
            flowable_items.append(("h3", md_inline_mla(sec_text)))
            if len(lines) > 1:
                body_text = ' '.join(lines[1:])
                flowable_items.append(("body", md_inline_mla(body_text)))
            continue

        # Regular paragraph (join wrapped lines)
        body_text = ' '.join(lines)
        flowable_items.append(("body", md_inline_mla(body_text)))

    return flowable_items, works_cited_entries

def build_rational_pdf(md_path=None, output_pdf=None, date_str=None, start_page=1):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if md_path is None:
        md_path = os.path.join(base_dir, "rational.md")
    if output_pdf is None:
        output_pdf = os.path.join(base_dir, "rational.pdf")
    if date_str is None:
        date_str = "16 September 2026"

    if not os.path.exists(md_path):
        print(f"[FAIL] Source markdown not found: {md_path}")
        return False

    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=72
    )

    styles = getSampleStyleSheet()

    mla_id = ParagraphStyle(
        'MLAIdentification',
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
        'MLAPaperTitle',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=24,
        alignment=TA_CENTER,
        spaceBefore=0,
        spaceAfter=0,
        firstLineIndent=0
    )

    mla_h2 = ParagraphStyle(
        'MLASectionH2',
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

    mla_h3 = ParagraphStyle(
        'MLASectionH3',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=0,
        firstLineIndent=0,
        keepWithNext=True
    )

    mla_body = ParagraphStyle(
        'MLABodyParagraph',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=0,
        firstLineIndent=36  # Standard 0.5-inch first-line indent
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
        leftIndent=36,       # 0.5-inch hanging indent
        firstLineIndent=-36
    )

    story = []

    # 1. MLA 9 Student Identification Block (First page top-left)
    id_block = [
        "Owen Lopez",
        "Professor Faulconer",
        "ENC 3250",
        date_str
    ]
    for line in id_block:
        story.append(Paragraph(line, mla_id))

    # 2. Paper Title
    flowable_items, works_cited_entries = parse_rational_markdown(md_path)

    # Check if a custom title was defined in markdown
    custom_title = None
    body_items = []
    for itype, text in flowable_items:
        if itype == "title" and custom_title is None:
            custom_title = text
        else:
            body_items.append((itype, text))

    paper_title = custom_title if custom_title else "Rhetorical Rationale"
    story.append(Paragraph(paper_title, mla_title))

    # 3. Body paragraphs and sections
    for itype, text in body_items:
        if itype == "h2":
            story.append(Paragraph(text, mla_h2))
        elif itype == "h3":
            story.append(Paragraph(text, mla_h3))
        else:
            story.append(Paragraph(text, mla_body))

    # 4. Optional Works Cited standalone page
    if works_cited_entries:
        story.append(PageBreak())
        story.append(Paragraph("Works Cited", mla_wc_head))
        for entry in works_cited_entries:
            story.append(Paragraph(entry, mla_wc_entry))

    # Two-pass canvas stamping Lopez [Page#]
    def canvas_maker(*args, **kwargs):
        return MLACanvas(*args, start_page=start_page, **kwargs)

    doc.build(story, canvasmaker=canvas_maker)
    print(f"[OK] Successfully compiled: {output_pdf}")
    return True

def merge_documents(document_pdf_path, rational_pdf_path, output_prototype_path):
    """Merges document.pdf and rational.pdf into prototype.pdf using pypdf."""
    if not os.path.exists(document_pdf_path):
        print(f"[FAIL] document.pdf not found at: {document_pdf_path}")
        return False
    if not os.path.exists(rational_pdf_path):
        print(f"[FAIL] rational.pdf not found at: {rational_pdf_path}")
        return False

    writer = PdfWriter()
    writer.append(document_pdf_path)
    writer.append(rational_pdf_path)

    with open(output_prototype_path, "wb") as f_out:
        writer.write(f_out)

    print(f"[OK] Successfully merged into: {output_prototype_path}")
    return True

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, "rational.md")
    rational_pdf = os.path.join(base_dir, "rational.pdf")
    document_md = os.path.join(base_dir, "document.md")
    document_pdf = os.path.join(base_dir, "document.pdf")
    prototype_pdf = os.path.join(base_dir, "prototype.pdf")

    # Step 1: Ensure document.pdf is up to date with document.md
    if os.path.exists(document_md):
        if not os.path.exists(document_pdf) or os.path.getmtime(document_md) > os.path.getmtime(document_pdf):
            try:
                import compile_document
                print("[INFO] Rebuilding document.pdf from latest document.md...")
                compile_document.build_pdf()
            except Exception as e:
                print(f"[WARN] Could not auto-rebuild document.pdf: {e}")

    # Step 2: Compile rational.md to rational.pdf
    success = build_rational_pdf(md_path, rational_pdf)
    if not success:
        sys.exit(1)

    # Step 3: Merge document.pdf and rational.pdf into prototype.pdf
    merge_success = merge_documents(document_pdf, rational_pdf, prototype_pdf)
    if not merge_success:
        sys.exit(1)

if __name__ == "__main__":
    main()
