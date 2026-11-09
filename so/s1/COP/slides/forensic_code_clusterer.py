#!/usr/bin/env python3
"""
forensic_code_clusterer.py

Refined Column & Quadrant-aware forensic code container clustering.
"""

import os
import json
import re

with open('/tmp/all_deck_raw_data.json') as f:
    all_data = json.load(f)

ALREADY_INJECTED = {
    ('Slide02_JavaBasics.pdf', 4),
    ('bufferProblem.pdf', 3),
    ('Slide03_JavaBasics2.pdf', 20),
    ('Slide04_Methods.pdf', 7),
    ('Slide06_ArraysInJava.pdf', 9),
    ('Slide06_ArraysInJava.pdf', 11),
    ('Slide12_InheritancePart1.pdf', 4),
    ('Slide13_InheritancePart2.pdf', 4),
    ('Slide16_Java_File_Operations.pdf', 6),
    ('Slide19_Linked_Lists.pdf', 6),
    ('Slide22_Exceptions.pdf', 8)
}

JAVA_KEYWORDS = {
    'public', 'private', 'protected', 'class', 'static', 'void', 'int', 'double', 'float',
    'boolean', 'char', 'long', 'short', 'byte', 'String', 'new', 'return', 'import', 'package',
    'extends', 'implements', 'if', 'else', 'for', 'while', 'do', 'switch', 'case', 'break',
    'continue', 'try', 'catch', 'finally', 'throw', 'throws', 'super', 'this', 'instanceof',
    'enum', 'interface', 'abstract', 'final', 'default', 'null', 'true', 'false', 'Scanner',
    'ArrayList', 'LinkedList', 'Iterator', 'System.out.println', 'System.out.print', 'System.out.printf'
}

def clean_text(txt):
    return txt.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"').replace('&#34;', '"')

def is_code_line(text):
    s = text.strip()
    if not s:
        return False
    # If starts with bullet point • and not an import
    if s.startswith('•') and not 'import ' in s and not 'System.out' in s:
        # Check if it's purely bullet description
        words = s.split()
        if len(words) > 3 and not any(c in s for c in ';{}='):
            return False
    if s.endswith(';') or s.endswith('{') or s.endswith('}'):
        return True
    if s.startswith('//') or s.startswith('/*') or s.endswith('*/') or s.startswith('*'):
        return True
    if re.search(r'\b(public|private|protected|static|void|class|interface|enum|extends|implements)\b', s):
        return True
    if re.search(r'\b(System\s*\.\s*out\s*\.\s*print|Scanner|ArrayList|new\s+[A-Z]\w*|import\s+java|package\s+\w+)', s):
        return True
    if re.search(r'\b(if|for|while|switch|catch)\s*\(', s):
        return True
    if re.search(r'\b(int|double|float|boolean|String|char|long)\s+[a-zA-Z_]\w*\s*=', s):
        return True
    words = re.findall(r'\b[A-Za-z_]\w*\b', s)
    kw_count = sum(1 for w in words if w in JAVA_KEYWORDS)
    if kw_count >= 2 and any(c in s for c in '=();<>[]+-*/'):
        return True
    return False

def is_output_line(text):
    s = text.strip()
    if not s:
        return False
    if re.match(r'^\[.*\]$', s):
        return True
    if s.startswith('Output:') or s.startswith('output:'):
        return True
    if s.startswith('error:') or 'Exception in thread' in s:
        return True
    return False

def reconstruct_visual_lines(elements, pw, ph):
    els = sorted(elements, key=lambda e: (e['top'], e['left']))
    lines = []
    for el in els:
        t = clean_text(el['text'])
        matched = None
        for l in lines:
            if abs(el['top'] - l['top']) <= 6:
                gap = el['left'] - l['right']
                if 0 <= gap < 40:
                    matched = l
                    break
        if matched:
            matched['right'] = max(matched['right'], el['left'] + el['width'])
            matched['bottom'] = max(matched['bottom'], el['top'] + el['height'])
            matched['text'] += ' ' + t
            matched['els'].append(el)
        else:
            lines.append({
                'top': el['top'],
                'bottom': el['top'] + el['height'],
                'left': el['left'],
                'right': el['left'] + el['width'],
                'text': t,
                'els': [el]
            })
    return lines

