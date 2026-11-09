#!/usr/bin/env python3
"""
generate_prototypes.py

Generates 5 distinct prototype slides for user validation following the exact
rectification directives:
  1. Standalone Slide (Format 1): Pure text slide, fills entire page on a dark surface.
  2. Single Code Injection (Format 2A): 'Full code of the problem case' (bufferProblem p3)
     with dark Dracula code box replacing the unformatted code box; text on right intact.
  3. Mixed Code Injection (Format 2B): 'Typecasting examples' (Slide03 p20)
     with dark Dracula code box replacing the code box; warnings and output boxes on right intact.
  4. Multi-Box Code Injection (Format 2C): 'Inheritance example' (Slide12 p4)
     with 4 dark Dracula code boxes replacing the 4 unformatted boxes.
  5. Adjacent Format (Format 3): External code integration (Slide16 File Operations on left,
     external FileTester.java in Dracula dark mode on right).
"""

import os
import subprocess
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pygments
from pygments.lexers import JavaLexer
from pygments.styles import get_style_by_name

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Color Palette: Dracula Theme
DRACULA_BG = (40, 42, 54, 255)         # #282a36
DRACULA_BORDER = (68, 71, 90, 255)     # #44475a
DARK_SURFACE = (18, 19, 26, 255)       # #12131a

def get_fonts(font_size=24):
    """Load high-quality monospace font for syntax highlighting."""
    font_paths = [
        '/usr/share/fonts/TTF/JetBrainsMonoNerdFontPropo-Bold.ttf',
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

def render_dracula_code_box(code_text, width, height, font_size=26, radius=14, line_numbers=False):
    """Render a syntax-highlighted Dracula dark-mode code snippet box."""
    box_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(box_img)
    
    # Outer dark container with rounded corners and border
    draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, fill=DRACULA_BG, outline=DRACULA_BORDER, width=2)
    
    style = get_style_by_name('dracula')
    font = get_fonts(font_size)
    
    lines = code_text.strip().split('\n')
    line_h = int(font_size * 1.5)
    pad_x = 28
    pad_y = 24
    
    # Optional line numbers
    gutter_w = int(font_size * 2.2) if line_numbers else 0
    
    for row_idx, line in enumerate(lines):
        curr_y = pad_y + row_idx * line_h
        if curr_y + line_h > height - 12:
            break
            
        if line_numbers:
            draw.text((pad_x, curr_y), f"{row_idx + 1:2d}", font=font, fill=(98, 114, 164, 255))
            
        cur_x = pad_x + gutter_w
        tokens = list(pygments.lex(line, JavaLexer()))
        for ttype, val in tokens:
            if not val:
                continue
            sinfo = style.style_for_token(ttype)
            col_hex = sinfo.get('color') or 'f8f8f2'
            r = int(col_hex[0:2], 16)
            g = int(col_hex[2:4], 16)
            b = int(col_hex[4:6], 16)
            draw.text((cur_x, curr_y), val, font=font, fill=(r, g, b, 255))
            
            bbox = font.getbbox(val)
            cur_x += (bbox[2] - bbox[0])
            
    return box_img

def place_slide_on_dark_surface(slide_img, target_w=2080, target_h=1170):
    """Place a slide image on a dark surface background, maximizing screen coverage."""
    sw, sh = slide_img.size
    scale = min((target_w - 40) / sw, (target_h - 40) / sh)
    new_w = int(sw * scale)
    new_h = int(sh * scale)
    
    scaled_slide = slide_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    canvas = Image.new('RGB', (target_w, target_h), (18, 19, 26))
    px = (target_w - new_w) // 2
    py = (target_h - new_h) // 2
    canvas.paste(scaled_slide, (px, py))
    return canvas

def make_prototype_1():
    """Prototype 1: Standalone Text Slide (Slide03 p19 - Typecasting)"""
    print("Generating Prototype 1: Standalone Text Slide...")
    tmp_out = '/tmp/p1_raw'
    subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '19', '-l', '19', 'Slide03_JavaBasics2.pdf', tmp_out], check=True)
    slide_img = Image.open(f'{tmp_out}-19.png')
    page = place_slide_on_dark_surface(slide_img)
    out_path = os.path.join(BASE_DIR, 'proto_1_standalone_text.png')
    page.save(out_path)
    print(f"  [OK] Saved: {out_path}")
    return page

def make_prototype_2():
    """Prototype 2: Single Code Injection (bufferProblem p3 - Full code of problem case)"""
    print("Generating Prototype 2: Single Code Box Injection...")
    tmp_out = '/tmp/p2_raw'
    subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '3', '-l', '3', 'bufferProblem.pdf', tmp_out], check=True)
    slide_img = Image.open(f'{tmp_out}-03.png').convert('RGBA')
    
    # Injected Code
    code = """package testjava;
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
}"""
    # Box coordinates detected on 2000x1125: (96, 160, 1400, 950)
    bx, by, bw, bh = 94, 158, 1404, 940
    snippet = render_dracula_code_box(code, bw, bh, font_size=31, radius=14)
    slide_img.paste(snippet, (bx, by), snippet)
    
    page = place_slide_on_dark_surface(slide_img)
    out_path = os.path.join(BASE_DIR, 'proto_2_single_injection.png')
    page.save(out_path)
    print(f"  [OK] Saved: {out_path}")
    return page

