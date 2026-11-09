#!/usr/bin/env python3
"""
find_all_code_blocks.py

Systematic analysis script to detect and classify code blocks across all 25 decks.
"""

import json
import re

with open('/tmp/all_deck_raw_data.json') as f:
    all_data = json.load(f)

JAVA_KEYWORDS = {
    'public', 'private', 'protected', 'class', 'static', 'void', 'int', 'double', 'float',
    'boolean', 'char', 'long', 'short', 'byte', 'String', 'new', 'return', 'import', 'package',
    'extends', 'implements', 'if', 'else', 'for', 'while', 'do', 'switch', 'case', 'break',
    'continue', 'try', 'catch', 'finally', 'throw', 'throws', 'super', 'this', 'instanceof',
    'enum', 'interface', 'abstract', 'final', 'default', 'null', 'true', 'false'
}

JAVA_INDICATORS = [
    r'System\s*\.\s*out\s*\.\s*print',
    r'public\s+class\b',
    r'public\s+static\s+void\s+main\b',
    r'public\s+(?:int|void|boolean|String|double|float)\b',
    r'private\s+(?:int|void|boolean|String|double|float|Node)\b',
    r'ArrayList\s*<',
    r'new\s+[A-Z]\w*\(',
    r'for\s*\(',
    r'while\s*\(',
    r'try\s*\{',
    r'catch\s*\(',
    r'import\s+java\.',
    r'package\s+\w+'
]

def is_code_line(text):
    text_s = text.strip()
    if not text_s:
        return False
    # Check if ends with ; or { or }
    if text_s.endswith(';') or text_s.endswith('{') or text_s.endswith('}'):
        return True
    if text_s.startswith('//') or text_s.startswith('/*') or text_s.endswith('*/') or text_s.startswith('*'):
        # Comment line
        return True
    # Check regex indicators
    for ind in JAVA_INDICATORS:
        if re.search(ind, text_s):
            return True
    # Check keywords count
    words = re.findall(r'\b[A-Za-z_]\w*\b', text_s)
    kw_count = sum(1 for w in words if w in JAVA_KEYWORDS)
    if kw_count >= 2 and any(c in text_s for c in '()[]={};<>'):
        return True
    return False

def analyze_page(page):
    p_num = page['page_num']
    pw = page['page_width']
    ph = page['page_height']
    title = page['title']
    elements = page['text_elements']

    if not elements:
        return None

    # Group elements into lines based on vertical proximity (within 6px)
    elements_sorted = sorted(elements, key=lambda e: (e['top'], e['left']))
    lines = []
    for el in elements_sorted:
        if not lines or abs(el['top'] - lines[-1]['top']) > 6:
            lines.append({
                'top': el['top'],
                'bottom': el['top'] + el['height'],
                'left': el['left'],
                'right': el['left'] + el['width'],
                'height': el['height'],
                'elements': [el],
                'text': el['text']
            })
        else:
            # same line
            last = lines[-1]
            last['right'] = max(last['right'], el['left'] + el['width'])
            last['height'] = max(last['height'], el['height'])
            last['bottom'] = max(last['bottom'], el['top'] + el['height'])
            last['elements'].append(el)
            # Add space if there is a horizontal gap
            gap = el['left'] - (last['elements'][-2]['left'] + last['elements'][-2]['width'])
            if gap > 3:
                last['text'] += ' ' + el['text']
            else:
                last['text'] += el['text']

    # Filter out title line(s)
    body_lines = [l for l in lines if l['top'] > ph * 0.12]

    # Evaluate lines for code
    code_lines = []
    for l in body_lines:
        c_flag = is_code_line(l['text'])
        code_lines.append((l, c_flag))

    # Cluster code lines into blocks
    # A code block is a sequence of consecutive or nearby code lines (vertical gap < 45px)
    blocks = []
    curr_block = []
    for l, is_c in code_lines:
        if is_c:
            if not curr_block:
                curr_block.append(l)
            else:
                gap = l['top'] - curr_block[-1]['bottom']
                if gap < 45:
                    curr_block.append(l)
                else:
                    if len(curr_block) >= 2:
                        blocks.append(curr_block)
                    curr_block = [l]
        else:
            # If line is NOT code, could it be part of the block? (e.g. an inner print or blank)
            if curr_block:
                gap = l['top'] - curr_block[-1]['bottom']
                # If gap is small and has indentation or braces
                if gap < 35 and ('{' in l['text'] or '}' in l['text'] or l['left'] > pw * 0.1):
                    # Check if next line is code
                    curr_block.append(l)
                else:
                    if len(curr_block) >= 2:
                        blocks.append(curr_block)
                    curr_block = []
    if len(curr_block) >= 2:
        blocks.append(curr_block)

    return {
        'page_num': p_num,
        'title': title,
        'blocks': blocks,
        'all_lines': lines
    }

deck_summary = {}
for deck_name, pages in all_data.items():
    code_pages = []
    for p in pages:
        res = analyze_page(p)
        if res and res['blocks']:
            # Count total code lines
            tot_lines = sum(len(b) for b in res['blocks'])
            # Filter: we want multi-line code snippets (at least 3 lines or a clear class/method/statement)
            if tot_lines >= 3 or any('public class' in ' '.join(l['text'] for l in b) for b in res['blocks']):
                code_pages.append(res)
    deck_summary[deck_name] = code_pages
    print(f"{deck_name}: {len(code_pages)} slides with code blocks (pages: {[p['page_num'] for p in code_pages]})")

