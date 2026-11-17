# Block 5 Master Documents: Production & Verification Report
BSC2010C: General Biology I • Course Curriculum Integration (Exam 5)

This report documents the directory organization, full-document conversion, visual verification, and PDF compilation for Block 5, covering **Chapter 14** ("Mendel & The Gene Idea") and **Chapter 15** ("The Chromosomal Basis of Inheritance"). Unlike summary-only builds, **100% of every `.html`, `.pptx`, `.docx`, and `.pdf` source document** held inside `/home/owen/ucf/so/s1/BSC/block5/` is embedded in full inside the compiled PDF deliverables.

---

## 1. Directory Structure Organization

The Block 5 workspace follows the standardized modular layout used across Blocks 3 and 4:

```text
/home/owen/ucf/so/s1/BSC/block5/
├── documents/
│   ├── chapter_14/
│   │   ├── html/            # 4 Canvas modules & asset directories
│   │   ├── powerpoint/      # Chapter 14_student.pptx (58 slides)
│   │   └── practice/        # Practice Questions.docx + Simple Mono/Dihybrid answers.pdf
│   └── chapter_15/
│       ├── html/            # 1 Canvas module & asset directory
│       ├── powerpoint/      # Chapter 15_student.pptx (22 slides)
│       └── practice/        # Practice Questions.docx + Practice Genetics answers.pdf
├── generated/               # Compiled Master Reference PDFs
└── reports/                 # Markdown production & audit report
```

---

## 2. Embedded Curriculum Inventory (100% Source Inclusion)

Every file inside `block5/documents/` was converted and fused cleanly without omitting slides, pages, figures, or handwritten answer keys:

