#!/usr/bin/env python3
"""
Compiles infoinventory.md into an MLA 9th Edition formatted PDF.
Converts everything after '# Response', formatting Part Two into an MLA Table.
"""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, PageBreak, Spacer, Table, TableStyle, KeepTogether
)
from reportlab.pdfgen import canvas
from reportlab.lib import colors

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

def build_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.abspath(os.path.join(base_dir, "..", "final"))
    os.makedirs(output_dir, exist_ok=True)
    output_pdf_path = os.path.join(output_dir, "infoinventory.pdf")

    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=72
    )

    styles = getSampleStyleSheet()

    # MLA Styles
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

    mla_h1 = ParagraphStyle(
        'MLASectionH1',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=12,
        spaceAfter=0,
        firstLineIndent=0
    )

    mla_h2 = ParagraphStyle(
        'MLASectionH2',
        parent=styles['Normal'],
        fontName='Times-BoldItalic',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=8,
        spaceAfter=0,
        firstLineIndent=0
    )

    mla_h3 = ParagraphStyle(
        'MLASectionH3',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=6,
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

    mla_item = ParagraphStyle(
        'MLAItem',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=0,
        leftIndent=36,
        firstLineIndent=-18
    )

    mla_subitem = ParagraphStyle(
        'MLASubItem',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=24,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=0,
        leftIndent=54,
        firstLineIndent=-18
    )

    # Table styles (10pt Times-Roman for compact, clean tabular presentation)
    table_header = ParagraphStyle(
        'MLATableHeader',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=11,
        leading=14,
        alignment=TA_LEFT
    )

    table_cell = ParagraphStyle(
        'MLATableCell',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10.5,
        leading=14,
        alignment=TA_LEFT
    )

    table_caption_num = ParagraphStyle(
        'MLATableNum',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=11,
        leading=16,
        alignment=TA_LEFT,
        spaceBefore=14,
        spaceAfter=2,
        firstLineIndent=0
    )

    table_caption_title = ParagraphStyle(
        'MLATableTitle',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=11,
        leading=16,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=8,
        firstLineIndent=0
    )

    story = []

    # Identification Block
    heading_lines = [
        "Owen Lopez",
        "Professor Faulconer",
        "ENC 3250",
        "13 September 2026"
    ]
    for line in heading_lines:
        story.append(Paragraph(line, mla_heading))

    # Paper Title
    story.append(Paragraph("Information Inventory and Content Strategy", mla_title))

    # --- Part One ---
    story.append(Paragraph("Part One: Information Inventory &amp; Content Strategy", mla_h1))

    story.append(Paragraph(
        "My professional document will be about the code editor <i>Vim</i>, in particular the <i>VS Code</i> "
        "Extension for <i>Vim</i>. It will primarily focus on conveying basic usage of the code editor and the "
        "philosophy that supports its particular manner of editing.",
        mla_body
    ))

    # Information Inventory
    story.append(Paragraph("Information Inventory", mla_h2))

    # Must Know
    story.append(Paragraph("Must Know", mla_h3))
    story.append(Paragraph("1. <i>Core Navigation</i>: How to move the cursor.", mla_item))
    story.append(Paragraph("2. <i>Modal Editing</i>: The fundamental philosophy behind the <i>Vim</i> code editor.", mla_item))
    story.append(Paragraph("3. <i>Essential Modes</i>: How one operates the program.", mla_item))
    story.append(Paragraph("4. <i>File Operations</i>: Saving and editing files, behaviors that are required to work with a project.", mla_item))

    # Useful to Know
    story.append(Paragraph("Useful to Know", mla_h3))
    story.append(Paragraph("1. <i>Advanced Navigation</i>: Specific mechanisms for moving efficiently throughout a file.", mla_item))
    story.append(Paragraph("2. <i>Editing Operators</i>: Controls for editing entire blocks of text.", mla_item))
    story.append(Paragraph("3. <i>Operator Combination</i>: High-level logic that allows for chains of commands.", mla_item))
    story.append(Paragraph("4. <i>Search Operator</i>: Mechanisms for retrieving and editing specific parts of a document.", mla_item))

    # Don't Need to Know
    story.append(Paragraph("Don't Need to Know", mla_h3))
    story.append(Paragraph("1. <i>Terminal Vim</i>: Downloading and operating Vim from a terminal. The document will only explain <i>Vim</i> concepts that can be utilized anywhere.", mla_item))
    story.append(Paragraph("2. <i>REGEX</i>: REGEX is an advanced pattern-matching tool that can be used in search strings; it is outside the scope of this document.", mla_item))
    story.append(Paragraph("3. <i>Buffer Management</i>: The ability to open new visual panes, which display text concurrently.", mla_item))
    story.append(Paragraph("4. <i>Configuration</i>: <i>Vim</i> contains an entire scripting and configuration language (in fact, two entire languages). These topics require a deeper analysis than can be provided in this document.", mla_item))

    # Content Strategy
    story.append(Paragraph("Content Strategy", mla_h2))

    story.append(Paragraph(
        "The essential message of my document will be explaining how to properly utilize <i>Vim</i> in an introductory manner. "
        "As the program is very complex, it is essential that the guide covers only the most necessary features and concepts to "
        "allow a new user to start working within it. For this reason, the guide will focus on how to use an extension for the popular "
        "<i>VS Code</i> that utilizes only the core features of <i>Vim</i>, rather than the native terminal application.",
        mla_body
    ))

    story.append(Paragraph(
        "The audience will require, in the following order, three key concepts in order to gain a basic understanding of <i>Vim</i>. "
        "They will begin with an overview of the Modal Editing Paradigm, which is the concept of editing data through utilizing specific "
        "tools, or modes. Applications like image editors or 3D modeling tools function in this manner, where users rotate between different "
        "tools that all behave differently. Once modal editing has been established, navigation throughout a project will be the first "
        "topic covered. This requires the explanation and memorization of the functions of a myriad of keys. Each key in Vim performs some "
        "action, and there are around ten keys to learn for basic navigation. Now that the audience can navigate, we will turn to actually "
        "performing some productive edits with basic operators. As with navigation, every key performs something different and thus has "
        "to be learned. Finally, the guide will end with file-level commands, like saving or exiting. These operate on a higher plane than "
        "a user's edits, with there being a core few that should be learned for basic usage.",
        mla_body
    ))

    story.append(Paragraph(
        "There is an enormous amount of information that could be covered in the document, but I have decided to ignore the majority of it. "
        "Specifically, I will not cover configuration and the command line. <i>Vim</i> can be configured through a file written with a "
        "domain-specific language (Vimscript); learning an entire language in an introductory guide is impractical. The program is also "
        "typically interacted with in the terminal and the command line (CMD). As the audience will instead be learning through the "
        "<i>VS Code</i> extension, I will not mention any of the numerous command-line quirks that can be found when using native <i>Vim</i>.",
        mla_body
    ))

    story.append(Paragraph(
        "I intend for the audience to download the extension and follow along with the guide themselves. Following along will provide the "
        "most efficient manner to learn the information presented. I have decided to use the <i>VS Code</i> extension due to my audience's "
        "lack of command-line knowledge. It is simpler to introduce <i>Vim</i> itself to begin with and then allow them to dive into the CMD "
        "when they are ready. Additionally, I will be framing <i>Vim</i> primarily as a code editing tool rather than a general-purpose text "
        "editor (I'm using it currently to write this document). This framing will appeal to the audience due to their programming background, "
        "as a means for enhancing their efficiency.",
        mla_body
    ))

    # --- Part Two: The "So What?" Test ---
    story.append(PageBreak())
    story.append(Paragraph("Part Two: The &ldquo;So What?&rdquo; Test", mla_h1))

    # Table 1 Header Block (Standard MLA Table format)
    table_caption = [
        Paragraph("Table 1", table_caption_num),
        Paragraph("The &ldquo;So What?&rdquo; Test: Audience Relevance of Core Vim Concepts", table_caption_title)
    ]
    story.append(KeepTogether(table_caption))

    # 10 facts table data
    facts_data = [
        [
            Paragraph("Information / Concept", table_header),
            Paragraph("Why Does My Audience Need to Know This? (\"So What?\")", table_header)
        ],
        [
            Paragraph("1. <i>Vim</i> utilizes different modes to edit text.", table_cell),
            Paragraph("This allows for complex chains of actions and utilization of solely the keyboard.", table_cell)
        ],
        [
            Paragraph("2. Pressing 'i' enters insert mode.", table_cell),
            Paragraph("This is the primary manner of adding new text to a document.", table_cell)
        ],
        [
            Paragraph("3. Pressing 'Esc' or 'Ctrl-c' returns the user to normal mode.", table_cell),
            Paragraph("This is required to switch back to navigation and command modes throughout Vim.", table_cell)
        ],
        [
            Paragraph("4. The keys 'h', 'j', 'k', and 'l' control directional cursor navigation.", table_cell),
            Paragraph("This keeps navigation bound entirely to the keyboard home row, eliminating mouse reliance.", table_cell)
        ],
        [
            Paragraph("5. Pressing 'w' and 'b' advances the cursor forward and backward across words.", table_cell),
            Paragraph("This enables rapid traversal through tokens and code identifiers without repeated keystrokes.", table_cell)
        ],
        [
            Paragraph("6. Pressing 'x' deletes the character currently under the cursor.", table_cell),
            Paragraph("This allows quick single-character corrections without switching out of normal mode.", table_cell)
        ],
        [
            Paragraph("7. Pressing 'dd' deletes a line, while 'yy' copies it to the clipboard.", table_cell),
            Paragraph("This executes line-level manipulation commands in a single streamlined, reproducible action.", table_cell)
        ],
        [
            Paragraph("8. Pressing 'p' pastes the most recently yanked or deleted text after the cursor.", table_cell),
            Paragraph("This completes basic cut-and-paste operations entirely within normal mode.", table_cell)
        ],
        [
            Paragraph("9. Pressing 'u' undoes changes, while 'Ctrl-r' redoes them.", table_cell),
            Paragraph("This provides essential error recovery controls directly through the keyboard interface.", table_cell)
        ],
        [
            Paragraph("10. Pressing ':' opens the command-line interface for ex-commands like ':w' and ':q'.", table_cell),
            Paragraph("This executes core file operations such as saving and closing buffers without menu navigation.", table_cell)
        ],
    ]

    col_widths = [200, 268]  # Total 468 pt (6.5 in printable width)
    chart_table = Table(facts_data, colWidths=col_widths, repeatRows=1)
    chart_table.setStyle(TableStyle([
        # Standard MLA Table lines: top, bottom of header, and bottom of table
        ('LINEABOVE', (0, 0), (-1, 0), 1.0, colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 1.0, colors.black),
        ('LINEBELOW', (0, -1), (-1, -1), 1.0, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))

    story.append(chart_table)

    doc.build(story, canvasmaker=MLACanvas)
    print(f"Successfully compiled: {output_pdf_path}")

if __name__ == "__main__":
    build_pdf()
