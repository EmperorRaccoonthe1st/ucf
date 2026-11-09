#!/usr/bin/env python3
"""
COP 3330 OOP Master Course Reference Archive Extractor & Verifier
Cross-platform tool to recombine and extract split 7z archives with SHA-256 verification.
"""

import os
import sys
import glob
import hashlib
import shutil
import subprocess

EXPECTED_SHA256 = "10de56a4f21b9d6e80b9d730453ad33f07f814a50eb1912eb32c59994da9c9ff"
TARGET_FILE = "COP3330_OOP_Complete_Course_Reference.pdf"
VOLUME_PATTERN = "COP3330_OOP_Course_Reference.7z.*"


def compute_sha256(filepath: str) -> str:
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(1024 * 1024 * 4):  # 4MB chunks
            hasher.update(chunk)
    return hasher.hexdigest()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print("=" * 79)
    print("  COP 3330: Object-Oriented Programming - Course Reference Extractor")
    print("=" * 79)

    parts = sorted(glob.glob(VOLUME_PATTERN))
    if not parts:
        print(f"[ERROR] No archive parts matching '{VOLUME_PATTERN}' found in {script_dir}")
        sys.exit(1)

    print(f"[INFO] Found {len(parts)} archive volumes:")
    total_size = 0
    for p in parts:
        sz = os.path.getsize(p)
        total_size += sz
        print(f"       - {p} ({sz / (1024*1024):.2f} MB)")
    print(f"[INFO] Total compressed archive size: {total_size / (1024*1024):.2f} MB")

    if os.path.exists(TARGET_FILE):
        print(f"\n[INFO] Target deliverable '{TARGET_FILE}' already exists.")
        actual_sha = compute_sha256(TARGET_FILE)
        if actual_sha == EXPECTED_SHA256:
            print("[PASS] Existing deliverable SHA-256 matches master catalog!")
            print(f"       SHA-256: {actual_sha}")
            print(f"       Size:    {os.path.getsize(TARGET_FILE) / (1024*1024):.2f} MB")
            print("=" * 79)
            return
        else:
            print("[WARN] Existing deliverable checksum mismatch. Proceeding with re-extraction...")

    # Method 1: Check for 7z executable
    sevenzip_bin = None
    for cand in ["7z", "7za"]:
        found = shutil.which(cand)
        if found:
            sevenzip_bin = found
            break

    # Also check standard Windows locations if on Windows
    if not sevenzip_bin and sys.platform.startswith("win"):
        win_candidates = [
            os.path.expandvars(r"%ProgramFiles%\7-Zip\7z.exe"),
            os.path.expandvars(r"%ProgramFiles(x86)%\7-Zip\7z.exe"),
            os.path.expandvars(r"%LocalAppData%\Programs\7-Zip\7z.exe"),
            os.path.expandvars(r"%ProgramData%\chocolatey\bin\7z.exe"),
        ]
        for p in win_candidates:
            if os.path.isfile(p):
                sevenzip_bin = p
                break

    extracted = False
    if sevenzip_bin:
        print(f"\n[INFO] Using 7-Zip engine: {sevenzip_bin}")
        ret = subprocess.run([sevenzip_bin, "x", "-y", parts[0]])
        if ret.returncode == 0 and os.path.isfile(TARGET_FILE):
            extracted = True
        else:
            print("[WARN] 7-Zip extraction returned non-zero code. Trying fallback...")

    # Method 2: Recombine into temporary file and use tar / bsdtar
    if not extracted:
        tar_bin = shutil.which("tar") or shutil.which("bsdtar")
        if tar_bin:
            temp_combined = "_temp_combined_archive.7z"
            print(f"\n[INFO] Recombining volumes into temporary file '{temp_combined}'...")
            try:
                with open(temp_combined, "wb") as outfile:
                    for part in parts:
                        with open(part, "rb") as infile:
                            shutil.copyfileobj(infile, outfile, 1024 * 1024 * 8)
                print(f"[INFO] Extracting via {tar_bin}...")
                ret = subprocess.run([tar_bin, "-xf", temp_combined])
                if ret.returncode == 0 and os.path.isfile(TARGET_FILE):
                    extracted = True
            finally:
                if os.path.exists(temp_combined):
                    os.remove(temp_combined)

    if not extracted:
        print("\n[ERROR] Failed to extract archive automatically.")
        print("Please install 7-Zip (https://www.7-zip.org/) or run: '7z x COP3330_OOP_Course_Reference.7z.001'")
        sys.exit(1)

    # Integrity verification
    print("\n[INFO] Verifying SHA-256 integrity of extracted PDF deliverable...")
    actual_sha = compute_sha256(TARGET_FILE)
    if actual_sha == EXPECTED_SHA256:
        print(f"[PASS] Exact SHA-256 match: {actual_sha}")
    else:
        print(f"[FAIL] Checksum mismatch!")
        print(f"       Expected: {EXPECTED_SHA256}")
        print(f"       Actual:   {actual_sha}")
        sys.exit(1)

    pdf_size = os.path.getsize(TARGET_FILE)
    print("=" * 79)
    print(f"[PASS] Successfully verified and extracted {TARGET_FILE}")
    print(f"       Size:  {pdf_size / (1024*1024):.2f} MB ({pdf_size:,} bytes)")
    print(f"       Pages: 776")
    print("=" * 79)


if __name__ == "__main__":
    main()
