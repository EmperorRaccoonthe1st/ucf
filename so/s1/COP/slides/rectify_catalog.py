#!/usr/bin/env python3
"""
rectify_catalog.py
==================
Forensic rectification of missing_code_snippets_catalog.json:
1. Filters out false-positive injections (bullet lists, title fragments, prose).
2. Snaps all code container bounding boxes to exact PDF vector shapes (0 white slivers).
3. Restores missing top-level declarations (package, class, imports) truncated by text clustering.
4. Eliminates contaminated text from adjacent explanation columns.
"""

import os
import json
import re
import html
import pypdf
import subprocess

BASE_DIR = "/home/owen/ucf/so/s1/COP/slides"
CATALOG_PATH = os.path.join(BASE_DIR, "missing_code_snippets_catalog.json")

def get_page_vector_boxes(pdf_path, page_num):
    reader = pypdf.PdfReader(pdf_path)
    if page_num > len(reader.pages):
        return []
    page = reader.pages[page_num - 1]
    content = page.get_contents()
    if isinstance(content, list):
        data = b''.join(c.get_data() for c in content).decode('latin1', errors='ignore')
    elif content is not None:
        data = content.get_data().decode('latin1', errors='ignore')
    else:
        return []
    rects = re.findall(r'([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+re', data)
    boxes = []
    seen = set()
    for x, y, w, h in rects:
        x, y, w, h = float(x), float(y), float(w), float(h)
        if w >= 940 and h >= 520:
            continue
        if w < 40 or h < 30:
            continue
        top = 540.0 - (y + h)
        rx = round(x / 960.0, 4)
        ry = round(top / 540.0, 4)
        rw = round(w / 960.0, 4)
        rh = round(h / 540.0, 4)
        k = (round(rx, 2), round(ry, 2), round(rw, 2), round(rh, 2))
        if k not in seen:
            seen.add(k)
            boxes.append({'rx': rx, 'ry': ry, 'rw': rw, 'rh': rh})
    return boxes

def get_page_lines(pdf_path, page_num):
    cmd = ['pdftotext', '-f', str(page_num), '-l', str(page_num), '-bbox-layout', pdf_path, '-']
    xml = subprocess.check_output(cmd).decode('utf-8', errors='ignore')
    line_matches = re.findall(r'<line xMin=\"([0-9.]+)\" yMin=\"([0-9.]+)\" xMax=\"([0-9.]+)\" yMax=\"([0-9.]+)\">(.*?)</line>', xml, re.DOTALL)
    lines = []
    for x1, y1, x2, y2, content in line_matches:
        words = re.findall(r'<word[^>]*>(.*?)</word>', content)
        text = ' '.join(words).strip()
        text = html.unescape(text)
        if text:
            lx = (float(x1) + float(x2)) / 2.0 / 960.0
            ly = (float(y1) + float(y2)) / 2.0 / 540.0
            lines.append((ly, lx, text))
    return lines

def is_false_positive(code_text):
    lines = [l.strip() for l in code_text.split('\n') if l.strip()]
    if not lines:
        return True
    has_bullets = any(l.startswith('•') or l.startswith('–') or l.startswith('\u2022') or l.startswith('\u2013') for l in lines)
    semi_count = code_text.count(';')
    brace_count = code_text.count('{') + code_text.count('}')
    
    # Bullet list with minimal code (e.g. imports lecture, explanation bullets)
    if has_bullets and semi_count <= 1:
        return True
    # Pure text without code syntax
    if semi_count == 0 and brace_count == 0 and not any(kw in code_text for kw in ['class ', 'void ', 'int ', 'double ', 'boolean ']):
        return True
    return False

def main():
    with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Backup original
    bak_path = CATALOG_PATH + ".bak"
    if not os.path.exists(bak_path):
        with open(bak_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    inventory = data.get('inventory', [])
    print(f"Loaded {len(inventory)} items from catalog.")

    rectified = []
    dropped_fp = 0
    snapped = 0
    headers_fixed = 0

    for it in inventory:
        deck = it['deck']
        page = it['page']
        code = it['code_text']
        bbox = it['bbox_rel']
        pdf_path = os.path.join(BASE_DIR, deck)

        # 1. Filter false positives
        if is_false_positive(code):
            dropped_fp += 1
            print(f"[DROPPED FP] {deck} p{page}: {code.replace(chr(10), ' ')[:60]}")
            continue

        # 2. Vector shape snapping
        vboxes = []
        if os.path.exists(pdf_path):
            try:
                vboxes = get_page_vector_boxes(pdf_path, page)
            except Exception:
                vboxes = []

        best_v = None
        best_iou = 0.0
        bx1, by1, bx2, by2 = bbox['rx'], bbox['ry'], bbox['rx'] + bbox['rw'], bbox['ry'] + bbox['rh']
        bcx, bcy = (bx1 + bx2) / 2.0, (by1 + by2) / 2.0

        for vb in vboxes:
            vx1, vy1, vx2, vy2 = vb['rx'], vb['ry'], vb['rx'] + vb['rw'], vb['ry'] + vb['rh']
            ix1, iy1 = max(bx1, vx1), max(by1, vy1)
            ix2, iy2 = min(bx2, vx2), min(by2, vy2)
            if ix2 > ix1 and iy2 > iy1:
                inter = (ix2 - ix1) * (iy2 - iy1)
                union = (bx2 - bx1)*(by2 - by1) + (vx2 - vx1)*(vy2 - vy1) - inter
                iou = inter / union if union > 0 else 0
                if iou > best_iou:
                    best_iou = iou
                    best_v = vb
            elif vx1 <= bcx <= vx2 and vy1 <= bcy <= vy2:
                best_v = vb
                best_iou = 0.5

        if best_v and (best_iou > 0.25 or (best_v['rx'] <= bcx <= best_v['rx'] + best_v['rw'])):
            snapped += 1
            it['bbox_rel'] = dict(best_v)

            # Re-extract lines cleanly bounded inside vector shape
            try:
                plines = get_page_lines(pdf_path, page)
                # Keep margin tolerance of 0.015 for sub-pixel text positioning
                box_lines = [
                    l[2] for l in plines
                    if (best_v['rx'] - 0.015 <= l[1] <= best_v['rx'] + best_v['rw'] + 0.015)
                    and (best_v['ry'] - 0.015 <= l[0] <= best_v['ry'] + best_v['rh'] + 0.015)
                ]
                if len(box_lines) >= 2:
                    new_code = '\n'.join(box_lines)
                    # Filter out any stray bullet lines that might be inside
                    filtered_lines = [l for l in box_lines if not (l.startswith('•') and len(l) > 30 and ';' not in l)]
                    if len(filtered_lines) >= 2:
                        new_code = '\n'.join(filtered_lines)
                    
                    if ('class ' in new_code and 'class ' not in code) or ('package ' in new_code and 'package ' not in code):
                        headers_fixed += 1
                        print(f"[HEADER RESTORED] {deck} p{page}: added class/package header!")
                    it['code_text'] = new_code
            except Exception as e:
                print(f"[WARN] Error re-extracting lines for {deck} p{page}: {e}")

        rectified.append(it)

    data['inventory'] = rectified
    with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print("\n" + "="*60)
    print("CATALOG RECTIFICATION COMPLETE")
    print("="*60)
    print(f"False Positives Dropped: {dropped_fp}")
    print(f"Snapped Vector Boxes:    {snapped}")
    print(f"Missing Headers Restored:{headers_fixed}")
    print(f"Total Active Containers: {len(rectified)}")
    print("="*60)

if __name__ == '__main__':
    main()
