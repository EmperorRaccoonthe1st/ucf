.PHONY: all document rational review clean

# Default target: builds document.pdf, rational.pdf, and merges into prototype.pdf
all: prototype.pdf

prototype.pdf: compile_rational.py compile_document.py document.md rational.md
	python3 compile_rational.py

document: document.md compile_document.py
	python3 compile_document.py

rational: rational.md compile_rational.py
	python3 compile_rational.py

# Render pages to PNG images for visual inspection in terminal or image viewer
review: all
	@mkdir -p /tmp/prototype_review
	pdftoppm -png -r 150 prototype.pdf /tmp/prototype_review/page
	@echo "[OK] Rendered prototype pages to /tmp/prototype_review/page-*.png"

clean:
	rm -f document.pdf rational.pdf prototype.pdf
	rm -rf /tmp/prototype_review
