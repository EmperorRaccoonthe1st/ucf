.PHONY: all compile review clean

# Default target compiles analysis.pdf
all: compile

compile: draft.md compile_analysis.py
	python3 compile_analysis.py

# Rasterize pages to PNG images for visual inspection in terminal or image viewer
review: compile
	@mkdir -p /tmp/analysis_review
	pdftoppm -png -r 150 analysis.pdf /tmp/analysis_review/page
	@echo "[OK] Rendered analysis pages to /tmp/analysis_review/page-*.png"

clean:
	rm -f analysis.pdf
	rm -rf /tmp/analysis_review
