#!/usr/bin/env python3
"""
catalog_all_snippets.py

Deep forensic auditor for all code snippets across all 25 lecture decks.
Dumps a comprehensive JSON file containing:
  - Deck name
  - Page number
  - Slide title
  - Detected code blocks with:
      * Exact code text (with proper Java indentation)
      * Bounding box: relative (rx, ry, rw, rh) and absolute pt (x, y, w, h)
      * Layout classification (Single Box, Multi-Box, Mixed Code + Output, Adjacent)
      * Injection status: ALREADY_INJECTED vs MISSING_INJECTION
      * Line count and font details
"""

import json
import re
import os

with open('/tmp/all_deck_raw_data.json') as f:
    all_data = json.load(f)

ALREADY_INJECTED_MAP = {
    ('Slide02_JavaBasics.pdf', 4): "FirstJavaProgram class with header comment",
    ('bufferProblem.pdf', 3): "Scanner buffer problem test",
    ('Slide03_JavaBasics2.pdf', 20): "Typecasting examples (int and float)",
    ('Slide04_Methods.pdf', 7): "max method implementation",
    ('Slide06_ArraysInJava.pdf', 9): "1D array traversal (standard & enhanced for)",
    ('Slide06_ArraysInJava.pdf', 11): "2D array matrix traversal nested loops",
    ('Slide12_InheritancePart1.pdf', 4): "4-Quadrant Car & Vehicle inheritance",
    ('Slide13_InheritancePart2.pdf', 4): "instanceof polymorphic test",
    ('Slide16_Java_File_Operations.pdf', 6): "WriteFile method with BufferedWriter",
    ('Slide19_Linked_Lists.pdf', 6): "LinkedList class definition",
    ('Slide22_Exceptions.pdf', 8): "Multi-catch exception handling"
}

JAVA_KEYWORDS = {
    'public', 'private', 'protected', 'class', 'static', 'void', 'int', 'double', 'float',
    'boolean', 'char', 'long', 'short', 'byte', 'String', 'new', 'return', 'import', 'package',
    'extends', 'implements', 'if', 'else', 'for', 'while', 'do', 'switch', 'case', 'break',
    'continue', 'try', 'catch', 'finally', 'throw', 'throws', 'super', 'this', 'instanceof',
    'enum', 'interface', 'abstract', 'final', 'default', 'null', 'true', 'false', 'Scanner',
    'ArrayList', 'LinkedList', 'Iterator', 'System.out.println', 'System.out.print'
}

def clean_text(txt):
    return txt.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"').replace('&#34;', '"')

def is_code_line(text):
    text_s = text.strip()
    if not text_s:
        return False
    # Definite code endings
    if text_s.endswith(';') or text_s.endswith('{') or text_s.endswith('}'):
        return True
    if text_s.startswith('//') or text_s.startswith('/*') or text_s.endswith('*/') or text_s.startswith('*'):
        return True
    # Method signatures / calls
    if re.search(r'\b(public|private|protected|static|void|class|interface|enum|extends|implements)\b', text_s):
        return True
    if re.search(r'\b(System\s*\.\s*out\s*\.\s*print|Scanner|ArrayList|new\s+[A-Z]\w*|import\s+java|package\s+\w+)', text_s):
        return True
    if re.search(r'\b(if|for|while|switch|catch)\s*\(', text_s):
        return True
    if re.search(r'\b(int|double|float|boolean|String|char|long)\s+[a-zA-Z_]\w*\s*=', text_s):
        return True
    # High density of keywords or code symbols
    words = re.findall(r'\b[A-Za-z_]\w*\b', text_s)
    kw_count = sum(1 for w in words if w in JAVA_KEYWORDS)
    if kw_count >= 2 and any(c in text_s for c in '=();<>[]+-*/'):
        return True
    return False

def is_output_text(text):
    # Detect console output statements like "Hi Class!", "[1, 2, 3]", "Output: ...", numbers
    text_s = text.strip()
    if re.match(r'^\[.*\]$', text_s):
        return True
    if text_s.startswith('Output:') or text_s.startswith('output:'):
        return True
    return False