def make_prototype_3():
    """Prototype 3: Mixed Code Injection (Slide03 p20 - Typecasting examples)"""
    print("Generating Prototype 3: Mixed Code Box Injection...")
    tmp_out = '/tmp/p3_raw'
    subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '20', '-l', '20', 'Slide03_JavaBasics2.pdf', tmp_out], check=True)
    slide_img = Image.open(f'{tmp_out}-20.png').convert('RGBA')
    
    code = """package somePackage;

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
}"""
    # Box coords on 2000x1125: (87, 157, 1187, 914)
    bx, by, bw, bh = 85, 155, 1190, 920
    snippet = render_dracula_code_box(code, bw, bh, font_size=28, radius=14)
    slide_img.paste(snippet, (bx, by), snippet)
    
    page = place_slide_on_dark_surface(slide_img)
    out_path = os.path.join(BASE_DIR, 'proto_3_mixed_injection.png')
    page.save(out_path)
    print(f"  [OK] Saved: {out_path}")
    return page

def make_prototype_4():
    """Prototype 4: Multi-Box Code Injection (Slide12 p4 - Inheritance example)"""
    print("Generating Prototype 4: Multi-Box Code Injection...")
    tmp_out = '/tmp/p4_raw'
    subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '4', '-l', '4', 'Slide12_InheritancePart1.pdf', tmp_out], check=True)
    slide_img = Image.open(f'{tmp_out}-04.png').convert('RGBA')
    
    # 4 distinct boxes detected on 2000x1125:
    # Box 1: (36, 160, 932, 694) - Car extends Vehicle
    code1 = """package carEx;

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
}"""
    snip1 = render_dracula_code_box(code1, 932, 694, font_size=23, radius=12)
    slide_img.paste(snip1, (36, 160), snip1)
    
    # Box 2: (29, 871, 934, 243) - go() override
    code2 = """public void go() {
    System.out.println(brandName +
        " is going on " + super.getWheelNum() +
        " wheels");
}"""
    snip2 = render_dracula_code_box(code2, 934, 243, font_size=21, radius=12)
    slide_img.paste(snip2, (29, 871), snip2)
    
    # Box 3: (990, 159, 998, 566) - Vehicle class
    code3 = """package carEx;

public class Vehicle {
    private int wheelNumber;

    public Vehicle() {
        wheelNumber = 4;
        System.out.println("Vehicle is created");
    }

    public int getWheelNum() {
        return wheelNumber;
    }
}"""
    snip3 = render_dracula_code_box(code3, 998, 566, font_size=24, radius=12)
    slide_img.paste(snip3, (990, 159), snip3)
    
    # Box 4: (992, 735, 990, 370) - vehiclesTester
    code4 = """package carEx;

public class vehiclesTester {
    public static void main(String[] args) {
        Car myCar = new Car("Ford");
        myCar.go();
        System.out.println(myCar.getWheelNum());
    }
}"""
    snip4 = render_dracula_code_box(code4, 990, 370, font_size=24, radius=12)
    slide_img.paste(snip4, (992, 735), snip4)
    
    page = place_slide_on_dark_surface(slide_img)
    out_path = os.path.join(BASE_DIR, 'proto_4_multi_injection.png')
    page.save(out_path)
    print(f"  [OK] Saved: {out_path}")
    return page

def make_prototype_5():
    """Prototype 5: Adjacent Format (External File Integration - FileTester.java + Slide16)"""
    print("Generating Prototype 5: Adjacent Format (External Code Example)...")
    # Left: Slide16 Page 6 (Writing to a file)
    tmp_out = '/tmp/p5_raw'
    subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '6', '-l', '6', 'Slide16_Java_File_Operations.pdf', tmp_out], check=True)
    slide_img = Image.open(f'{tmp_out}-06.png')
    
    # Right: External FileTester.java source code
    with open('../exam1/04_Code_Examples/FileTester/src/FileTester/FileTester.java', 'r', encoding='utf-8') as f:
        file_src = f.read()
        
    target_w, target_h = 2400, 1350
    canvas = Image.new('RGB', (target_w, target_h), (18, 19, 26)) # dark surface
    
    # Left Pane (Slide): 1120 x 1270
    sw, sh = slide_img.size
    scale = min(1120 / sw, 1270 / sh)
    lw = int(sw * scale)
    lh = int(sh * scale)
    slide_scaled = slide_img.resize((lw, lh), Image.Resampling.LANCZOS)
    canvas.paste(slide_scaled, (40, (target_h - lh) // 2))
    
    # Right Pane (Code): 1160 x 1270
    rw = 1160
    rh = 1270
    code_box = render_dracula_code_box(file_src, rw, rh, font_size=22, radius=16, line_numbers=True)
    canvas.paste(code_box, (1200, (target_h - rh) // 2), code_box)
    
    out_path = os.path.join(BASE_DIR, 'proto_5_adjacent_format.png')
    canvas.save(out_path)
    print(f"  [OK] Saved: {out_path}")
    return canvas

def main():
    make_prototype_1()
    make_prototype_2()
    make_prototype_3()
    make_prototype_4()
    make_prototype_5()
    
    import img2pdf
    imgs = [
        os.path.join(BASE_DIR, 'proto_1_standalone_text.png'),
        os.path.join(BASE_DIR, 'proto_2_single_injection.png'),
        os.path.join(BASE_DIR, 'proto_3_mixed_injection.png'),
        os.path.join(BASE_DIR, 'proto_4_multi_injection.png'),
        os.path.join(BASE_DIR, 'proto_5_adjacent_format.png')
    ]
    pdf_path = os.path.join(BASE_DIR, 'PROTOTYPE_SLIDES.pdf')
    with open(pdf_path, 'wb') as f:
        f.write(img2pdf.convert(imgs))
    print(f"\n[PASS] All 5 prototypes compiled into: {pdf_path}")

if __name__ == '__main__':
    main()
