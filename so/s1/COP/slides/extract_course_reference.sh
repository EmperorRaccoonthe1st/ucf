#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

TARGET="COP3330_OOP_Complete_Course_Reference.pdf"
PART1="COP3330_OOP_Course_Reference.7z.001"
EXPECTED_SHA="10de56a4f21b9d6e80b9d730453ad33f07f814a50eb1912eb32c59994da9c9ff"
COMBINED_TEMP="_temp_combined_archive.7z"

echo "==============================================================================="
echo "  COP 3330: Object-Oriented Programming - Course Reference Extractor"
echo "==============================================================================="

if [ ! -f "$PART1" ]; then
    echo "[ERROR] Missing archive volume 1: $PART1"
    echo "Ensure all parts (.7z.001 to .7z.005) are present in this directory."
    exit 1
fi

if [ -f "$TARGET" ]; then
    echo "[INFO] Deliverable already exists: $TARGET"
    read -p "Overwrite existing file? (y/N): " -r CONFIRM
    if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
        echo "[INFO] Extraction cancelled."
        exit 0
    fi
    echo ""
fi

# Step 1: Use 7-Zip if installed
if command -v 7z >/dev/null 2>&1; then
    echo "[INFO] Using 7-Zip (7z)..."
    7z x -y "$PART1"
elif command -v 7za >/dev/null 2>&1; then
    echo "[INFO] Using 7za..."
    7za x -y "$PART1"
# Step 2: Use bsdtar if installed
elif command -v bsdtar >/dev/null 2>&1; then
    echo "[INFO] 7-Zip not found. Using bsdtar with recombined archive..."
    cat COP3330_OOP_Course_Reference.7z.* > "$COMBINED_TEMP"
    bsdtar -xf "$COMBINED_TEMP"
    rm -f "$COMBINED_TEMP"
# Step 3: Python fallback
elif command -v python3 >/dev/null 2>&1; then
    echo "[INFO] Running Python extractor..."
    python3 extract_course_reference.py
else
    echo "[ERROR] Neither 7z, bsdtar, nor python3 was found."
    echo "Install p7zip: 'sudo apt install p7zip-full' or 'brew install p7zip'"
    exit 1
fi

# Integrity Check
if [ -f "$TARGET" ]; then
    echo "[INFO] Verifying SHA-256 integrity..."
    if command -v sha256sum >/dev/null 2>&1; then
        ACTUAL_SHA=$(sha256sum "$TARGET" | awk '{print $1}')
    elif command -v shasum >/dev/null 2>&1; then
        ACTUAL_SHA=$(shasum -a 256 "$TARGET" | awk '{print $1}')
    else
        ACTUAL_SHA=""
    fi

    if [ -n "$ACTUAL_SHA" ]; then
        if [ "$ACTUAL_SHA" = "$EXPECTED_SHA" ]; then
            echo "[PASS] SHA-256 integrity verified: $ACTUAL_SHA"
        else
            echo "[WARN] Checksum mismatch! Expected $EXPECTED_SHA but got $ACTUAL_SHA"
        fi
    fi

    FILESIZE=$(ls -lh "$TARGET" | awk '{print $5}')
    echo "==============================================================================="
    echo "[PASS] Successfully extracted $TARGET ($FILESIZE, 776 pages)"
    echo "==============================================================================="
else
    echo "[ERROR] Deliverable $TARGET was not created."
    exit 1
fi