def cluster_lines(page):
    pw = page['page_width']
    ph = page['page_height']
    elements = page['text_elements']
    if not elements:
        return []

    elements_sorted = sorted(elements, key=lambda e: (e['top'], e['left']))
    raw_lines = []
    for el in elements_sorted:
        t = clean_text(el['text'])
        if not raw_lines or abs(el['top'] - raw_lines[-1]['top']) > 7:
            raw_lines.append({
                'top': el['top'],
                'bottom': el['top'] + el['height'],
                'left': el['left'],
                'right': el['left'] + el['width'],
                'height': el['height'],
                'elements': [el],
                'text': t
            })
        else:
            last = raw_lines[-1]
            last['right'] = max(last['right'], el['left'] + el['width'])
            last['height'] = max(last['height'], el['height'])
            last['bottom'] = max(last['bottom'], el['top'] + el['height'])
            last['elements'].append(el)
            gap = el['left'] - (last['elements'][-2]['left'] + last['elements'][-2]['width'])
            if gap > 3:
                last['text'] += ' ' + t
            else:
                last['text'] += t

    # Exclude title lines (top 12% of slide)
    body_lines = [l for l in raw_lines if l['top'] > ph * 0.11]
    return body_lines

def extract_code_blocks_from_page(deck_name, page):
    p_num = page['page_num']
    pw = page['page_width']
    ph = page['page_height']
    title = clean_text(page['title'])
    lines = cluster_lines(page)

    if not lines:
        return []

    # Check horizontal splitting (e.g. multi-column layouts like Left code, Right code or Left code, Right output/notes)
    # Group lines by horizontal column:
    # Check if lines naturally separate into left (< 0.55 pw) vs right (> 0.45 pw)
    left_lines = [l for l in lines if l['left'] < pw * 0.52 and l['right'] < pw * 0.70]
    right_lines = [l for l in lines if l['left'] >= pw * 0.45]
    wide_lines = [l for l in lines if l['left'] < pw * 0.45 and l['right'] >= pw * 0.70]

    columns = []
    if wide_lines or (not left_lines and not right_lines):
        # Single full-width layout
        columns = [lines]
    elif left_lines and right_lines:
        columns = [left_lines, right_lines]
    elif left_lines:
        columns = [left_lines]
    else:
        columns = [right_lines]

    detected_blocks = []

    for col in columns:
        curr_block = []
        for l in col:
            c_flag = is_code_line(l['text'])
            if c_flag:
                if not curr_block:
                    curr_block.append(l)
                else:
                    gap = l['top'] - curr_block[-1]['bottom']
                    if gap < 50:
                        curr_block.append(l)
                    else:
                        if len(curr_block) >= 3 or (len(curr_block) >= 2 and any(';' in x['text'] or '{' in x['text'] for x in curr_block)):
                            detected_blocks.append(curr_block)
                        curr_block = [l]
            else:
                # If non-code line is inside a code block (like a short variable name, bracket, or output)
                if curr_block:
                    gap = l['top'] - curr_block[-1]['bottom']
                    # If gap is small and text looks like code continuation or closing brace
                    if gap < 35 and ('{' in l['text'] or '}' in l['text'] or l['text'].strip().endswith(';') or l['text'].strip() in [')', '}', '{', '};']):
                        curr_block.append(l)
                    else:
                        if len(curr_block) >= 3 or (len(curr_block) >= 2 and any(';' in x['text'] or '{' in x['text'] for x in curr_block)):
                            detected_blocks.append(curr_block)
                        curr_block = []
        if len(curr_block) >= 3 or (len(curr_block) >= 2 and any(';' in x['text'] or '{' in x['text'] for x in curr_block)):
            detected_blocks.append(curr_block)

    # Refine detected blocks:
    # Filter out blocks that are just bullet text or lists of words without code structure
    valid_blocks = []
    for b in detected_blocks:
        code_str = '\n'.join([l['text'] for l in b])
        # Must have at least 2 code indicators: semicolon, curly brace, or keyword
        has_semi = code_str.count(';') >= 1
        has_brace = '{' in code_str or '}' in code_str
        has_kw = any(re.search(r'\b' + kw + r'\b', code_str) for kw in ['public', 'class', 'void', 'int', 'String', 'for', 'while', 'if', 'System.out', 'Scanner', 'ArrayList', 'Node', 'try', 'catch', 'import', 'package'])
        
        # Check if block is at least 2 lines and has programming structure
        if len(b) >= 2 and ((has_semi and (has_kw or has_brace)) or (has_kw and has_brace)):
            # Calculate bounding box
            min_x = min(l['left'] for l in b)
            min_y = min(l['top'] for l in b)
            max_x = max(l['right'] for l in b)
            max_y = max(l['bottom'] for l in b)

            # Add padding
            pad_x = 10
            pad_y = 10
            bx = max(0, min_x - pad_x)
            by = max(0, min_y - pad_y)
            bw = min(pw - bx, (max_x - min_x) + 2 * pad_x)
            bh = min(ph - by, (max_y - min_y) + 2 * pad_y)

            rx = round(bx / pw, 3)
            ry = round(by / ph, 3)
            rw = round(bw / pw, 3)
            rh = round(bh / ph, 3)

            valid_blocks.append({
                'lines': [l['text'] for l in b],
                'code_text': code_str,
                'bbox_pt': {'x': round(bx, 1), 'y': round(by, 1), 'w': round(bw, 1), 'h': round(bh, 1)},
                'bbox_rel': {'rx': rx, 'ry': ry, 'rw': rw, 'rh': rh},
                'line_count': len(b)
            })

    if not valid_blocks:
        return []

    # Determine layout classification
    # Check if there is terminal output on the slide
    has_output = any(is_output_text(l['text']) for l in lines)
    if len(valid_blocks) == 1:
        layout = "Mixed Code + Output" if has_output else "Single Box"
    elif len(valid_blocks) >= 2:
        layout = "Multi-Box"
    else:
        layout = "Single Box"

    status = "ALREADY_INJECTED" if (deck_name, p_num) in ALREADY_INJECTED_MAP else "MISSING_INJECTION"

    return [{
        'deck': deck_name,
        'page': p_num,
        'title': title,
        'layout': layout,
        'status': status,
        'block_index': idx + 1,
        'total_blocks_on_slide': len(valid_blocks),
        'code_text': vb['code_text'],
        'bbox_pt': vb['bbox_pt'],
        'bbox_rel': vb['bbox_rel'],
        'line_count': vb['line_count']
    } for idx, vb in enumerate(valid_blocks)]

