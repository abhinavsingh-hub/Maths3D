"""
Configuration for M3 Animation Video: Single-Variable Functions & Graphs
Project: f(x) = x^3 - 3x
Student: Abhinav Singh (ID: E25B070774)
Course: Linear Algebra & Calculus (M3)
"""

# Student & Video Metadata
STUDENT_NAME = "Abhinav Singh"
STUDENT_ID = "E25B070774"
VIDEO_TITLE = "Single-Variable Functions & Graphs"
VIDEO_SUBTITLE = "Reading a function's graph like a map"
CONCEPT_NAME = "Single-variable functions & graphs"

# Visual Style & Color Scheme
COLOR_BG = "#111418"             # Dark-grey background
COLOR_TEXT = "#FFFFFF"           # White main text
COLOR_INPUT = "#3B82F6"          # BLUE for input x
COLOR_OUTPUT = "#F97316"         # ORANGE for output f(x)
COLOR_CURVE = "#14B8A6"          # TEAL for function curve
COLOR_INTERCEPT = "#22C55E"      # GREEN for roots and intercepts
COLOR_TURNING = "#EAB308"        # YELLOW for turning points (local min/max)
COLOR_AID = "#94A3B8"            # GREY for symmetry lines and secondary aids
COLOR_SECONDARY = "#A855F7"      # PURPLE for secondary highlights
COLOR_RED = "#EF4444"            # RED for warnings / non-example lines

# Fonts & Typography Sizes (large and legible for 1080p, >= 32pt)
FONT_SIZE_TITLE = 48
FONT_SIZE_SUBTITLE = 36
FONT_SIZE_HEADING = 42
FONT_SIZE_BODY = 36
FONT_SIZE_MATH = 42
FONT_SIZE_LABEL = 32
FONT_SIZE_SMALL = 28

# Standard Coordinate Axes Range (consistent across all scenes)
X_MIN, X_MAX, X_STEP = -3.0, 3.0, 1.0
Y_MIN, Y_MAX, Y_STEP = -4.0, 4.0, 1.0

# Production Video Settings (16:9, 1080p, 30fps)
PRODUCTION_PIXEL_WIDTH = 1920
PRODUCTION_PIXEL_HEIGHT = 1080
PRODUCTION_FPS = 30

# Preview Video Settings (480p, 15fps)
PREVIEW_PIXEL_WIDTH = 854
PREVIEW_PIXEL_HEIGHT = 480
PREVIEW_FPS = 15

# Voice-over & Audio Mode
# "silent": Default for student live presentation or external recording.
#           Paces every beat naturally (~140 wpm) so visual timing aligns with the script.
# "recorded": Plays user's own recorded audio/sceneN.wav.
# "gtts": Uses Google Text-to-Speech via manim-voiceover.
VOICE_MODE = "silent"

# Target timing
TARGET_DURATION_SECONDS = 305    # ~5:05
MAX_ALLOWED_SECONDS = 420        # Hard maximum 7 minutes
