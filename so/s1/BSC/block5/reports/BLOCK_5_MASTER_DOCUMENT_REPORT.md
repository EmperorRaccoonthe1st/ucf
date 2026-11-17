# Block 5 Master Document: Production & Verification Report
BSC2010C: General Biology I • Course Curriculum Integration (Exam 5)

This report documents the directory organization, repository cleanup, full-document conversion, visual verification, and PDF compilation for Block 5, covering **Chapter 14** ("Mendel & The Gene Idea") and **Chapter 15** ("The Chromosomal Basis of Inheritance").

---

## 1. Directory Structure & Cleanup Summary

To minimize Git repository footprint while preserving 100% of curriculum content:
* Removed 16 MB of redundant Canvas Webcourses telemetry/UI boilerplate (`.js`, `.css`, `a_*.html`, `post_message_forwarding*`, avatars, and generic UI icons) from `*_files/`, retaining all 5 Canvas `.html` pages and all 11 biological diagram images.
* Consolidated generated output into a single unified archive PDF ([Block 5 - Complete Master Reference (Chapters 14 & 15).pdf](file:///home/owen/ucf/so/s1/BSC/block5/generated/Block%205%20-%20Complete%20Master%20Reference%20(Chapters%2014%20%26%2015).pdf)), removing duplicate per-chapter subset PDFs (~14.8 MB saved).
* Applied lossless `qpdf --object-streams=generate --recompress-flate` optimization (reducing final PDF size to 12.9 MiB / 13,529,953 bytes while keeping vector slides and outline bookmarks intact).

```text
/home/owen/ucf/so/s1/BSC/block5/
├── documents/
│   ├── chapter_14/
│   │   ├── html/            # 4 Canvas modules & 8 figure images
│   │   ├── powerpoint/      # Chapter 14_student.pptx (58 slides)
│   │   └── practice/        # Chapters 14 and 15 Practice Questions.docx + Simple Mono/Dihybrid PDF
│   └── chapter_15/
│       ├── html/            # 1 Canvas module & 3 figure images
│       ├── powerpoint/      # Chapter 15_student.pptx (22 slides)
│       └── practice/        # Chapters 14 and 15 Practice Questions.docx + Practice Genetics PDF
├── generated/
│   └── Block 5 - Complete Master Reference (Chapters 14 & 15).pdf
└── reports/
    └── BLOCK_5_MASTER_DOCUMENT_REPORT.md
```

---

## 2. Deliverable Features & Embedded Inventory

* **Primary Deliverable:** [Block 5 - Complete Master Reference (Chapters 14 & 15).pdf](file:///home/owen/ucf/so/s1/BSC/block5/generated/Block%205%20-%20Complete%20Master%20Reference%20(Chapters%2014%20%26%2015).pdf)
* **Compiled Volume:** 115 pages (12.9 MiB / 13,529,953 bytes)
* **Visual Theme:** Flat pastel cornflower blue (`#6b93d6` primary / `#edf3fc` tint / `#3b5f9e` accent typography) with zero gradients.
* **Firefox PDF.js Document Outline:** 129 nested hierarchical bookmarks across 3 levels:
  * **Part I (Chapter 14):** Modules 14.1–14.4 with heading-level sub-bookmarks, all 58 individual titled slides from `Chapter 14_student.pptx`, and all 3 annotated solution pages from `Simple Mono and Dihybrid Crosses_Spring 2023_answers.pdf`.
  * **Part II (Chapter 15):** Module 15.1 with sub-bookmarks, all 22 individual titled slides from `Chapter 15_student.pptx`, and all 6 annotated solution pages from `Practice Genetics Problems_Spring 2023_answers.pdf`.
  * **Part III (Shared Practice Bank):** All 5 pages + official answer key from `Chapters 14 and 15 Practice Questions.docx`.

| Source Component | Format | Embedded Scope |
|:-----------------|:-------|:---------------|
| Ch 14 & Ch 15 Canvas Modules (5 files) | HTML | 15 pages verbatim + 11 diagrams + Table 12.1 |
| Ch 14 & Ch 15 Lecture Decks (2 files) | PPTX | 80 vector slides in US Letter Landscape + XML speaker notes |
| Worked Practice Answer Keys (2 files) | PDF | 9 scanned handwritten solution pages (Punnett squares & pedigrees) |
| Practice Question Bank (1 file) | DOCX | 5 pages covering 28 practice items + complete answer key |

---

## 3. Build Reproduction

```bash
cd /home/owen/Downloads/tmp/web/block5/build
uv run --with weasyprint --with beautifulsoup4 --with pypdf --with reportlab python3 build_block5_master_pdfs.py
```
