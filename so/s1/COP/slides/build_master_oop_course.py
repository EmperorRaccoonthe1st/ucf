#!/usr/bin/env python3
"""
build_master_oop_course.py

Master Compiler for the Complete University OOP (COP 3330) Course Compendium.
Produces a unified, high-resolution, professionally formatted master reference PDF:
  - 16:9 QHD Widescreen standard (2560 x 1440 canvas, 1920 x 1080 pt deliverable).
  - Catppuccin Mocha theme with JetBrains Mono monospace font.
  - Tab expansion (expandtabs(4)) eradicating all tofu missing-glyph boxes.
  - In-slide code snippet injections modernization across lecture slides.
  - Content-aware responsive Adjacent Format for external code suites and model solutions.
  - Full hierarchical PDF outline bookmarks for fast navigation across all parts, modules, and code files.
  - Multi-core parallel execution across 24 CPU workers.
"""

import os
import sys
import subprocess
import time
import re
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont
import pygments
from pygments.lexers import JavaLexer
from pygments.style import Style
from pygments.token import (
    Keyword, Name, Comment, String, Error, Number, Operator, Whitespace, Punctuation
)
import img2pdf
import pypdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORK_DIR = os.path.join(BASE_DIR, ".master_build_cache")
os.makedirs(WORK_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# Catppuccin Mocha Palette
# -----------------------------------------------------------------------------
MOCHA_BASE     = (30, 30, 46, 255)       # #1e1e2e (Code container background)
MOCHA_MANTLE   = (24, 24, 37, 255)       # #181825 (Page surface background)
MOCHA_SURFACE0 = (49, 50, 68, 255)       # #313244 (Container border)
MOCHA_SURFACE2 = (88, 91, 112, 255)      # #585b70 (Line numbers)
MOCHA_OVERLAY0 = (108, 112, 134, 255)    # #6c7086 (Comments)
MOCHA_TEXT     = (205, 214, 244, 255)    # #cdd6f4 (Default foreground)
MOCHA_MAUVE    = (203, 166, 247, 255)    # #cba6f7 (Keywords)
MOCHA_BLUE     = (137, 180, 250, 255)    # #89b4fa (Methods, types)
MOCHA_YELLOW   = (249, 226, 175, 255)    # #f9e2af (Classes)
MOCHA_GREEN    = (166, 227, 161, 255)    # #a6e3a1 (Strings)
MOCHA_PEACH    = (250, 179, 135, 255)    # #fab387 (Numbers)
MOCHA_SKY      = (137, 220, 235, 255)    # #89dceb (Operators)
MOCHA_OVERLAY2 = (147, 153, 178, 255)    # #9399b2 (Punctuation)
MOCHA_RED      = (243, 139, 168, 255)    # #f38ba8 (Errors)

class CatppuccinMochaPygments(Style):
    default_style = '#cdd6f4'
    styles = {
        Whitespace: '#6c7086',
        Comment: 'italic #6c7086',
        Comment.Single: 'italic #6c7086',
        Comment.Multiline: 'italic #6c7086',
        Keyword: 'bold #cba6f7',
        Keyword.Declaration: 'bold #cba6f7',
        Keyword.Type: 'bold #89b4fa',
        Keyword.Constant: '#fab387',
        Name: '#cdd6f4',
        Name.Class: 'bold #f9e2af',
        Name.Function: 'bold #89b4fa',
        Name.Variable: '#cdd6f4',
        Name.Constant: '#fab387',
        String: '#a6e3a1',
        String.Char: '#a6e3a1',
        Number: '#fab387',
        Operator: '#89dceb',
        Punctuation: '#9399b2',
        Error: '#f38ba8'
    }

CANVAS_W = 2560
CANVAS_H = 1440

def get_font(font_size=28):
    font_paths = [
        '/usr/share/fonts/TTF/JetBrainsMonoNerdFontMono-Bold.ttf',
        '/usr/share/fonts/TTF/JetBrainsMonoNerdFontMono-Regular.ttf',
        '/home/owen/.local/share/fonts/fonts/ttf/JetBrainsMonoNL-ExtraBold.ttf',
        '/usr/share/fonts/noto/NotoSansMono-Regular.ttf'
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, font_size)
            except Exception:
                pass
    return ImageFont.load_default()

def render_catppuccin_code_box(code_text, width, height, font_size=None, radius=16, line_numbers=False, two_column=False):
    """
    Renders a pristine Catppuccin Mocha code container.
    - Expands all tabs to spaces (no tofu glyphs).
    - Uses exact font.getlength() character advance.
    - Isolated column surfaces in two-column mode preventing cross-column text collision.
    """
    code_text = code_text.expandtabs(4)
    lines = code_text.strip().split('\n')
    num_lines = len(lines)
    
    box_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(box_img)
    
    draw.rounded_rectangle(
        [0, 0, width - 1, height - 1],
        radius=radius,
        fill=MOCHA_BASE,
        outline=MOCHA_SURFACE0,
        width=2
    )
    
    pad_y = 28
    pad_x = 28
    avail_h = height - 2 * pad_y
    
    if two_column:
        mid = (num_lines + 1) // 2
        col1 = lines[:mid]
        col2 = lines[mid:]
        
        fs = 17 if font_size is None else font_size
        line_h = int(fs * 1.45)
        if mid * line_h > avail_h:
            fs = max(13, int(avail_h / (mid * 1.45)))
            line_h = int(fs * 1.45)
            
        font = get_font(fs)
        gutter_w = int(fs * 2.4) if line_numbers else 0
        gap = 36
        col_w = (width - 2 * pad_x - gap) // 2
        div_x = pad_x + col_w + gap // 2
        
        draw.line([(div_x, pad_y), (div_x, height - pad_y)], fill=MOCHA_SURFACE0, width=1)
        
        for col_idx, (col_lines, start_line) in enumerate([(col1, 1), (col2, mid + 1)]):
            cx = pad_x if col_idx == 0 else div_x + gap // 2
            col_surf = Image.new('RGBA', (col_w, avail_h), (0, 0, 0, 0))
            col_draw = ImageDraw.Draw(col_surf)
            
            for r_idx, line in enumerate(col_lines):
                cy = r_idx * line_h
                if cy + line_h > avail_h:
                    break
                if line_numbers:
                    col_draw.text((0, cy), f"{start_line + r_idx:2d}", font=font, fill=MOCHA_SURFACE2)
                cur_x = gutter_w
                tokens = list(pygments.lex(line, JavaLexer()))
                for ttype, val in tokens:
                    if not val:
                        continue
                    sinfo = CatppuccinMochaPygments.style_for_token(ttype)
                    col_hex = sinfo.get('color') or 'cdd6f4'
                    r, g, b = int(col_hex[0:2], 16), int(col_hex[2:4], 16), int(col_hex[4:6], 16)
                    if cur_x >= col_w - 4:
                        break
                    col_draw.text((cur_x, cy), val, font=font, fill=(r, g, b, 255))
                    cur_x += font.getlength(val)
                    
            box_img.paste(col_surf, (cx, pad_y), col_surf)
        return box_img
        
    # Single-column rendering
    if font_size is None:
        font_size = max(15, min(36, int(avail_h / (num_lines * 1.45))))
    else:
        line_h = int(font_size * 1.45)
        if num_lines * line_h > avail_h:
            font_size = max(14, int(avail_h / (num_lines * 1.45)))
            
    line_h = int(font_size * 1.45)
    font = get_font(font_size)
    gutter_w = int(font_size * 2.4) if line_numbers else 0
    
    for row_idx, line in enumerate(lines):
        curr_y = pad_y + row_idx * line_h
        if curr_y + line_h > height - 8:
            break
        if line_numbers:
            draw.text((pad_x, curr_y), f"{row_idx + 1:2d}", font=font, fill=MOCHA_SURFACE2)
        cur_x = pad_x + gutter_w
        tokens = list(pygments.lex(line, JavaLexer()))
        for ttype, val in tokens:
            if not val:
                continue
            sinfo = CatppuccinMochaPygments.style_for_token(ttype)
            col_hex = sinfo.get('color') or 'cdd6f4'
            r, g, b = int(col_hex[0:2], 16), int(col_hex[2:4], 16), int(col_hex[4:6], 16)
            draw.text((cur_x, curr_y), val, font=font, fill=(r, g, b, 255))
            cur_x += font.getlength(val)
            
    return box_img

def render_slide_ppm(pdf_path, page_num, dpi=180, out_prefix=None):
    """Renders a PDF page to a high-resolution PIL Image using pdftoppm."""
    if out_prefix is None:
        out_prefix = os.path.join(WORK_DIR, f"r_{abs(hash(pdf_path)) % 100000}_{page_num}_{os.getpid()}")
    subprocess.run([
        'pdftoppm', '-png', '-r', str(dpi),
        '-f', str(page_num), '-l', str(page_num),
        pdf_path, out_prefix
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    img_path = f"{out_prefix}-{page_num:02d}.png"
    if not os.path.exists(img_path):
        img_path = f"{out_prefix}-{page_num}.png"
    img = Image.open(img_path).convert('RGBA')
    if os.path.exists(img_path):
        try:
            os.remove(img_path)
        except OSError:
            pass
    return img

def place_slide_on_mocha_surface(slide_img):
    """Places a slide image onto the 2560 x 1440 Catppuccin Mantle surface."""
    sw, sh = slide_img.size
    max_w = CANVAS_W - 60
    max_h = CANVAS_H - 60
    scale = min(max_w / sw, max_h / sh)
    nw = int(sw * scale)
    nh = int(sh * scale)
    
    slide_scaled = slide_img.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new('RGB', (CANVAS_W, CANVAS_H), (24, 24, 37))
    
    px = (CANVAS_W - nw) // 2
    py = (CANVAS_H - nh) // 2
    canvas.paste(slide_scaled, (px, py))
    return canvas

# -----------------------------------------------------------------------------
# Curated In-Slide Code Snippet Injections Database (Merged with 318-Container Catalog)
# -----------------------------------------------------------------------------
SLIDE_INJECTIONS = {
    # Module 02 - JavaBasics p4: FirstJavaProgram
    ('Slide02_JavaBasics.pdf', 4): [
        {
            'code': """// Author: Safa Bacanli
/* This class salutes class, assignment0
   PID: 1231231 | NID: xy121212 */
package assignment0;

public class FirstJavaProgram {
    public static void main(String[] args) {
        System.out.println("Hi Class!");
    }
}""",
            'rx': 0.048, 'ry': 0.170, 'rw': 0.650, 'rh': 0.760, 'fs': 36
        }
    ],
    # bufferProblem p3: Scanner problem test
    ('bufferProblem.pdf', 3): [
        {
            'code': """package testjava;
import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter age");
        int age;
        age = scan.nextInt();
        System.out.println("Age is " + age);
        System.out.println("Enter full name");
        String name = scan.nextLine();
        System.out.println("Name is <" + name + ">");
        System.out.println("Enter name of school");
        String school = scan.nextLine();
    }
}""",
            'rx': 0.048, 'ry': 0.140, 'rw': 0.700, 'rh': 0.830, 'fs': 38
        }
    ],
    # Module 03 - JavaBasics2 p20: Typecasting examples
    ('Slide03_JavaBasics2.pdf', 20): [
        {
            'code': """package somePackage;

public class testString {
    public static void main(String[] args) {
        int numberi = 5;
        float numberf = 3.0f;
        numberf = numberi; // int can fit inside float
        System.out.println(numberi);
        System.out.println(numberf + "\\n");

        numberf = 3.2f;
        numberi = (int)numberf; // float cannot fit inside int
        System.out.println(numberi);
        System.out.println(numberf);
    }
}""",
            'rx': 0.043, 'ry': 0.138, 'rw': 0.595, 'rh': 0.820, 'fs': 34
        }
    ],
    # Module 04 - Methods p7: Max method
    ('Slide04_Methods.pdf', 7): [
        {
            'code': """/** Return the max between two numbers */
public static int max(int num1, int num2) {
    int result;
    if (num1 > num2)
        result = num1;
    else
        result = num2;

    return result;
}""",
            'rx': 0.045, 'ry': 0.190, 'rw': 0.650, 'rh': 0.680, 'fs': 34
        }
    ],
    # Module 06 - Arrays p9: 1D Array Traversal
    ('Slide06_ArraysInJava.pdf', 9): [
        {
            'code': """// Standard and Enhanced for-loop traversal:
int[] arr = {4, 5, 6, 7};

// Enhanced for-each loop:
for (int i : arr) {
    System.out.println(i);
}

// Index-based counter loop:
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}""",
            'rx': 0.048, 'ry': 0.190, 'rw': 0.580, 'rh': 0.740, 'fs': 34
        }
    ],
    # Module 06 - Arrays p11: 2D Matrix Traversal
    ('Slide06_ArraysInJava.pdf', 11): [
        {
            'code': """// Nested loops for 2D array matrix traversal:
for (int i = 0; i < arr.length; i++) {
    for (int j = 0; j < arr[i].length; j++) {
        System.out.print(arr[i][j] + " ");
    }
    System.out.println();
}""",
            'rx': 0.048, 'ry': 0.190, 'rw': 0.620, 'rh': 0.540, 'fs': 34
        }
    ],
    # Module 12 - Inheritance1 p4: 4 Quadrants
    ('Slide12_InheritancePart1.pdf', 4): [
        {
            'code': """package carEx;

public class Car extends Vehicle {
    private String brandName;

    public Car(String bname) {
        super();
        brandName = bname;
        System.out.println("Car is created");
    }

    public void go() {
        System.out.println(brandName + " is going on "
            + getWheelNum() + " wheels");
    }
}""",
            'rx': 0.018, 'ry': 0.142, 'rw': 0.468, 'rh': 0.615, 'fs': 28
        },
        {
            'code': """public void go() {
    System.out.println(brandName +
        " is going on " + super.getWheelNum() +
        " wheels");
}""",
            'rx': 0.015, 'ry': 0.772, 'rw': 0.468, 'rh': 0.218, 'fs': 26
        },
        {
            'code': """package carEx;

public class Vehicle {
    private int wheelNumber;

    public Vehicle() {
        wheelNumber = 4;
        System.out.println("Vehicle is created");
    }

    public int getWheelNum() {
        return wheelNumber;
    }
}""",
            'rx': 0.495, 'ry': 0.142, 'rw': 0.500, 'rh': 0.505, 'fs': 29
        },
        {
            'code': """package carEx;

public class vehiclesTester {
    public static void main(String[] args) {
        Car myCar = new Car("Ford");
        myCar.go();
        System.out.println(myCar.getWheelNum());
    }
}""",
            'rx': 0.496, 'ry': 0.655, 'rw': 0.496, 'rh': 0.330, 'fs': 29
        }
    ],
    # Module 13 - Inheritance2 p4: instanceof
    ('Slide13_InheritancePart2.pdf', 4): [
        {
            'code': """package payments;

public class CardPayment extends Payment {
    public CardPayment() {
        super();
        System.out.println("Card is created");
    }
}""",
            'rx': 0.018, 'ry': 0.140, 'rw': 0.465, 'rh': 0.395, 'fs': 28
        },
        {
            'code': """package payments;

public class Payment {
    private int amount;
    public Payment() {
        amount = 400;
        System.out.println("Payment is created");
    }
}""",
            'rx': 0.495, 'ry': 0.140, 'rw': 0.485, 'rh': 0.395, 'fs': 28
        },
        {
            'code': """package payments;

public class PaymentsTester {
    public static void main(String[] args) {
        Payment c = new Payment();
        CardPayment cp = new CardPayment();
        System.out.println(cp instanceof Payment);     // true
        System.out.println(cp instanceof CardPayment); // true
    }
}""",
            'rx': 0.018, 'ry': 0.540, 'rw': 0.565, 'rh': 0.435, 'fs': 28
        }
    ],
    # Module 16 - FileOps p6: WriteFile
    ('Slide16_Java_File_Operations.pdf', 6): [
        {
            'code': """public static void WriteFile(String fname){
    BufferedWriter bw; // why is this line outside of try catch?
    try{
        bw=new BufferedWriter(new FileWriter(fname));
        bw.write("Some text here"+System.lineSeparator());
        bw.write("another text here"+"\\n");
        bw.close();
    }catch(Exception e){
        e.printStackTrace();
    }//end of try catch
}//end of method""",
            'rx': 0.045, 'ry': 0.225, 'rw': 0.810, 'rh': 0.655, 'fs': 28
        }
    ],
    # Module 19 - LinkedLists p6: LinkedList class
    ('Slide19_Linked_Lists.pdf', 6): [
        {
            'code': """package allLinkedList;

public class LinkedList {
    private Node head;

    public LinkedList(){
        head=null;
    }

    private Node getHead() {
        return head;
    }

    public boolean isEmpty(){
        return head == null;
    }
}""",
            'rx': 0.040, 'ry': 0.035, 'rw': 0.440, 'rh': 0.700, 'fs': 28
        }
    ],
    # Module 22 - Exceptions p8: Multi-catch
    ('Slide22_Exceptions.pdf', 8): [
        {
            'code': """package javaEx;
import java.io.*;

public class TesterCode {
    public static void main(String[] args) {
        try {
            int result = 0 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic Exception Caught");
            e.printStackTrace();
        } catch (Exception e) {
            System.out.println("Generic Exception Caught");
            e.printStackTrace();
        }
        System.out.println("ENDOFBLOCK");
    }
}""",
            'rx': 0.015, 'ry': 0.185, 'rw': 0.612, 'rh': 0.720, 'fs': 32
        }
    ]
}

def load_all_injections():
    """Merges hand-tuned prototype injections with the full 318-container forensic catalog."""
    import json
    injections = dict(SLIDE_INJECTIONS)
    catalog_path = os.path.join(BASE_DIR, "missing_code_snippets_catalog.json")
    if os.path.exists(catalog_path):
        with open(catalog_path, 'r', encoding='utf-8') as f:
            catalog_data = json.load(f)
        for it in catalog_data.get('inventory', []):
            deck_name = it['deck']
            page_no = it['page']
            key = (deck_name, page_no)
            if key not in SLIDE_INJECTIONS:
                if key not in injections:
                    injections[key] = []
                injections[key].append({
                    'code': it['code_text'],
                    'rx': it['bbox_rel']['rx'],
                    'ry': it['bbox_rel']['ry'],
                    'rw': it['bbox_rel']['rw'],
                    'rh': it['bbox_rel']['rh'],
                    'fs': None
                })
    return injections

ALL_INJECTIONS = load_all_injections()

# -----------------------------------------------------------------------------
# Worker Functions for Parallel Rendering
# -----------------------------------------------------------------------------
def worker_render_slide(task):
    """
    Worker task:
      task = (out_png_path, pdf_path, page_num, key_tuple)
    """
    out_png_path, pdf_path, page_num, key = task
    try:
        out_pfx = f"{out_png_path}_ppm"
        slide_img = render_slide_ppm(pdf_path, page_num, out_prefix=out_pfx)
        sw, sh = slide_img.size
        
        # Apply in-slide injections if defined
        if key in ALL_INJECTIONS:
            for inj in ALL_INJECTIONS[key]:
                bx = int(sw * inj['rx'])
                by = int(sh * inj['ry'])
                bw = int(sw * inj['rw'])
                bh = int(sh * inj['rh'])
                
                # Dynamic font size with vertical and horizontal bounds
                code_text = inj['code']
                lines = code_text.strip().split('\n')
                max_len = max(len(l) for l in lines) if lines else 1
                avail_h = bh - 56
                avail_w = bw - 56
                fs_h = int(avail_h / (len(lines) * 1.45))
                fs_w = int(avail_w / (max_len * 0.62))
                fs = inj.get('fs') or max(14, min(34, fs_h, fs_w))
                
                box = render_catppuccin_code_box(code_text, bw, bh, font_size=fs, radius=14)
                slide_img.paste(box, (bx, by), box)
                
        canvas = place_slide_on_mocha_surface(slide_img)
        canvas.save(out_png_path, 'PNG')
        return out_png_path
    except Exception as e:
        print(f"Error rendering {pdf_path} p{page_num}: {e}", file=sys.stderr)
        raise e

def render_adjacent_pairing(left_pdf, left_page, code_file_path, out_png_path, code_w=820, font_size=16, two_column=False):
    """Renders a responsive content-hugging adjacent layout."""
    slide_img = render_slide_ppm(left_pdf, left_page)
    sw, sh = slide_img.size
    
    # Check if left slide has injections
    key = (os.path.basename(left_pdf), left_page)
    if key in ALL_INJECTIONS:
        for inj in ALL_INJECTIONS[key]:
            bx = int(sw * inj['rx'])
            by = int(sh * inj['ry'])
            bw = int(sw * inj['rw'])
            bh = int(sh * inj['rh'])
            box = render_catppuccin_code_box(inj['code'], bw, bh, font_size=inj.get('fs'), radius=14)
            slide_img.paste(box, (bx, by), box)
            
    with open(code_file_path, 'r', encoding='utf-8') as f:
        src = f.read().expandtabs(4)
        
    if two_column:
        wrapped = []
        for l in src.strip().split('\n'):
            if len(l) > 60 and '//' in l:
                idx = l.index('//')
                code_part = l[:idx].rstrip()
                comment_part = '    ' + l[idx:].lstrip()
                wrapped.append(code_part)
                wrapped.append(comment_part)
            else:
                wrapped.append(l)
        clean_code = '\n'.join(wrapped)
    else:
        clean_code = src
        
    canvas = Image.new('RGB', (CANVAS_W, CANVAS_H), (24, 24, 37))
    margin = 50
    code_h = 1340
    
    # Check if left document is portrait (e.g. Exam page)
    is_portrait = (sh > sw)
    if is_portrait:
        scale = code_h / sh
        nw = int(sw * scale)
        nh = int(sh * scale)
        slide_scaled = slide_img.resize((nw, nh), Image.Resampling.LANCZOS)
        canvas.paste(slide_scaled, (margin, (CANVAS_H - nh) // 2))
        
        dyn_code_w = CANVAS_W - margin * 3 - nw
        code_box = render_catppuccin_code_box(clean_code, dyn_code_w, code_h, font_size=font_size, radius=16, line_numbers=True, two_column=two_column)
        rx = margin * 2 + nw
        canvas.paste(code_box, (rx, (CANVAS_H - code_h) // 2), code_box)
    else:
        # Widescreen 16:9 slide
        code_box = render_catppuccin_code_box(clean_code, code_w, code_h, font_size=font_size, radius=16, line_numbers=True, two_column=two_column)
        avail_w = CANVAS_W - code_w - 3 * margin
        avail_h = code_h
        scale = min(avail_w / sw, avail_h / sh)
        nw = int(sw * scale)
        nh = int(sh * scale)
        slide_scaled = slide_img.resize((nw, nh), Image.Resampling.LANCZOS)
        
        canvas.paste(slide_scaled, (margin, (CANVAS_H - nh) // 2))
        rx = CANVAS_W - margin - code_w
        canvas.paste(code_box, (rx, (CANVAS_H - code_h) // 2), code_box)
        
    canvas.save(out_png_path, 'PNG')
    return out_png_path

# -----------------------------------------------------------------------------
# Master Document Assembly Specification
# -----------------------------------------------------------------------------
def get_course_structure():
    """Returns the ordered course outline and document manifest."""
    syllabus_pdf = os.path.join(BASE_DIR, "../exam1/01_Syllabus/COP3330_syllabus_slides.pdf")
    exam_pdf     = os.path.join(BASE_DIR, "../exam1/05_Sample_Exams/sampleMidtermExam.pdf")
    room_src     = os.path.join(BASE_DIR, "../exam1/05_Sample_Exams/rooms/Room.java")
    room_tester  = os.path.join(BASE_DIR, "../exam1/05_Sample_Exams/rooms/RoomTester.java")
    room_array   = os.path.join(BASE_DIR, "../exam1/05_Sample_Exams/rooms/RoomTesterArray.java")
    file_tester  = os.path.join(BASE_DIR, "../exam1/04_Code_Examples/FileTester/src/FileTester/FileTester.java")
    ula_dir      = os.path.join(BASE_DIR, "course_files_export/ula")
    
    sections = [
        # Part I
        {
            'part': 'Part I: Course Administration & Syllabus',
            'items': [
                ('Course Syllabus & Grading Policies', syllabus_pdf, 9)
            ]
        },
        # Part II: Core Lectures
        {
            'part': 'Part II: Core Lecture Slides (Modules 01 - 24)',
            'items': [
                ('Module 01: Introduction to Java', os.path.join(BASE_DIR, 'Slide01_JavaIntro.pdf'), 16),
                ('Module 02: Java Basics I - Syntax & Data Types', os.path.join(BASE_DIR, 'Slide02_JavaBasics.pdf'), 23),
                ('Module 03: Java Basics II - Control Flow & Loops', os.path.join(BASE_DIR, 'Slide03_JavaBasics2.pdf'), 22),
                ('Module 03 Supplement: Scanner Buffer Architecture', os.path.join(BASE_DIR, 'bufferProblem.pdf'), 10),
                ('Module 04: Methods & Parameter Passing', os.path.join(BASE_DIR, 'Slide04_Methods.pdf'), 21),
                ('Module 05: Strings & StringTokenizer', os.path.join(BASE_DIR, 'Slide05_Strings.pdf'), 24),
                ('Module 06: Arrays - 1D & 2D Arrays in Java', os.path.join(BASE_DIR, 'Slide06_ArraysInJava.pdf'), 27),
                ('Module 07: ArrayLists & Dynamic Collections', os.path.join(BASE_DIR, 'Slide07_ArrayLists.pdf'), 21),
                ('Module 08: OOP Fundamentals & Encapsulation', os.path.join(BASE_DIR, 'Slide08_OOP.pdf'), 17),
                ('Module 09: Objects II - References & Aliasing', os.path.join(BASE_DIR, 'Slide09_Objects2.pdf'), 29),
                ('Module 10: Objects III - Constructors & Static Scope', os.path.join(BASE_DIR, 'Slide10_Objects3.pdf'), 18),
                ('Module 11: Mid-Course OOP Review & Tracing', os.path.join(BASE_DIR, 'Slide11_Review_After_OOP.pdf'), 12),
                ('Module 12: Inheritance Part I - Superclasses & Hierarchy', os.path.join(BASE_DIR, 'Slide12_InheritancePart1.pdf'), 20),
                ('Module 13: Inheritance Part II - Method Overriding & Object', os.path.join(BASE_DIR, 'Slide13_InheritancePart2.pdf'), 12),
                ('Module 14: Interfaces & Multiple Implementation', os.path.join(BASE_DIR, 'Slide14_Interfaces.pdf'), 17),
                ('Module 15: Polymorphism & Dynamic Method Binding', os.path.join(BASE_DIR, 'Slide15_Polymorphism.pdf'), 26),
                ('Module 16: Java File Operations & I/O Streams', os.path.join(BASE_DIR, 'Slide16_Java_File_Operations.pdf'), 21),
                ('Module 17: JVM Memory Architecture - Stack & Heap', os.path.join(BASE_DIR, 'Slide17_Memory.pdf'), 28),
                ('Module 18: Asymptotic Runtime & Space Analysis (Big-O)', os.path.join(BASE_DIR, 'Slide18_RunTimeAnalysis.pdf'), 21),
                ('Module 19: Linked Lists Data Structure', os.path.join(BASE_DIR, 'Slide19_Linked_Lists.pdf'), 16),
                ('Module 20: Stacks Abstract Data Type', os.path.join(BASE_DIR, 'Slide20_Stacks.pdf'), 8),
                ('Module 21: Queues Abstract Data Type', os.path.join(BASE_DIR, 'Slide21_Queues.pdf'), 8),
                ('Module 22: Exception Handling Architecture', os.path.join(BASE_DIR, 'Slide22_Exceptions.pdf'), 20),
                ('Module 23: Java Collections Framework', os.path.join(BASE_DIR, 'Slide23_Collections.pdf'), 19),
                ('Module 24: Iterators & Enumerations', os.path.join(BASE_DIR, 'Slide24_Iterator_Enum.pdf'), 22),
            ]
        },
        # Part III: Companion Code Implementations
        {
            'part': 'Part III: Companion Code Implementations & Notes',
            'items': [
                ('Code Suite 01: Singly Linked Lists Implementation (Adjacent Model)', 'ADJACENT_LINKED_LIST', 1),
                ('Code Suite 01 Notes: Linked List Pointer Architecture', os.path.join(BASE_DIR, 'COP3330_linked_list_notes.pdf'), 12),
                ('Code Suite 02 Notes: Stack Structures & Array/List Implementations', os.path.join(BASE_DIR, 'COP3330_Stack_Notes.pdf'), 5),
                ('Code Suite 03 Notes: Queue Structures & FIFO Implementations', os.path.join(BASE_DIR, 'COP3330_Queue_Notes.pdf'), 6),
                ('Code Suite 04: File I/O Engine (FileTester.java Adjacent Model)', 'ADJACENT_FILE_TESTER', 1)
            ]
        },
        # Part IV: Midterm Exam Practice & Hotel Room Suite
        {
            'part': 'Part IV: Midterm Exam Practice & Hotel Room Solution Suite',
            'items': [
                ('Midterm Practice Exam Specification', exam_pdf, 3),
                ('Model Solution: Room Entity Class (Adjacent Model)', 'ADJACENT_ROOM', 1),
                ('Model Solution: Room ArrayList Tester Driver (Adjacent Model)', 'ADJACENT_ROOM_TESTER', 1),
                ('Model Solution: Room Array Tester Driver (Adjacent Model)', 'ADJACENT_ROOM_ARRAY', 1)
            ]
        },
        # Part V: ULA Comprehensive Review Guides
        {
            'part': 'Part V: ULA Comprehensive Review Guides',
            'items': [
                ('ULA Module 01: Intro to Java & Syntax', os.path.join(ula_dir, 'Intro to Java.pdf'), 4),
                ('ULA Module 02: Strings in Java', os.path.join(ula_dir, 'Strings in Java.pdf'), 4),
                ('ULA Module 03: Arrays & ArrayLists in Java', os.path.join(ula_dir, 'Arrays and ArrayLists in Java.pdf'), 4),
                ('ULA Module 04: Intro to Objects & References', os.path.join(ula_dir, 'Intro to Objects and References.pdf'), 5),
                ('ULA Module 05: The Four Pillars of OOP', os.path.join(ula_dir, 'The Pillars of OOP.pdf'), 4),
                ('ULA Module 06: Inheritance & Interfaces', os.path.join(ula_dir, 'Inheritance and Interfaces.pdf'), 5),
                ('ULA Module 07: File I/O & Exception Handling', os.path.join(ula_dir, 'File IO and Exception Handling.pdf'), 4),
                ('ULA Module 08: Runtime and Space Analysis', os.path.join(ula_dir, 'Runtime and Space Analysis.pdf'), 3),
                ('ULA Module 09: Linked Lists In-Depth', os.path.join(ula_dir, 'Linked Lists.pdf'), 5),
                ('ULA Module 10: Stacks & Queues Implementations', os.path.join(ula_dir, 'Stacks & Queues.pdf'), 4),
                ('ULA Module 11: Practice Exam Questions', os.path.join(ula_dir, 'practice_question.pdf'), 4),
                ('ULA Module 12: Sample Object Assignment', os.path.join(ula_dir, 'sampleObjectAssignment.pdf'), 4)
            ]
        }
    ]
    return sections

def create_master_cover_spread():
    """Generates the master compendium cover spread."""
    cover_img = Image.new('RGB', (CANVAS_W, CANVAS_H), (24, 24, 37))
    draw = ImageDraw.Draw(cover_img)
    
    # Outer frame
    draw.rounded_rectangle([60, 60, CANVAS_W - 61, CANVAS_H - 61], radius=24, fill=(30, 30, 46), outline=MOCHA_SURFACE0, width=3)
    
    # Inner hero card
    f_badge = get_font(24)
    f_hero = get_font(52)
    f_sub = get_font(28)
    f_desc = get_font(20)
    
    # Badge
    draw.rounded_rectangle([120, 120, 720, 175], radius=10, fill=(24, 24, 37), outline=MOCHA_SURFACE0, width=2)
    draw.text((140, 134), "UNIVERSITY OF CENTRAL FLORIDA  •  COP 3330", font=f_badge, fill=MOCHA_BLUE)
    
    # Title
    draw.text((120, 230), "OBJECT-ORIENTED PROGRAMMING", font=f_hero, fill=(255, 255, 255))
    draw.text((120, 310), "Complete University Course Reference Compendium", font=f_sub, fill=MOCHA_BLUE)
    draw.text((120, 360), "Standardized Widescreen Reference Unifying Lecture Slides, Syntax-Highlighted Code & Study Modules", font=f_desc, fill=MOCHA_OVERLAY0)
    
    # Divider
    draw.line([(120, 415), (CANVAS_W - 120, 415)], fill=MOCHA_SURFACE0, width=2)
    
    # Overview cards
    cards = [
        ("Part I: Course Administration & Syllabus", "Policies, grading standards, academic expectations, and schedule.", MOCHA_BLUE),
        ("Part II: Core Lecture Slides (01-24)", "24 comprehensive slide decks + Scanner buffer supplement (482 slides).", MOCHA_GREEN),
        ("Part III: Companion Code Implementations", "Linked Lists, Stacks, Queues, and File I/O runnable engines.", MOCHA_PEACH),
        ("Part IV: Midterm Practice & Hotel Room Suite", "Midterm exam problem prompt and verified Hotel Room model suite.", MOCHA_MAUVE),
        ("Part V: ULA Comprehensive Review Guides", "12 in-depth Undergraduate Learning Assistant review and trace guides.", MOCHA_SKY)
    ]
    
    cy = 460
    f_card_t = get_font(22)
    f_card_d = get_font(18)
    for title, desc, col in cards:
        draw.rounded_rectangle([120, cy, CANVAS_W - 120, cy + 130], radius=12, fill=(24, 24, 37), outline=MOCHA_SURFACE0, width=2)
        draw.text((160, cy + 28), title, font=f_card_t, fill=col)
        draw.text((160, cy + 72), desc, font=f_card_d, fill=MOCHA_TEXT)
        cy += 160
        
    draw.text((120, CANVAS_H - 120), "Department of Computer Science  •  College of Engineering & Computer Science  •  Orlando, FL", font=f_desc, fill=MOCHA_OVERLAY0)
    draw.text((CANVAS_W - 620, CANVAS_H - 120), "Catppuccin Mocha Standard  •  JetBrains Mono", font=f_desc, fill=MOCHA_BLUE)
    
    cover_path = os.path.join(WORK_DIR, "page_0000_cover.png")
    cover_img.save(cover_path, 'PNG')
    return cover_path

def main():
    start_time = time.time()
    print("=" * 80)
    print("COP 3330 MASTER COURSE REFERENCE: PRODUCTION COMPILER")
    print("=" * 80)
    
    sections = get_course_structure()
    
    # 1. Build Cover Page
    print("\n[STEP 1/4] Generating Master Cover Spread...")
    cover_png = create_master_cover_spread()
    print(f"  [OK] Cover saved: {cover_png}")
    
    # 2. Build Render Task Queue
    print("\n[STEP 2/4] Queuing and executing parallel rendering across 24 CPU cores...")
    render_tasks = []
    page_inventory = [] # [(page_num, part_title, item_title, png_path)]
    global_page_idx = 1
    
    page_inventory.append((0, "Overview", "Course Compendium Overview", cover_png))
    
    slide16_pdf = os.path.join(BASE_DIR, 'Slide16_Java_File_Operations.pdf')
    slide19_pdf = os.path.join(BASE_DIR, 'Slide19_Linked_Lists.pdf')
    exam_pdf    = os.path.join(BASE_DIR, "../exam1/05_Sample_Exams/sampleMidtermExam.pdf")
    room_src    = os.path.join(BASE_DIR, "../exam1/05_Sample_Exams/rooms/Room.java")
    room_tester = os.path.join(BASE_DIR, "../exam1/05_Sample_Exams/rooms/RoomTester.java")
    room_array  = os.path.join(BASE_DIR, "../exam1/05_Sample_Exams/rooms/RoomTesterArray.java")
    file_tester = os.path.join(BASE_DIR, "../exam1/04_Code_Examples/FileTester/src/FileTester/FileTester.java")
    
    special_renders = []
    
    for sec in sections:
        part_name = sec['part']
        for item_title, target_spec, count in sec['items']:
            if target_spec == 'ADJACENT_FILE_TESTER':
                out_png = os.path.join(WORK_DIR, f"page_{global_page_idx:04d}_adj_filetester.png")
                special_renders.append((render_adjacent_pairing, (slide16_pdf, 6, file_tester, out_png, 820, 16, False)))
                page_inventory.append((global_page_idx, part_name, item_title, out_png))
                global_page_idx += 1
            elif target_spec == 'ADJACENT_LINKED_LIST':
                out_png = os.path.join(WORK_DIR, f"page_{global_page_idx:04d}_adj_linkedlist.png")
                # Using linked list code
                ll_code_path = os.path.join(WORK_DIR, "LinkedListCode.java")
                with open(ll_code_path, 'w') as f:
                    f.write("""package allLinkedList;

public class LinkedList {
    private Node head;

    public LinkedList() {
        head = null;
    }

    // Copy constructor making deep copy
    public LinkedList(LinkedList tobecopied) {
        head = null;
        Node cur = tobecopied.getHead();
        while (cur != null) {
            insertTail(cur.getItem());
            cur = cur.getNext();
        }
    }

    public void insertHead(int el) {
        Node newNode = new Node(el);
        newNode.setNext(head);
        head = newNode;
    }

    public void insertTail(int el) {
        if (isEmpty()) {
            insertHead(el);
            return;
        }
        Node cur = head;
        while (cur.getNext() != null) {
            cur = cur.getNext();
        }
        cur.setNext(new Node(el));
    }

    public boolean isEmpty() {
        return head == null;
    }
}""")
                special_renders.append((render_adjacent_pairing, (slide19_pdf, 6, ll_code_path, out_png, 720, 22, False)))
                page_inventory.append((global_page_idx, part_name, item_title, out_png))
                global_page_idx += 1
            elif target_spec == 'ADJACENT_ROOM':
                out_png = os.path.join(WORK_DIR, f"page_{global_page_idx:04d}_adj_room.png")
                special_renders.append((render_adjacent_pairing, (exam_pdf, 2, room_src, out_png, 1375, 17, True)))
                page_inventory.append((global_page_idx, part_name, item_title, out_png))
                global_page_idx += 1
            elif target_spec == 'ADJACENT_ROOM_TESTER':
                out_png = os.path.join(WORK_DIR, f"page_{global_page_idx:04d}_adj_roomtester.png")
                special_renders.append((render_adjacent_pairing, (exam_pdf, 2, room_tester, out_png, 1375, 18, True)))
                page_inventory.append((global_page_idx, part_name, item_title, out_png))
                global_page_idx += 1
            elif target_spec == 'ADJACENT_ROOM_ARRAY':
                out_png = os.path.join(WORK_DIR, f"page_{global_page_idx:04d}_adj_roomarray.png")
                special_renders.append((render_adjacent_pairing, (exam_pdf, 3, room_array, out_png, 1375, 17, True)))
                page_inventory.append((global_page_idx, part_name, item_title, out_png))
                global_page_idx += 1
            else:
                # Regular PDF deck
                pdf_path = target_spec
                base_pdf_name = os.path.basename(pdf_path)
                try:
                    real_count = len(pypdf.PdfReader(pdf_path).pages)
                except Exception:
                    real_count = count
                for p_idx in range(1, real_count + 1):
                    out_png = os.path.join(WORK_DIR, f"page_{global_page_idx:04d}_{base_pdf_name}_{p_idx:02d}.png")
                    render_tasks.append((out_png, pdf_path, p_idx, (base_pdf_name, p_idx)))
                    page_inventory.append((global_page_idx, part_name, item_title, out_png))
                    global_page_idx += 1
                    
    total_pages = len(page_inventory)
    print(f"Total pages queued for compilation: {total_pages} pages")
    
    # Execute special adjacent renders synchronously
    print(f"  Rendering {len(special_renders)} adjacent pairings...")
    for fn, args in special_renders:
        fn(*args)
        print(f"    [OK] Adjacent pairing rendered: {os.path.basename(args[3])}")
        
    # Execute standard slide renders in parallel with 24 workers
    print(f"  Launching pool of 24 workers for {len(render_tasks)} slides...")
    pool_start = time.time()
    with Pool(processes=24) as pool:
        results = pool.map(worker_render_slide, render_tasks)
    pool_end = time.time()
    print(f"  [OK] Parallel rendering finished in {pool_end - pool_start:.2f} seconds ({len(results)} slides).")
    
    # 3. Assemble PDF with img2pdf
    print("\n[STEP 3/4] Converting high-res page images into master PDF deliverable...")
    ordered_pngs = [item[3] for item in page_inventory]
    for p in ordered_pngs:
        if not os.path.exists(p):
            raise FileNotFoundError(f"Missing required rendered page: {p}")
            
    raw_pdf_path = os.path.join(WORK_DIR, "raw_master.pdf")
    with open(raw_pdf_path, 'wb') as f:
        f.write(img2pdf.convert(ordered_pngs))
    print(f"  [OK] Raw master PDF generated ({os.path.getsize(raw_pdf_path) / (1024*1024):.2f} MB).")
    
    # 4. Inject Hierarchical Outline Bookmarks
    print("\n[STEP 4/4] Injecting interactive navigation outline bookmarks with pypdf...")
    final_output_pdf = os.path.join(BASE_DIR, "COP3330_OOP_Complete_Course_Reference.pdf")
    
    reader = pypdf.PdfReader(raw_pdf_path)
    writer = pypdf.PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
        
    # Build outline hierarchy
    current_part = None
    part_bookmark = None
    current_item = None
    
    for page_idx, part_name, item_title, png_path in page_inventory:
        if part_name != current_part:
            current_part = part_name
            part_bookmark = writer.add_outline_item(part_name, page_idx)
            current_item = None
            
        if item_title != current_item:
            current_item = item_title
            # Add module bookmark under part
            writer.add_outline_item(item_title, page_idx, parent=part_bookmark)
            
    with open(final_output_pdf, 'wb') as f:
        writer.write(f)
        
    end_time = time.time()
    file_size_mb = os.path.getsize(final_output_pdf) / (1024 * 1024)
    print("\n" + "=" * 80)
    print("MASTER PDF COMPILATION SUCCESSFUL")
    print(f"Deliverable: {final_output_pdf}")
    print(f"Total Pages: {len(writer.pages)}")
    print(f"File Size:   {file_size_mb:.2f} MB")
    print(f"Total Time:  {end_time - start_time:.2f} seconds")
    print("=" * 80)

if __name__ == '__main__':
    main()
