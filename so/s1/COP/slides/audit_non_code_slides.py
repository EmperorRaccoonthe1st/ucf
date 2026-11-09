#!/usr/bin/env python3
"""
audit_non_code_slides.py

Adversarial check: Inspects all 216 slides that were NOT classified as code slides
to verify zero false negatives.
"""

import json
import re

with open('/tmp/all_deck_raw_data.json') as f:
    all_data = json.load(f)

with open('/tmp/refined_code_inventory.json') as f:
    refined = json.load(f)

detected_pages = {}
for deck, stats in refined['deck_stats'].items():
    detected_pages[deck] = set(stats['injected_pages'] + stats['missing_pages'])

print(f"Total decks: {len(all_data)}")

suspect_slides = []

for deck_name, pages in all_data.items():
    code_set = detected_pages.get(deck_name, set())
    for p in pages:
        p_num = p['page_num']
        if p_num in code_set:
            continue
        # Check text of skipped page
        full_text = ' '.join(t['text'] for t in p['text_elements'])
        
        # Check if it has any code-like phrases
        has_java = any(kw in full_text for kw in [
            'System.out', 'public class', 'public static', 'void main', 'for (', 'while (',
            'int[]', 'ArrayList<', 'new ', 'try {', 'catch (', 'return ', 'class '
        ])
        semi_count = full_text.count(';')
        brace_count = full_text.count('{') + full_text.count('}')
        
        if has_java and (semi_count >= 1 or brace_count >= 1):
            suspect_slides.append({
                'deck': deck_name,
                'page': p_num,
                'title': p['title'],
                'semi_count': semi_count,
                'brace_count': brace_count,
                'text_sample': full_text[:120]
            })

print(f"Suspect skipped slides count: {len(suspect_slides)}")
for s in suspect_slides:
    print(f"{s['deck']} p{s['page']} ({s['title']}): semi={s['semi_count']}, brace={s['brace_count']} | {s['text_sample']}")
