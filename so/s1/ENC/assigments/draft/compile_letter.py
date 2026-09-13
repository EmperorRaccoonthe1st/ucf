#!/usr/bin/env python3
"""
Compiles letter.md into a clean, light personal letter PDF.
Not in MLA format - formatted as a personal letter.
"""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfgen import canvas

def md_to_reportlab(text):
    """Convert inline markdown formatting (_italic_, **bold**) to ReportLab tags."""
    text = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    text = re.sub(r'_(.+?)_', r'<i>\1</i>', text)
    return text

def parse_letter(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    blocks = [b.strip() for b in content.split('\n\n') if b.strip()]
    return blocks

def build_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, "letter.md")
    output_dir = os.path.abspath(os.path.join(base_dir, "..", "final"))
    os.makedirs(output_dir, exist_ok=True)
    output_pdf_path = os.path.join(output_dir, "letter.pdf")

    blocks = parse_letter(md_path)

    # Clean personal letter geometry
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=54,      # 0.75 in
        rightMargin=54,     # 0.75 in
        topMargin=54,       # 0.75 in
        bottomMargin=54     # 0.75 in
    )

    styles = getSampleStyleSheet()

    # Personal Letter Styles - single page proportioned
    date_style = ParagraphStyle(
        'LetterDate',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10.5,
        leading=15,
        alignment=TA_LEFT,
        spaceAfter=14
    )

    salutation_style = ParagraphStyle(
        'LetterSalutation',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11,
        leading=15,
        alignment=TA_LEFT,
        spaceAfter=12
    )

    body_style = ParagraphStyle(
        'LetterBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10.5,
        leading=15,
        alignment=TA_LEFT,
        spaceAfter=10,
        firstLineIndent=0
    )

    closing_style = ParagraphStyle(
        'LetterClosing',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10.5,
        leading=15,
        alignment=TA_LEFT,
        spaceBefore=12,
        spaceAfter=20
    )

    signature_style = ParagraphStyle(
        'LetterSignature',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11,
        leading=15,
        alignment=TA_LEFT
    )

    story = []

    # blocks:
    # 0: Date ("September 13, 2026")
    # 1: Salutation ("Dear Mike,")
    # 2..-2: Body paragraphs
    # -1: Closing ("With love,\nOwen" or separate)

    # Process blocks
    date_text = blocks[0]
    salutation_text = blocks[1]
    body_blocks = blocks[2:-1]
    closing_block = blocks[-1]

    story.append(Paragraph(md_to_reportlab(date_text), date_style))
    story.append(Paragraph(md_to_reportlab(salutation_text), salutation_style))

    for p in body_blocks:
        lines = [line.strip() for line in p.split('\n') if line.strip()]
        p_joined = ' '.join(lines)
        story.append(Paragraph(md_to_reportlab(p_joined), body_style))

    # Closing block might have "With love,\nOwen"
    closing_lines = [line.strip() for line in closing_block.split('\n') if line.strip()]
    if len(closing_lines) >= 2:
        story.append(Paragraph(md_to_reportlab(closing_lines[0]), closing_style))
        story.append(Paragraph(md_to_reportlab(closing_lines[1]), signature_style))
    else:
        story.append(Paragraph(md_to_reportlab(closing_block), closing_style))

    doc.build(story)
    print(f"Successfully compiled: {output_pdf_path}")

if __name__ == "__main__":
    build_pdf()
