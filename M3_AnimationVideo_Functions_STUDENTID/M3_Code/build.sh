#!/usr/bin/env bash
# ==============================================================================
# Build and Render Script for M3 Animation Video
# Single-Variable Functions & Graphs: f(x) = x^3 - 3x
# Student: Abhinav Singh (ID: E25B070774)
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Add Homebrew to PATH if on macOS
if [ -d "/opt/homebrew/bin" ]; then
    export PATH="/opt/homebrew/bin:$PATH"
fi

echo "======================================================================"
echo " M3 Animation Video: Single-Variable Functions & Graphs"
echo " Student: Abhinav Singh | ID: E25B070774"
echo "======================================================================"

# ------------------------------------------------------------------------------
# 1. System Package Dependency Checks
# ------------------------------------------------------------------------------
MISSING_DEPS=0

check_cmd() {
    if ! command -v "$1" &> /dev/null; then
        echo "[-] Missing system dependency: $1"
        MISSING_DEPS=1
    else
        echo "[+] Found system tool: $1 ($(command -v $1))"
    fi
}

check_cmd ffmpeg
check_cmd python3

# Check LaTeX (optional for unicode rendering, recommended for TeX)
if ! command -v latex &> /dev/null && ! command -v pdflatex &> /dev/null; then
    echo "[!] LaTeX (pdflatex/latex) not found on PATH."
    echo "    Note: Our project includes a fallback engine with Unicode math via Pango/Cairo."
    echo "    To install full LaTeX distribution:"
    echo "      - macOS:   brew install --cask basictex  OR  brew install --cask mactex"
    echo "      - Ubuntu:  sudo apt update && sudo apt install -y texlive-full"
    echo "      - Windows: choco install miktex  OR  download MiKTeX / TeX Live"
fi

if [ $MISSING_DEPS -ne 0 ]; then
    echo ""
    echo "ERROR: Please install missing tools:"
    echo "  - macOS:   brew install ffmpeg pango cairo"
    echo "  - Ubuntu:  sudo apt update && sudo apt install -y ffmpeg libpango1.0-dev libcairo2-dev"
    echo "  - Windows: choco install ffmpeg"
    exit 1
fi

# Locate Python environment
if [ -d ".venv" ]; then
    PYTHON=".venv/bin/python3"
    MANIM=".venv/bin/manim"
    PYTEST=".venv/bin/pytest"
else
    PYTHON="python3"
    MANIM="manim"
    PYTEST="pytest"
fi

# ------------------------------------------------------------------------------
# 2. Mathematical Verification Tests (Mandatory SymPy/Pytest)
# ------------------------------------------------------------------------------
echo ""
echo "[*] Step 1: Running SymPy Mathematical Verification Tests..."
$PYTEST tests/test_math.py -v
if [ $? -ne 0 ]; then
    echo "FATAL: Math verification failed! Halting build."
    exit 1
fi
echo "[+] All mathematical assertions passed successfully."

# ------------------------------------------------------------------------------
# 3. Determine Render Quality (Production vs Preview)
# ------------------------------------------------------------------------------
MODE="${1:-production}"
if [ "$MODE" == "preview" ]; then
    echo ""
    echo "[*] Step 2: Rendering in PREVIEW mode (854x480 @ 15 fps)..."
    RES_FLAGS="-r 854,480 --fps 15"
    QUALITY_DIR="480p15"
else
    echo ""
    echo "[*] Step 2: Rendering in PRODUCTION mode (1920x1080 @ 30 fps)..."
    RES_FLAGS="-r 1920,1080 --fps 30"
    QUALITY_DIR="1080p30"
fi

SCENES=(
    "scene1_hook.py Scene1Hook"
    "scene2_concept.py Scene2Concept"
    "scene3_intuition.py Scene3Intuition"
    "scene4_worked_example.py Scene4WorkedExample"
    "scene5_interpretation.py Scene5Interpretation"
    "scene6_summary.py Scene6Summary"
)

