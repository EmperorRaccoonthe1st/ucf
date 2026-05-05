#!/bin/bash
MODULES_DIR="/home/owen/ucf/f/s2/STA/final/plan/NEW_EXAM_PLAN/isolated_tests/modules"
CERTIFIED_DIR="/home/owen/ucf/f/s2/STA/final/plan/NEW_EXAM_PLAN/isolated_tests/certified"
TEST_TEX="/home/owen/ucf/f/s2/STA/final/plan/NEW_EXAM_PLAN/isolated_tests/test.tex"
STYLE_GUIDE="/home/owen/ucf/f/s2/STA/final/plan/NEW_EXAM_PLAN/style_guide.tex"

modules=(
    "ans_mod_2.tex" "ans_mod_3.tex"
    "ans_mod_4.tex" "ans_mod_5.tex" "ans_mod_6.tex"
)

for mod in "${modules[@]}"; do
    echo "Processing $mod..."
    
    # Create test wrapper
    cat <<EOF > "$TEST_TEX"
\documentclass[11pt]{article}
\input{$STYLE_GUIDE}
\begin{document}
\input{$MODULES_DIR/$mod}
\end{document}
EOF

    # Compile with Tectonic
    if tectonic "$TEST_TEX"; then
        echo "$mod compiled successfully."
        # Move to certified
        mv "$MODULES_DIR/$mod" "$CERTIFIED_DIR/$mod"
    else
        echo "FAILED to compile $mod."
        exit 1
    fi
done

echo "Remaining modules certified."
