#!/usr/bin/env python3
"""
Compiles bestworstpracticeslog.md into an MLA 9th Edition formatted PDF.
Follows the specifications in summaries/GEMINI.md.
"""

import os
import re
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

def build_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_pdf_path = os.path.join(base_dir, "bestworstpracticeslog.pdf")

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

    mla_section = ParagraphStyle(
        'MLASection',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
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

    story = []

    # Student Identification Block
    heading_lines = [
        "Owen Lopez",
        "Professor Faulconer",
        "ENC 3250",
        "29 August 2026"
    ]
    for line in heading_lines:
        story.append(Paragraph(line, mla_heading))

    # Document Title
    story.append(Paragraph("Best and Worst Practices Log", mla_title))

    # Best Practices Section
    story.append(Paragraph("Best Practices", mla_section))
    story.append(Paragraph(
        "<i>Vocabulary</i>: In almost every serious sentence I put down I will review for grammar, "
        "punctuation, &amp; specifically for vocabulary. I ensure that every verb, noun, or adverb is "
        "specifically chosen to reflect the context of my current piece and always aims for a high level "
        "of complexity/detail. It is very rare for me to utilize a \"simple\" word or phrase when I am "
        "writing, as I really do spend a considerable amount of time choosing the proper, advanced, "
        "term for the situation.",
        mla_body
    ))

    # Worst Practices Section
    story.append(Paragraph("Worst Practices", mla_section))
    story.append(Paragraph(
        "<i>Run-On Sentences</i>: Run-On sentences are when an author places too many clauses into "
        "a single sentence, through commas or repetitive uses of conjunctions, instead of utilizing "
        "multiple related sentences. I often find myself writing Run-On sentences when I want to express "
        "a complex though. I have to slow down, evaluate my last sentence, and split it into multiple "
        "complete sentences.",
        mla_body
    ))

    doc.build(story, canvasmaker=MLACanvas)
    print(f"Successfully compiled: {output_pdf_path}")

if __name__ == "__main__":
    build_pdf()
