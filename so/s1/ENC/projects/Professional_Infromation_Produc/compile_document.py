#!/usr/bin/env python3
"""
compile_document.py
Compiles document.md into a publication-grade PDF (document.pdf).
Dynamically parses Markdown syntax including:
- Metadata header block
- Level 1, 2, and 3 headings
- Clean typography and robust inline styling (escaping bare angle brackets, bold, italic, code backticks)
- Multi-style callouts (NOTE, PRO TIP, WARNING)
- Preformatted ASCII diagrams (rendered via Courier)
- Markdown tables with headers and zebra striping
- Smart image placement (wide banners vs. two-column vertical crops)
- 4-page balanced layout with zero orphan table rows
- Running header/footer with dynamic 'Page X of Y' page numbering
"""

import os
import re
from PIL import Image as PILImage

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, PageBreak, Spacer, Image, KeepTogether, Table, TableStyle, Preformatted
)
from reportlab.pdfgen import canvas

class TechnicalDocCanvas(canvas.Canvas):
    """Two-pass canvas for dynamic running headers and footers with 'Page X of Y'."""
    doc_title = "Vim in VSCode"
    doc_subtitle = "An Introduction to Vim Motions"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, total_pages):
        self.saveState()
        page_w, page_h = letter  # 612 x 792 pt
        margin_x = 54  # 0.75 in
        
        # Suppress running header on page 1
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#475569"))
            self.drawString(margin_x, page_h - 36, self.doc_title)
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#475569"))
            self.drawRightString(page_w - margin_x, page_h - 36, self.doc_subtitle)
            
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(margin_x, page_h - 42, page_w - margin_x, page_h - 42)

        # Running footer on all pages
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(margin_x, 42, page_w - margin_x, 42)

        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(margin_x, 30, "ENC 3250: Professional & Technical Writing")
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawRightString(page_w - margin_x, 30, page_str)

        self.restoreState()

def md_inline(text):
    """Converts inline markdown to ReportLab XML tags with strict angle bracket escaping."""
    # 1. Escape literal ampersands
    text = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', text)
    # 2. Escape literal angle brackets before adding HTML tags
    text = text.replace('<', '&lt;').replace('>', '&gt;')
    # 3. Inline code: `code` -> <b><font face="Courier">code</font></b>
    text = re.sub(r'`([^`]+)`', r'<b><font face="Courier">\1</font></b>', text)
    # 4. Bold: **bold**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # 5. Italic: *italic* or _italic_
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    text = re.sub(r'(?<!_)_([^_]+)_(?!_)', r'<i>\1</i>', text)
    return text

