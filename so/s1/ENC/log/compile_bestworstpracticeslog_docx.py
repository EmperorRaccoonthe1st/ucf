#!/usr/bin/env python3
"""
Compiles log/bestworstpracticeslog.md into an MLA 9th Edition formatted DOCX / DOC document.
Includes:
- Standard MLA running head: Lopez [Page#] (top-right, 0.5 in from edge)
- Exact double spacing throughout (2.0 line spacing, 0 pt before/after)
- 1.0-inch margins on all four sides
- Identification block (top-left, double-spaced)
- Centered title: Best and Worst Practices Log
- Bold section headings with keep_with_next
- 0.5-inch first-line indents for reflective paragraphs
- Google Docs-style horizontal divider line between entries
- Preserved inline formatting (**bold**, *italic*, _italic_)
Generates both bestworstpracticeslog.doc and bestworstpracticeslog.docx.
Follows the specifications in summaries/GEMINI.md.
"""

import sys
import os

# Ensure python-docx is accessible (try persistent venv if not in current env)
try:
    import docx
except ImportError:
    venv_python = "/home/owen/.venvs/docx/bin/python3"
    if os.path.exists(venv_python) and sys.executable != venv_python:
        os.execv(venv_python, [venv_python] + sys.argv)
    else:
        raise

import re
import shutil
from datetime import datetime
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

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

def add_markdown_runs(p, text):
    """Parse inline markdown tokens (**bold**, *italic*, _italic_) and append formatted runs."""
    pattern = re.compile(r'(\*\*.*?\*\*|\*.*?\*|_.*?_)')
    parts = pattern.split(text)
    for part in parts:
        if not part:
            continue
        if part.startswith('**') and part.endswith('**'):
            r = p.add_run(part[2:-2])
            r.bold = True
        elif (part.startswith('*') and part.endswith('*')) or (part.startswith('_') and part.endswith('_')):
            r = p.add_run(part[1:-1])
            r.italic = True
        else:
            r = p.add_run(part)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)

def add_horizontal_rule(doc):
    """Add a subtle Google Docs style horizontal divider line spanning margin-to-margin."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.line_spacing = 1.0
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')       # 3/4 pt clean subtle line
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), 'A0A0A0') # Subtle gray matching Google Docs
    pBdr.append(bottom)
    pPr.append(pBdr)

def build_doc():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, "bestworstpracticeslog.md")
    output_docx_path = os.path.join(base_dir, "bestworstpracticeslog.docx")
    output_doc_path = os.path.join(base_dir, "bestworstpracticeslog.doc")

    if not os.path.exists(md_path):
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    doc = docx.Document()

    # Section & Page Setup (US Letter, 1.0-inch margins)
    for section in doc.sections:
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.header_distance = Inches(0.5)

        # Header: Lopez [Page#] (flush right)
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hp.paragraph_format.space_before = Pt(0)
        hp.paragraph_format.space_after = Pt(0)
        hp.paragraph_format.line_spacing = 1.0
        hrun = hp.add_run("Lopez ")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(12)

        # Page Number Field
        fldSimple = OxmlElement('w:fldSimple')
        fldSimple.set(qn('w:instr'), 'PAGE')
        hp._p.append(fldSimple)

    # Set Normal Style Font
    normal_style = doc.styles['Normal']
    font = normal_style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)

    def add_para(text="", align=WD_ALIGN_PARAGRAPH.LEFT, indent=0.0, bold=False, italic=False, keep_with_next=False):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 2.0
        p.paragraph_format.first_line_indent = Inches(indent)
        p.paragraph_format.keep_with_next = keep_with_next
        if text:
            r = p.add_run(text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.bold = bold
            r.italic = italic
        return p

    # Split into entry blocks separated by `# `
    raw_entries = re.split(r'\n(?=#\s+)', md_content.strip())

    # Get latest date for identification block
    first_entry_match = re.search(r'#\s*([0-9/]+)', raw_entries[0] if raw_entries else "")
    latest_date_str = format_date_str(first_entry_match.group(1)) if first_entry_match else "8 November 2026"

    # Identification Block (Top-left, double spaced)
    add_para("Owen Lopez")
    add_para("Professor Faulconer")
    add_para("ENC 3250")
    add_para(latest_date_str)

    # Document Title (Centered, double spaced)
    add_para("Best and Worst Practices Log", align=WD_ALIGN_PARAGRAPH.CENTER)

    # Process each log entry
    entry_count = 0
    for entry in raw_entries:
        lines = [line.strip() for line in entry.strip().split('\n') if line.strip()]
        if not lines:
            continue

        # Filter out standalone horizontal rule markers inside entry
        filtered_lines = [l for l in lines if l not in ['---', '***', '___']]
        if not filtered_lines:
            continue

        if entry_count > 0:
            # Google Docs style horizontal divider between entries
            add_horizontal_rule(doc)

        entry_count += 1

        for line in filtered_lines:
            if line.startswith('# '):
                raw_date = line[2:].strip()
                formatted_date = format_date_str(raw_date)
                entry_header_text = f"Log Entry — {formatted_date}"
                add_para(entry_header_text, bold=True, keep_with_next=True)
            elif line.startswith('## '):
                sec_title = line[3:].strip()
                add_para(sec_title, bold=True, keep_with_next=True)
            elif line.startswith('- '):
                item_text = line[2:].strip()
                p = add_para(indent=0.5)
                add_markdown_runs(p, item_text)
            else:
                p = add_para(indent=0.5)
                add_markdown_runs(p, line)

    # Save both .docx and .doc formats
    doc.save(output_docx_path)
    shutil.copyfile(output_docx_path, output_doc_path)
    print(f"Successfully generated: {output_doc_path}")
    print(f"Successfully generated: {output_docx_path}")

if __name__ == "__main__":
    build_doc()