# Render each scene
for item in "${SCENES[@]}"; do
    FILE=$(echo $item | cut -d' ' -f1)
    CLASS=$(echo $item | cut -d' ' -f2)
    echo ""
    echo ">>> Rendering $CLASS from $FILE..."
    $MANIM $RES_FLAGS "$FILE" "$CLASS"
done

# ------------------------------------------------------------------------------
# 4. Generate Storyboard PDF
# ------------------------------------------------------------------------------
echo ""
echo "[*] Step 3: Generating Storyboard.pdf from docs/storyboard.md..."
$PYTHON generate_storyboard_pdf.py

# ------------------------------------------------------------------------------
# 5. Concatenate Rendered Scenes with FFmpeg
# ------------------------------------------------------------------------------
echo ""
echo "[*] Step 4: Stitching scenes into final video..."

CONCAT_LIST="concat_list.txt"
rm -f "$CONCAT_LIST"

SCENE_FILES=(
    "media/videos/scene1_hook/$QUALITY_DIR/Scene1Hook.mp4"
    "media/videos/scene2_concept/$QUALITY_DIR/Scene2Concept.mp4"
    "media/videos/scene3_intuition/$QUALITY_DIR/Scene3Intuition.mp4"
    "media/videos/scene4_worked_example/$QUALITY_DIR/Scene4WorkedExample.mp4"
    "media/videos/scene5_interpretation/$QUALITY_DIR/Scene5Interpretation.mp4"
    "media/videos/scene6_summary/$QUALITY_DIR/Scene6Summary.mp4"
)

for sf in "${SCENE_FILES[@]}"; do
    if [ ! -f "$sf" ]; then
        echo "ERROR: Missing rendered scene file: $sf"
        exit 1
    fi
    echo "file '$sf'" >> "$CONCAT_LIST"
done

OUTPUT_VIDEO="../M3_Video.mp4"
rm -f "$OUTPUT_VIDEO"

# Check for optional background music in music/bg.mp3
BG_MUSIC="music/bg.mp3"
if [ -f "$BG_MUSIC" ]; then
    echo "[+] Detected background music: $BG_MUSIC. Mixing at -25 dB..."
    ffmpeg -y -f concat -safe 0 -i "$CONCAT_LIST" \
        -i "$BG_MUSIC" \
        -filter_complex "[1:a]volume=0.06[music];[0:a][music]amix=inputs=2:duration=first[aout]" \
        -map 0:v -map "[aout]" \
        -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 192k \
        "$OUTPUT_VIDEO"
else
    # Concatenate video and ensure consistent aac audio track
    ffmpeg -y -f concat -safe 0 -i "$CONCAT_LIST" \
        -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 \
        -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest \
        "$OUTPUT_VIDEO"
fi

rm -f "$CONCAT_LIST"

# ------------------------------------------------------------------------------
# 6. Duration Verification & Reporting
# ------------------------------------------------------------------------------
echo ""
echo "======================================================================"
echo " BUILD COMPLETE!"
echo " Output video: $OUTPUT_VIDEO"
echo "======================================================================"

if command -v ffprobe &> /dev/null; then
    DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$OUTPUT_VIDEO")
    DUR_INT=$(printf "%.0f" "$DURATION")
    MINUTES=$((DUR_INT / 60))
    SECONDS=$((DUR_INT % 60))
    echo "Total Video Duration: ${MINUTES}m ${SECONDS}s (${DURATION} seconds)"
    
    if [ $DUR_INT -gt 420 ]; then
        echo "WARNING: Video duration exceeds the hard limit of 7 minutes (420 s)!"
    elif [ $DUR_INT -gt 360 ]; then
        echo "NOTE: Video duration exceeds the recommended 6 minutes (target ~5m 05s)."
    else
        echo "SUCCESS: Duration is within the optimal range (~5 minutes)."
    fi
fi