def make_callout(text_content, callout_type="note", width=494):
    """Generates a professional callout card with an accented left border."""
    type_configs = {
        "note": {
            "title": "NOTE",
            "border_color": colors.HexColor("#2563eb"),
            "bg_color": colors.HexColor("#eff6ff"),
            "title_color": colors.HexColor("#1e40af")
        },
        "practice": {
            "title": "GO PRACTICE!",
            "border_color": colors.HexColor("#ea580c"),
            "bg_color": colors.HexColor("#fff7ed"),
            "title_color": colors.HexColor("#c2410c")
        },
        "go practice": {
            "title": "GO PRACTICE!",
            "border_color": colors.HexColor("#ea580c"),
            "bg_color": colors.HexColor("#fff7ed"),
            "title_color": colors.HexColor("#c2410c")
        },
        "tip": {
            "title": "PRO TIP",
            "border_color": colors.HexColor("#059669"),
            "bg_color": colors.HexColor("#ecfdf5"),
            "title_color": colors.HexColor("#065f46")
        },
        "warning": {
            "title": "WARNING!",
            "border_color": colors.HexColor("#dc2626"),
            "bg_color": colors.HexColor("#fef2f2"),
            "title_color": colors.HexColor("#991b1b")
        }
    }
    cfg = type_configs.get(callout_type.lower(), type_configs["note"])
    
    title_p = Paragraph(f"<b>{cfg['title']}</b>", ParagraphStyle(
        'CalloutTitle',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=cfg['title_color']
    ))
    body_p = Paragraph(md_inline(text_content), ParagraphStyle(
        'CalloutBody',
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#1e293b")
    ))
    
    table = Table([[title_p], [body_p]], colWidths=[width])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), cfg['bg_color']),
        ('LINELEFT', (0, 0), (0, -1), 3.5, cfg['border_color']),
        ('TOPPADDING', (0, 0), (-1, 0), 5),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
        ('TOPPADDING', (0, 1), (-1, 1), 2),
        ('BOTTOMPADDING', (0, 1), (-1, 1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    return table

def parse_callout(line):
    """Extracts callout type and clean text body from markdown blockquote."""
    content = re.sub(r'^>\s*', '', line).strip()
    
    # Check for Practice / Go Practice!
    m_prac = re.match(r'^(?:\*\*(?:Go Practice!?|Practice!?|Practice:?)\*\*|(?:Go Practice!?|Practice!?|Practice:?))\s*(.*)', content, re.IGNORECASE)
    if m_prac:
        return "practice", m_prac.group(1).strip()
    
    # Check for Warning! / Warning: / Warning
    m_warn = re.match(r'^(?:\*\*(?:Warning!?|Warning:?)\*\*|(?:Warning!?|Warning:?))\s*(.*)', content, re.IGNORECASE)
    if m_warn:
        return "warning", m_warn.group(1).strip()
    
    # Check for Tip
    m_tip = re.match(r'^(?:\*\*(?:Tip!?|Tip:?|Pro Tip:?)\*\*|(?:Tip!?|Tip:?|Pro Tip:?))\s*(.*)', content, re.IGNORECASE)
    if m_tip:
        return "tip", m_tip.group(1).strip()
    
    # Check for Note
    m_note = re.match(r'^(?:\*\*(?:Note!?|Note:?)\*\*|(?:Note!?|Note:?))\s*(.*)', content, re.IGNORECASE)
    if m_note:
        return "note", m_note.group(1).strip()
    
    return "note", content

def render_mermaid_diagram(mermaid_code, output_png_path):
    """Renders a Mermaid diagram into a crisp monochrome PNG using mmdc."""
    import subprocess
    import tempfile
    import json
    
    config = {
        "theme": "base",
        "look": "classic",
        "themeVariables": {
            "primaryColor": "#f8fafc",
            "primaryTextColor": "#0f172a",
            "primaryBorderColor": "#1e293b",
            "lineColor": "#334155",
            "edgeLabelBackground": "#ffffff",
            "tertiaryColor": "#ffffff",
            "fontFamily": "Helvetica, Arial, sans-serif",
            "fontSize": "12px"
        }
    }
    
    with tempfile.NamedTemporaryFile('w', suffix='.mmd', delete=False) as f_mmd, \
         tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f_cfg:
        f_mmd.write(mermaid_code)
        f_mmd.flush()
        json.dump(config, f_cfg)
        f_cfg.flush()
        mmd_file = f_mmd.name
        cfg_file = f_cfg.name

    try:
        cmd = [
            "npx", "-y", "@mermaid-js/mermaid-cli",
            "-i", mmd_file,
            "-o", output_png_path,
            "-c", cfg_file,
            "-b", "white",
            "-s", "2"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"[OK] Rendered Mermaid diagram to: {output_png_path}")
        else:
            print(f"[WARN] mmdc render notice: {res.stderr}")
    except Exception as e:
        print(f"[WARN] Failed to render mermaid via mmdc: {e}")
    finally:
        if os.path.exists(mmd_file):
            os.remove(mmd_file)
        if os.path.exists(cfg_file):
            os.remove(cfg_file)

def parse_markdown_to_flowables(md_path, base_dir, styles):
    """Parses markdown text into ReportLab Flowables."""
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    flowables = []
    
    # Typography Styles
    doc_title = ParagraphStyle(
        'TechTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=0,
        spaceAfter=4
    )
    doc_subtitle = ParagraphStyle(
        'TechSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#475569"),
        spaceBefore=0,
        spaceAfter=8
    )
    h1_style = ParagraphStyle(
        'TechH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'TechH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#1e293b"),
        spaceBefore=5,
        spaceAfter=2,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'TechBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#334155"),
        spaceBefore=0,
        spaceAfter=2.5
    )
    caption_style = ParagraphStyle(
        'TechCaption',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#64748b"),
        alignment=TA_CENTER,
        spaceBefore=2,
        spaceAfter=4
    )
    code_box_style = ParagraphStyle(
        'CodeBox',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#0f172a")
    )
    th_style = ParagraphStyle(
        'TableHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )
    tc_key = ParagraphStyle(
        'TableCode',
        parent=styles['Normal'],
        fontName='Courier-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#0f172a")
    )
    tc_action = ParagraphStyle(
        'TableAction',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#1e293b")
    )
    tc_desc = ParagraphStyle(
        'TableDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#334155")
    )

    i = 0
    total = len(lines)
    meta_buffer = []

    while i < total:
        line = lines[i].strip()
        
        # Empty lines
        if not line:
            i += 1
            continue

        # Document Title (# Title)
        if line.startswith("# "):
            title_text = line[2:].strip()
            if ":" in title_text:
                main_t, sub_t = title_text.split(":", 1)
                flowables.append(Paragraph(main_t.strip(), doc_title))
                flowables.append(Paragraph(sub_t.strip(), doc_subtitle))
            else:
                flowables.append(Paragraph(title_text, doc_title))
            i += 1
            continue

        # Metadata bullets (* **Key:** Value)
        if line.startswith("* **") and i < 15:
            meta_buffer.append(line)
            i += 1
            while i < total and lines[i].strip().startswith("* **"):
                meta_buffer.append(lines[i].strip())
                i += 1
            
            row_items = []
            for m in meta_buffer[:3]:
                clean_m = md_inline(re.sub(r'^\*\s*', '', m))
                row_items.append(Paragraph(clean_m, tc_desc))
            while len(row_items) < 3:
                row_items.append(Paragraph("", tc_desc))
            
            meta_t = Table([row_items], colWidths=[175, 175, 154])
            meta_t.setStyle(TableStyle([
                ('LINEBELOW', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
                ('TOPPADDING', (0, 0), (-1, -1), 2),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ]))
            flowables.append(meta_t)
            flowables.append(Spacer(1, 6))
            meta_buffer = []
            continue

        # Section Heading (## ...)
        if line.startswith("## "):
            heading_text = line[3:].strip()
            # Clean layout pagination
            # Page 1: Title, Section 1, Section 2 Step 1 (Fig. 1)
            # Page 2: Step 2 (Fig. 2) + Section 3 (Modal Architecture)
            # Page 3: Section 4 (Navigation) + Section 5 (Editing Operators)
            # Page 4: Section 6 (File Operations) + Section 7 (Next Steps)
            if heading_text.startswith("4.") or heading_text.startswith("6."):
                flowables.append(PageBreak())
            else:
                flowables.append(Spacer(1, 6))
            
            flowables.append(Paragraph(heading_text, h1_style))
            i += 1
            continue

        # Subsection Heading (### ...)
        if line.startswith("### "):
            subhead_text = line[4:].strip()
            # Step 2: Starts Page 2 with 2-column layout
            if "Step 2" in subhead_text:
                flowables.append(PageBreak())
                flowables.append(Paragraph(subhead_text, h2_style))
                i += 1
                
                step2_desc = []
                img2_path = None
                caption2 = "Fig. 2. Extensions Marketplace search results highlighting the official VSCodeVim package."
                
                while i < total and not lines[i].strip().startswith("##") and not lines[i].strip().startswith("---"):
                    cur = lines[i].strip()
                    if cur.startswith("![") and "images/2.png" in cur:
                        img2_path = os.path.join(base_dir, "images", "2.png")
                    elif cur.startswith("*Fig. 2."):
                        caption2 = cur.strip("*_ ")
                    elif cur.startswith(">"):
                        callout_type, callout_text = parse_callout(cur)
                        step2_desc.append((callout_type, callout_text))
                    elif cur:
                        step2_desc.append(("text", cur))
                    i += 1
                
                if img2_path and os.path.exists(img2_path):
                    w2 = 72
                    h2 = int(w2 / (313 / 836))  # ~192 pt
                    im2 = Image(img2_path, width=w2, height=h2)
                    im2_box = Table([[im2]], colWidths=[w2])
                    im2_box.setStyle(TableStyle([
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#94a3b8")),
                        ('LEFTPADDING', (0, 0), (-1, -1), 0),
                        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                        ('TOPPADDING', (0, 0), (-1, -1), 0),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                    ]))
                    
                    right_flowables = []
                    text_accum = []
                    for dtype, dval in step2_desc:
                        if dtype in ("tip", "warning", "note"):
                            if text_accum:
                                right_flowables.append(Paragraph(md_inline(" ".join(text_accum)), body_style))
                                right_flowables.append(Spacer(1, 3))
                                text_accum = []
                            right_flowables.append(make_callout(dval, dtype, width=402))
                            right_flowables.append(Spacer(1, 3))
                        else:
                            text_accum.append(dval)
                    if text_accum:
                        right_flowables.append(Paragraph(md_inline(" ".join(text_accum)), body_style))
                    
                    step2_table = Table([[im2_box, right_flowables]], colWidths=[82, 412])
                    step2_table.setStyle(TableStyle([
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 0),
                        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                        ('TOPPADDING', (0, 0), (-1, -1), 0),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                    ]))
                    flowables.append(KeepTogether([
                        step2_table,
                        Paragraph(caption2, caption_style)
                    ]))
                    flowables.append(Spacer(1, 4))
                continue
            else:
                flowables.append(Paragraph(subhead_text, h2_style))
                i += 1
                continue

        # Horizontal Rule (---)
        if line.startswith("---"):
            i += 1
            continue

        # Image Flowable (![Caption](path))
        img_match = re.match(r'!\[(.*?)\]\((.*?)\)', line)
        if img_match:
            img_caption_raw = img_match.group(1)
            img_rel_path = img_match.group(2)
            full_img_path = os.path.join(base_dir, img_rel_path)
            
            # Check for subsequent caption line, skipping empty lines
            caption_line = img_caption_raw
            lookahead = i + 1
            while lookahead < total and not lines[lookahead].strip():
                lookahead += 1
            if lookahead < total and (lines[lookahead].strip().startswith("*Fig.") or lines[lookahead].strip().startswith("Fig.") or lines[lookahead].strip().startswith("_Fig.")):
                caption_line = lines[lookahead].strip("*_ ")
                i = lookahead
            
            if os.path.exists(full_img_path):
                with PILImage.open(full_img_path) as pimg:
                    orig_w, orig_h = pimg.size
                
                # Scaled width to ensure Step 1 fits cleanly on Page 1
                target_w = 320
                target_h = int(target_w * (orig_h / orig_w))
                im = Image(full_img_path, width=target_w, height=target_h)
                im_box = Table([[im]], colWidths=[target_w])
                im_box.setStyle(TableStyle([
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#94a3b8")),
                    ('LEFTPADDING', (0, 0), (-1, -1), 0),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                    ('TOPPADDING', (0, 0), (-1, -1), 0),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                ]))
                flowables.append(KeepTogether([
                    im_box,
                    Paragraph(caption_line, caption_style)
                ]))
            i += 1
            continue

        # Standalone caption line skip (if not consumed above)
        if line.startswith("*Fig.") or line.startswith("Fig.") or line.startswith("_Fig."):
            i += 1
            continue

        # Callouts (> **Note:** / > **Tip:** / > **Warning:** / > **Go Practice!**)
        if line.startswith(">"):
            callout_type, callout_text = parse_callout(line)
            flowables.append(make_callout(callout_text, callout_type, width=494))
            flowables.append(Spacer(1, 5))
            i += 1
            continue

        # Code block fence (```mermaid ... ``` or ```text ... ```)
        if line.startswith("```"):
            fence_lang = line[3:].strip().lower()
            code_lines = []
            i += 1
            while i < total and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # Skip closing fence
            raw_code = "\n".join(code_lines)

            if fence_lang == "mermaid":
                diag_img_path = os.path.join(base_dir, "images", "3.png")
                # Auto-generate if missing or outdated
                if not os.path.exists(diag_img_path) or os.path.getmtime(diag_img_path) < os.path.getmtime(md_path):
                    render_mermaid_diagram(raw_code, diag_img_path)
                
                # Check for subsequent accompanying text block (ASCII companion for glow)
                lookahead = i
                while lookahead < total and not lines[lookahead].strip():
                    lookahead += 1
                if lookahead < total and lines[lookahead].strip().startswith("```"):
                    # Consume accompanying ASCII text fence so it is not duplicated in PDF
                    lookahead += 1
                    while lookahead < total and not lines[lookahead].strip().startswith("```"):
                        lookahead += 1
                    lookahead += 1
                    i = lookahead
                
                # Check for caption (*Fig. 3. ...*)
                caption3 = "Fig. 3. Vim modal architecture state transitions and keybindings."
                cap_look = i
                while cap_look < total and not lines[cap_look].strip():
                    cap_look += 1
                if cap_look < total and (lines[cap_look].strip().startswith("*Fig.") or lines[cap_look].strip().startswith("Fig.")):
                    caption3 = lines[cap_look].strip("*_ ")
                    i = cap_look + 1
                
                if os.path.exists(diag_img_path):
                    with PILImage.open(diag_img_path) as pimg:
                        diag_w, diag_h = pimg.size
                    target_w = 350
                    target_h = int(target_w * (diag_h / diag_w))
                    im_diag = Image(diag_img_path, width=target_w, height=target_h)
                    diag_box = Table([[im_diag]], colWidths=[target_w])
                    diag_box.setStyle(TableStyle([
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 0),
                        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                        ('TOPPADDING', (0, 0), (-1, -1), 0),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                    ]))
                    flowables.append(KeepTogether([
                        diag_box,
                        Paragraph(caption3, caption_style)
                    ]))
                    flowables.append(Spacer(1, 4))
                continue

            code_elem = Preformatted(raw_code, code_box_style)
            code_table = Table([[code_elem]], colWidths=[494])
            code_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
                ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
                ('TOPPADDING', (0, 0), (-1, -1), 5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
                ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ]))
            flowables.append(KeepTogether([code_table]))
            flowables.append(Spacer(1, 5))
            continue

        # Markdown Table (| Col 1 | Col 2 | ...)
        if line.startswith("|") and line.endswith("|"):
            table_raw_rows = [line]
            i += 1
            while i < total and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                table_raw_rows.append(lines[i].strip())
                i += 1
            
            parsed_rows = []
            for r_idx, raw_r in enumerate(table_raw_rows):
                if re.match(r'^\|(?:\s*:?-+:?\s*\|)+$', raw_r):
                    continue
                cells = [c.strip() for c in raw_r.split("|")[1:-1]]
                if r_idx == 0:
                    parsed_rows.append([Paragraph(md_inline(c), th_style) for c in cells])
                else:
                    row_cells = []
                    for c_idx, c in enumerate(cells):
                        if c_idx == 0 and ("`" in c or len(c) <= 10):
                            row_cells.append(Paragraph(md_inline(c), tc_key))
                        elif c_idx == 1 and len(cells) == 3:
                            row_cells.append(Paragraph(md_inline(c), tc_action))
                        else:
                            row_cells.append(Paragraph(md_inline(c), tc_desc))
                    parsed_rows.append(row_cells)
            
            num_cols = len(parsed_rows[0])
            if num_cols == 3:
                col_w = [80, 110, 304]
            elif num_cols == 2:
                col_w = [180, 314]
            else:
                col_w = [int(494 / num_cols)] * num_cols

            rl_table = Table(parsed_rows, colWidths=col_w)
            rl_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e293b")),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('TOPPADDING', (0, 0), (-1, -1), 3.5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
                ('LEFTPADDING', (0, 0), (-1, -1), 5),
                ('RIGHTPADDING', (0, 0), (-1, -1), 5),
            ]))
            flowables.append(KeepTogether([rl_table]))
            flowables.append(Spacer(1, 5))
            continue

        # Bullet lists and numbered items
        if line.startswith("* ") or re.match(r'^\d+\.\s', line):
            clean_li = md_inline(re.sub(r'^(?:\*\s|\d+\.\s)', '', line))
            if re.match(r'^\d+\.\s', line):
                prefix = re.match(r'^(\d+\.)\s', line).group(1) + " "
                clean_li = f"<b>{prefix}</b>" + clean_li
            flowables.append(Paragraph(f"&bull; {clean_li}" if line.startswith("* ") else clean_li, body_style))
            i += 1
            continue

        # Standard Paragraph: aggregate consecutive lines until blank line or block element
        para_lines = [line]
        i += 1
        while i < total:
            next_l = lines[i].strip()
            if not next_l or next_l.startswith("#") or next_l.startswith(">") or next_l.startswith("```") or next_l.startswith("|") or next_l.startswith("* ") or re.match(r'^\d+\.\s', next_l) or next_l.startswith("![") or next_l.startswith("---") or next_l.startswith("*Fig.") or next_l.startswith("Fig."):
                break
            para_lines.append(next_l)
            i += 1
        flowables.append(Paragraph(md_inline(" ".join(para_lines)), body_style))
        flowables.append(Spacer(1, 4))
        continue

    return flowables

def build_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, "document.md")
    output_pdf_path = os.path.join(base_dir, "document.pdf")

    if not os.path.exists(md_path):
        print(f"[FAIL] Source markdown file not found: {md_path}")
        return

    # Dynamically extract document title & subtitle for running headers
    with open(md_path, 'r', encoding='utf-8') as f:
        for line in f:
            line_str = line.strip()
            if line_str.startswith("# "):
                full_t = line_str[2:].strip()
                if ":" in full_t:
                    t_parts = full_t.split(":", 1)
                    TechnicalDocCanvas.doc_title = t_parts[0].strip()
                    TechnicalDocCanvas.doc_subtitle = t_parts[1].strip()
                else:
                    TechnicalDocCanvas.doc_title = full_t
                    TechnicalDocCanvas.doc_subtitle = ""
                break

    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    flowables = parse_markdown_to_flowables(md_path, base_dir, styles)

    doc.build(flowables, canvasmaker=TechnicalDocCanvas)
    print(f"[OK] Successfully built: {output_pdf_path}")

if __name__ == "__main__":
    build_pdf()