def cluster_code_containers(lines, pw, ph):
    """
    Column & Region aware clustering.
    Identifies if a slide has:
    1. Single code container (full slide or one column)
    2. Multi-column code containers
    3. 4-quadrant containers
    """
    body_lines = [l for l in lines if l['top'] > ph * 0.11]
    if not body_lines:
        return []

    for l in body_lines:
        l['is_code'] = is_code_line(l['text'])
        l['is_output'] = is_output_line(l['text'])

    code_lines = [l for l in body_lines if l['is_code']]
    if not code_lines:
        return []

    # Check horizontal column boundaries
    # Are there multiple distinct columns of code?
    # Check if lines have left < pw*0.48 vs left > pw*0.48
    col_left = [l for l in code_lines if l['right'] < pw * 0.52]
    col_right = [l for l in code_lines if l['left'] > pw * 0.46]
    col_wide = [l for l in code_lines if l['left'] < pw * 0.46 and l['right'] > pw * 0.52]

    # Partition lines into column groups
    if col_wide or (not col_left and not col_right):
        # Single column / full width
        column_groups = [code_lines]
    elif col_left and col_right:
        column_groups = [col_left, col_right]
    elif col_left:
        column_groups = [col_left]
    else:
        column_groups = [col_right]

    containers = []

    for cgroup in column_groups:
        # Within each column, check if it's a single container or multiple vertically stacked boxes
        # (e.g. Car vs go() in left column of Slide12 p4, or multiple independent functions)
        # Sort lines by top
        cgroup_sorted = sorted(cgroup, key=lambda l: l['top'])
        
        # Check vertical clustering
        curr_box = []
        for l in cgroup_sorted:
            if not curr_box:
                curr_box.append(l)
            else:
                v_gap = l['top'] - curr_box[-1]['bottom']
                # If gap is moderate (< 85px) and no class declaration resetting context
                is_new_class = re.match(r'^(public\s+)?class\s+\w+', l['text'].strip()) or re.match(r'^package\s+\w+', l['text'].strip())
                # If there is a new class declaration and vertical gap > 35px, start new box
                if is_new_class and v_gap > 35 and len(curr_box) >= 4:
                    containers.append(curr_box)
                    curr_box = [l]
                elif v_gap <= 85:
                    curr_box.append(l)
                else:
                    if len(curr_box) >= 2:
                        containers.append(curr_box)
                    curr_box = [l]
        if len(curr_box) >= 2:
            containers.append(curr_box)

    # Format containers
    final_containers = []
    for comp in containers:
        comp_sorted = sorted(comp, key=lambda l: (l['top'], l['left']))
        code_str = '\n'.join([l['text'] for l in comp_sorted])

        semi_count = code_str.count(';')
        brace_count = code_str.count('{') + code_str.count('}')
        kw_hits = [kw for kw in JAVA_KEYWORDS if re.search(r'\b' + re.escape(kw) + r'\b', code_str)]

        # Must have at least 2 lines and genuine code structure
        if len(comp_sorted) >= 2 and (semi_count >= 1 or brace_count >= 1 or len(kw_hits) >= 2):
            min_x = min(l['left'] for l in comp_sorted)
            min_y = min(l['top'] for l in comp_sorted)
            max_x = max(l['right'] for l in comp_sorted)
            max_y = max(l['bottom'] for l in comp_sorted)

            pad_x = 12
            pad_y = 12
            bx = max(0, min_x - pad_x)
            by = max(0, min_y - pad_y)
            bw = min(pw - bx, (max_x - min_x) + 2 * pad_x)
            bh = min(ph - by, (max_y - min_y) + 2 * pad_y)

            final_containers.append({
                'lines': [l['text'] for l in comp_sorted],
                'code_text': code_str,
                'min_x': min_x, 'min_y': min_y, 'max_x': max_x, 'max_y': max_y,
                'bbox_pt': {'x': round(bx, 1), 'y': round(by, 1), 'w': round(bw, 1), 'h': round(bh, 1)},
                'bbox_rel': {
                    'rx': round(bx / pw, 3),
                    'ry': round(by / ph, 3),
                    'rw': round(bw / pw, 3),
                    'rh': round(bh / ph, 3)
                },
                'line_count': len(comp_sorted)
            })

    final_containers.sort(key=lambda c: (c['bbox_pt']['y'], c['bbox_pt']['x']))
    return final_containers

def run():
    all_results = []
    deck_stats = {}

    for deck_name, pages in all_data.items():
        deck_containers = []
        for p in pages:
            p_num = p['page_num']
            pw, ph = p['page_width'], p['page_height']
            title = clean_text(p['title'])

            lines = reconstruct_visual_lines(p['text_elements'], pw, ph)
            containers = cluster_code_containers(lines, pw, ph)

            if not containers:
                continue

            # Determine layout
            has_output = any(is_output_line(l['text']) for l in lines)
            layout = "Multi-Box" if len(containers) > 1 else ("Mixed Code + Output" if has_output else "Single Box")
            status = "ALREADY_INJECTED" if (deck_name, p_num) in ALREADY_INJECTED else "MISSING_INJECTION"

            for idx, c in enumerate(containers):
                deck_containers.append({
                    'deck': deck_name,
                    'page': p_num,
                    'title': title,
                    'layout': layout,
                    'status': status,
                    'container_index': idx + 1,
                    'total_containers_on_slide': len(containers),
                    'code_text': c['code_text'],
                    'bbox_pt': c['bbox_pt'],
                    'bbox_rel': c['bbox_rel'],
                    'line_count': c['line_count']
                })

        all_results.extend(deck_containers)
        pages_with_code = sorted(list(set(c['page'] for c in deck_containers)))
        injected = [p for p in pages_with_code if (deck_name, p) in ALREADY_INJECTED]
        missing = [p for p in pages_with_code if (deck_name, p) not in ALREADY_INJECTED]

        deck_stats[deck_name] = {
            'total_code_slides': len(pages_with_code),
            'total_containers': len(deck_containers),
            'injected_pages': injected,
            'missing_pages': missing
        }
        print(f"{deck_name}: {len(pages_with_code)} code slides ({len(deck_containers)} containers) | Injected: {len(injected)} | Missing: {len(missing)}")

    print("\n" + "="*60)
    total_slides = sum(s['total_code_slides'] for s in deck_stats.values())
    total_boxes = sum(s['total_containers'] for s in deck_stats.values())
    total_injected = sum(len(s['injected_pages']) for s in deck_stats.values())
    total_missing = sum(len(s['missing_pages']) for s in deck_stats.values())
    print(f"TOTAL CODE SLIDES: {total_slides}")
    print(f"TOTAL CODE CONTAINERS: {total_boxes}")
    print(f"TOTAL ALREADY INJECTED: {total_injected}")
    print(f"TOTAL MISSING INJECTION: {total_missing}")

    with open('/tmp/refined_code_inventory.json', 'w') as f:
        json.dump({
            'deck_stats': deck_stats,
            'inventory': all_results
        }, f, indent=2)

if __name__ == '__main__':
    run()