if __name__ == '__main__':
    all_snippets = []
    deck_stats = {}

    for deck_name in all_data:
        deck_snippets = []
        for p in all_data[deck_name]:
            snips = extract_code_blocks_from_page(deck_name, p)
            if snips:
                deck_snippets.extend(snips)
        all_snippets.extend(deck_snippets)

        pages_with_code = sorted(list(set(s['page'] for s in deck_snippets)))
        injected = [p for p in pages_with_code if (deck_name, p) in ALREADY_INJECTED_MAP]
        missing = [p for p in pages_with_code if (deck_name, p) not in ALREADY_INJECTED_MAP]

        deck_stats[deck_name] = {
            'total_code_slides': len(pages_with_code),
            'total_snippets': len(deck_snippets),
            'injected_pages': injected,
            'missing_pages': missing
        }
        print(f"{deck_name}: {len(pages_with_code)} code slides ({len(deck_snippets)} snippets) | Injected: {len(injected)} | Missing: {len(missing)}")

    print("\n" + "="*50)
    total_slides = sum(s['total_code_slides'] for s in deck_stats.values())
    total_snips = sum(s['total_snippets'] for s in deck_stats.values())
    total_injected = sum(len(s['injected_pages']) for s in deck_stats.values())
    total_missing = sum(len(s['missing_pages']) for s in deck_stats.values())
    print(f"TOTAL CODE SLIDES: {total_slides}")
    print(f"TOTAL CODE SNIPPETS: {total_snips}")
    print(f"TOTAL ALREADY INJECTED: {total_injected}")
    print(f"TOTAL MISSING INJECTION: {total_missing}")

    with open('/tmp/all_cataloged_code_snippets.json', 'w') as f:
        json.dump({
            'deck_stats': deck_stats,
            'snippets': all_snippets
        }, f, indent=2)
    print("Catalog saved to /tmp/all_cataloged_code_snippets.json")