### A. Unified Deliverable
* **Document:** [Block 5 - Complete Master Reference (Chapters 14 & 15).pdf](file:///home/owen/ucf/so/s1/BSC/block5/generated/Block%205%20-%20Complete%20Master%20Reference%20(Chapters%2014%20%26%2015).pdf)
* **Total Volume:** 115 pages (14.66 MB)
* **Scope:** Single unified archive containing Cover/TOC + all Chapter 14 HTML modules (12 pages) + all 58 `Chapter 14_student.pptx` slides + all 3 pages of `Simple Mono and Dihybrid Crosses_Spring 2023_answers.pdf` + Chapter 15 HTML module (3 pages) + all 22 `Chapter 15_student.pptx` slides + all 6 pages of `Practice Genetics Problems_Spring 2023_answers.pdf` + all 5 pages of `Chapters 14 and 15 Practice Questions.docx` + section dividers with extracted XML speaker notes.

### B. Chapter 14 Embedded Files
* **Canvas Modules (4 HTML files, 12 rendered pages):**
  * `Chapter 14 Content Introduction_ BSC2010C-26Fall 0001.html` (genes, alleles, loci diagram)
  * `Chapter 14 Gregor Mendel's Experiments_ BSC2010C-26Fall 0001.html` (model system, Table 12.1)
  * `Chapter 14 Laws of Inheritance_ BSC2010C-26Fall 0001.html` (segregation, independent assortment)
  * `Chapter 14 Non-Mendelian Inheritance_ BSC2010C-26Fall 0001.html` (incomplete dominance, codominance, epistasis)
* **PowerPoint Deck (58 vector slides):**
  * `Chapter 14_student.pptx` converted via LibreOffice Impress headless -> US Letter Landscape framed vector pages, plus Slide 9 and Slide 19 XML speaker notes printed on the Section 14.5 divider page.
* **Worked Answer Key PDF (3 scanned handwritten pages):**
  * `Simple Mono and Dihybrid Crosses_Spring 2023_answers.pdf` framed in US Letter Portrait with zero cropping of handwritten Punnett squares or marginalia.

### C. Chapter 15 Embedded Files
* **Canvas Module (1 HTML file, 3 rendered pages):**
  * `Chapter 15 Content Introduction_ BSC2010C-26Fall 0001.html` (SRY gene, PAR synapsis, X-Y and Z-W sex determination diagrams)
* **PowerPoint Deck (22 vector slides):**
  * `Chapter 15_student.pptx` converted via LibreOffice Impress headless -> US Letter Landscape framed vector pages.
* **Worked Answer Key PDF (6 scanned handwritten pages):**
  * `Practice Genetics Problems_Spring 2023_answers.pdf` framed in US Letter Portrait covering Drosophila sex-linked crosses, Golden Retriever MWD pedigree, ABO blood types, Rh factor, and inheritance problems.

### D. Shared Word Practice Bank (Chapters 14 & 15)
* **Word Document (5 rendered pages):**
  * `Chapters 14 and 15 Practice Questions.docx` converted via LibreOffice Writer headless preserving exact formatting, highlighting, all practice questions, and the complete answer key.

---

## 3. Compiled Deliverables Catalog

| Deliverable PDF | Volume | Location |
|:----------------|:-------|:---------|
| [Block 5 - Complete Master Reference (Chapters 14 & 15).pdf](file:///home/owen/ucf/so/s1/BSC/block5/generated/Block%205%20-%20Complete%20Master%20Reference%20(Chapters%2014%20%26%2015).pdf) | 115 pages (14.66 MB) | `block5/generated/` |
| [Chapter 14 - Master Reference (Verbatim).pdf](file:///home/owen/ucf/so/s1/BSC/block5/generated/Chapter%2014%20-%20Master%20Reference%20(Verbatim).pdf) | 82 pages (8.71 MB) | `block5/generated/` |
| [Chapter 15 - Master Reference (Verbatim).pdf](file:///home/owen/ucf/so/s1/BSC/block5/generated/Chapter%2015%20-%20Master%20Reference%20(Verbatim).pdf) | 40 pages (6.11 MB) | `block5/generated/` |

> **Note:** Identical copies of all three compiled PDFs are also synchronized in `/home/owen/Downloads/tmp/web/generated/`.

---

## 4. Pipeline & Verification Matrix

```text
+-------------------------------------------------------------------------------+
| BLOCK 5 FULL-DOCUMENT EMBEDDING & VERIFICATION MATRIX                         |
+-------------------------------------------------------------------------------+
|                                                                               |
|  [Canvas HTML Modules (5 files)]                                              |
|   ├── Renderer: BeautifulSoup4 cleanup + WeasyPrint (US Letter Portrait)      |
|   └── Status: [PASS] 12 pp (Ch 14) + 3 pp (Ch 15) with all local figures      |
|                                                                               |
|  [PowerPoint Slide Decks (.pptx, 80 slides total)]                            |
|   ├── Renderer: LibreOffice Impress headless -> framed US Letter Landscape    |
|   └── Status: [PASS] 58 slides (Ch 14) + 22 slides (Ch 15) + speaker notes    |
|                                                                               |
|  [Worked Practice PDFs (.pdf, 9 scanned pages total)]                         |
|   ├── Renderer: pypdf scaling/framing onto US Letter Portrait                 |
|   └── Status: [PASS] 3 pp (Simple Mono/Dihybrid) + 6 pp (Practice Genetics)   |
|                                                                               |
|  [Practice Question Bank (.docx, 5 pages)]                                    |
|   ├── Renderer: LibreOffice Writer headless -> framed US Letter Portrait      |
|   └── Status: [PASS] All 5 pages + highlighted header + full answer key       |
|                                                                               |
|  [Final Assembly & Visual QA]                                                 |
|   ├── Features: Two-pass exact TOC page ranges, PDF bookmarks, page stamps    |
|   └── Status: [PASS] Verified rendered PNGs across every document category    |
|                                                                               |
+-------------------------------------------------------------------------------+
```

---

## 5. Build Reproduction

To regenerate all Block 5 PDFs from organized source documents:

```bash
cd /home/owen/Downloads/tmp/web/block5/build
uv run --with weasyprint --with beautifulsoup4 --with pypdf --with reportlab python3 build_block5_master_pdfs.py
```
