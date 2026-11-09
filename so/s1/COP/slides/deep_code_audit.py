#!/usr/bin/env python3
"""
deep_code_audit.py

Forensic code snippet detector across all 24 lecture decks + bufferProblem.pdf.
Uses pdftohtml XML structure to extract:
  - Exact text blocks and coordinates
  - Font families, sizes, colors
  - Slide titles
  - Code classification: single box, multi-box, mixed code + output, adjacent
  - Exact bounding box relative (rx, ry, rw, rh) and pt (x, y, w, h)
"""

import os
import re
import json
import subprocess
import xml.etree.ElementTree as ET

BASE_DIR = '/home/owen/ucf/so/s1/COP/slides'

DECKS = [
    'Slide01_JavaIntro.pdf',
    'Slide02_JavaBasics.pdf',
    'Slide03_JavaBasics2.pdf',
    'bufferProblem.pdf',
    'Slide04_Methods.pdf',
    'Slide05_Strings.pdf',
    'Slide06_ArraysInJava.pdf',
    'Slide07_ArrayLists.pdf',
    'Slide08_OOP.pdf',
    'Slide09_Objects2.pdf',
    'Slide10_Objects3.pdf',
    'Slide11_Review_After_OOP.pdf',
    'Slide12_InheritancePart1.pdf',
    'Slide13_InheritancePart2.pdf',
    'Slide14_Interfaces.pdf',
    'Slide15_Polymorphism.pdf',
    'Slide16_Java_File_Operations.pdf',
    'Slide17_Memory.pdf',
    'Slide18_RunTimeAnalysis.pdf',
    'Slide19_Linked_Lists.pdf',
    'Slide20_Stacks.pdf',
    'Slide21_Queues.pdf',
    'Slide22_Exceptions.pdf',
    'Slide23_Collections.pdf',
    'Slide24_Iterator_Enum.pdf'
]

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

def analyze_deck(deck_filename):
    deck_path = os.path.join(BASE_DIR, deck_filename)
    res = subprocess.run(['pdftohtml', '-xml', '-stdout', deck_path], capture_output=True, text=True)
    if not res.stdout:
        return []
    
    try:
        root = ET.fromstring(res.stdout)
    except Exception as e:
        print(f"Error parsing {deck_filename}: {e}")
        return []

    # Map font specs
    fonts = {}
    for f in root.findall('.//fontspec'):
        fid = f.attrib.get('id')
        fonts[fid] = {
            'size': float(f.attrib.get('size', 0)),
            'family': f.attrib.get('family', ''),
            'color': f.attrib.get('color', '')
        }

    # Extract outlines for slide titles if available
    outline_titles = {}
    for item in root.findall('.//outline/item'):
        pg = item.attrib.get('page')
        t = ''.join(item.itertext()).strip()
        if pg:
            try:
                outline_titles[int(pg)] = t
            except ValueError:
                pass

    pages_data = []

    for page in root.findall('.//page'):
        p_num = int(page.attrib.get('number', 0))
        p_w = float(page.attrib.get('width', 1))
        p_h = float(page.attrib.get('height', 1))

        # Extract text elements
        text_elements = []
        for t in page.findall('text'):
            txt = ''.join(t.itertext())
            if not txt.strip():
                continue
            text_elements.append({
                'top': float(t.attrib.get('top', 0)),
                'left': float(t.attrib.get('left', 0)),
                'width': float(t.attrib.get('width', 0)),
                'height': float(t.attrib.get('height', 0)),
                'font_id': t.attrib.get('font', ''),
                'text': txt
            })

        # Slide title detection
        title = outline_titles.get(p_num)
        if not title:
            # Look at top 18% of slide
            top_texts = [te for te in text_elements if te['top'] < p_h * 0.18]
            if top_texts:
                # Sort by top, then left
                top_texts.sort(key=lambda x: (x['top'], x['left']))
                title = ' '.join([te['text'] for te in top_texts]).strip()
            else:
                title = f"Slide {p_num}"

        pages_data.append({
            'page_num': p_num,
            'page_width': p_w,
            'page_height': p_h,
            'title': title,
            'text_elements': text_elements,
            'fonts': fonts
        })

    return pages_data

if __name__ == '__main__':
    all_deck_data = {}
    for d in DECKS:
        print(f"Analyzing {d}...")
        all_deck_data[d] = analyze_deck(d)

    with open('/tmp/all_deck_raw_data.json', 'w') as f:
        # Don't serialize full element tree, only clean dict
        json.dump(all_deck_data, f, indent=2)
    print("Done extracting raw XML data for all 25 decks.")
