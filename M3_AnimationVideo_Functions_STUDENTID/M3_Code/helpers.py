"""
Reusable Helper Functions and Components for M3 Animation Video
Contains:
 - Mathematical definitions (exact SymPy & numerical NumPy)
 - Labelled coordinate axes with consistent scale
 - Roller-coaster car asset (VGroup)
 - Section headers, step banners, and title cards
 - Math/Text abstraction with automatic LaTeX detection
 - BaseScene supporting silent pacing, gTTS voiceover, and recorded audio
"""

import os
import shutil
import numpy as np
import sympy as sp
from manim import *

from config import (
    COLOR_BG, COLOR_TEXT, COLOR_INPUT, COLOR_OUTPUT, COLOR_CURVE,
    COLOR_INTERCEPT, COLOR_TURNING, COLOR_AID, COLOR_SECONDARY,
    FONT_SIZE_TITLE, FONT_SIZE_SUBTITLE, FONT_SIZE_HEADING,
    FONT_SIZE_BODY, FONT_SIZE_MATH, FONT_SIZE_LABEL, FONT_SIZE_SMALL,
    X_MIN, X_MAX, X_STEP, Y_MIN, Y_MAX, Y_STEP,
    STUDENT_NAME, STUDENT_ID, VIDEO_TITLE, VIDEO_SUBTITLE,
    VOICE_MODE
)

# -------------------------------------------------------------------------
# Mathematical Definitions (Shared single source of truth)
# -------------------------------------------------------------------------
x_sym = sp.Symbol('x', real=True)
f_sympy = x_sym**3 - 3*x_sym

def f_func(x):
    """Numerical evaluation of f(x) = x^3 - 3x."""
    return float(x)**3 - 3.0*float(x)

TABLE_POINTS = [
    (-2.0, -2.0),
    (-float(np.sqrt(3)), 0.0),
    (-1.0, 2.0),
    (0.0, 0.0),
    (1.0, -2.0),
    (float(np.sqrt(3)), 0.0),
    (2.0, 2.0),
]

ROOTS = [-float(np.sqrt(3)), 0.0, float(np.sqrt(3))]
LOCAL_MAX = (-1.0, 2.0)
LOCAL_MIN = (1.0, -2.0)

# Check LaTeX availability on current system
HAS_LATEX = (shutil.which("latex") is not None) or (shutil.which("pdflatex") is not None)

def MathOrText(tex_str, plain_str=None, font_size=FONT_SIZE_MATH, color=COLOR_TEXT, **kwargs):
    """
    Renders MathTex if LaTeX is installed on the system;
    gracefully falls back to unicode Text if LaTeX is not installed.
    Guarantees no crash regardless of LaTeX installation status.
    """
    if HAS_LATEX:
        try:
            return MathTex(tex_str, font_size=font_size, color=color, **kwargs)
        except Exception:
            pass
    # Fallback to Text
    display_str = plain_str if plain_str is not None else tex_to_unicode(tex_str)
    return Text(display_str, font_size=font_size, color=color, **kwargs)

def tex_to_unicode(s):
    """Simple converter of common LaTeX expressions to clean unicode for Text."""
    replacements = [
        (r"\mathbb{R}", "ℝ"),
        (r"\to", "→"),
        (r"\in", "∈"),
        (r"\pm", "±"),
        (r"\sqrt{3}", "√3"),
        (r"\sqrt{", "√("),
        (r"^3", "³"),
        (r"^2", "²"),
        (r"\infty", "∞"),
        (r"\cdot", "·"),
        (r"\approx", "≈"),
        (r"\\", "\n"),
        ("{", ""),
        ("}", ""),
        ("$", ""),
    ]
    res = s
    for old, new in replacements:
        res = res.replace(old, new)
    return res

# -------------------------------------------------------------------------
# Reusable Visual Components
# -------------------------------------------------------------------------
def get_standard_axes(
    x_range=(X_MIN, X_MAX, X_STEP),
    y_range=(Y_MIN, Y_MAX, Y_STEP),
    x_length=6.5,
    y_length=6.0,
    include_numbers=True
):
    """Returns standardized coordinate axes with arrows, ticks, and labels."""
    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        tips=True,
        axis_config={
            "color": COLOR_AID,
            "stroke_width": 2.5,
            "include_numbers": False,
        }
    )
    labels = VGroup()
    # Add axis name labels
    x_label = MathOrText("x", "x", font_size=FONT_SIZE_LABEL, color=COLOR_INPUT).next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)
    y_label = MathOrText("y", "y", font_size=FONT_SIZE_LABEL, color=COLOR_OUTPUT).next_to(axes.y_axis.get_end(), UP, buff=0.15)
    labels.add(x_label, y_label)

    if include_numbers:
        for x_val in range(int(x_range[0]), int(x_range[1]) + 1, int(x_range[2])):
            if x_val != 0:
                t = Text(str(x_val), font_size=FONT_SIZE_LABEL, color=COLOR_AID)
                t.next_to(axes.c2p(x_val, 0), DOWN, buff=0.15)
                labels.add(t)
        for y_val in range(int(y_range[0]), int(y_range[1]) + 1, int(y_range[2])):
            if y_val != 0:
                t = Text(str(y_val), font_size=FONT_SIZE_LABEL, color=COLOR_AID)
                t.next_to(axes.c2p(0, y_val), LEFT, buff=0.15)
                labels.add(t)

    return axes, labels

def get_curve(axes, x_min=-2.25, x_max=2.25, color=COLOR_CURVE, stroke_width=4.5):
    """Returns the function curve f(x) = x^3 - 3x plotted on the given axes."""
    return axes.plot(
        lambda x: f_func(x),
        x_range=[x_min, x_max],
        color=color,
        stroke_width=stroke_width
    )

def create_roller_coaster_car(color=COLOR_OUTPUT, scale=0.4):
    """
    Creates a styled 2D roller-coaster car shape:
    Car body, windshield, two wheels, and a small passenger head.
    """
    # Body
    body = RoundedRectangle(
        corner_radius=0.12,
        height=0.45,
        width=0.9,
        fill_color=color,
        fill_opacity=1.0,
        stroke_color=WHITE,
        stroke_width=2.0
    )
    # Windshield
    windshield = Polygon(
        [-0.15, 0.225, 0],
        [0.35, 0.225, 0],
        [0.2, 0.42, 0],
        [-0.05, 0.42, 0],
        fill_color=COLOR_INPUT,
        fill_opacity=0.85,
        stroke_color=WHITE,
        stroke_width=1.5
    )
    # Wheels
    wheel_left = Circle(radius=0.11, fill_color="#334155", fill_opacity=1.0, stroke_color=WHITE, stroke_width=2.0)
    wheel_left.move_to([-0.25, -0.225, 0])
    wheel_right = Circle(radius=0.11, fill_color="#334155", fill_opacity=1.0, stroke_color=WHITE, stroke_width=2.0)
    wheel_right.move_to([0.25, -0.225, 0])
    
    # Hubcaps
    hub_l = Circle(radius=0.04, fill_color=WHITE, fill_opacity=1.0, stroke_width=0).move_to(wheel_left)
    hub_r = Circle(radius=0.04, fill_color=WHITE, fill_opacity=1.0, stroke_width=0).move_to(wheel_right)

    car = VGroup(body, windshield, wheel_left, wheel_right, hub_l, hub_r)
    car.scale(scale)
    return car

def create_title_card():
    """Generates the 4-second title frame."""
    title = Text(VIDEO_TITLE, font_size=FONT_SIZE_TITLE, color=WHITE, weight=BOLD)
    subtitle = Text(VIDEO_SUBTITLE, font_size=FONT_SIZE_SUBTITLE, color=COLOR_CURVE)
    formula = MathOrText(r"f(x) = x^3 - 3x", "f(x) = x³ - 3x", font_size=FONT_SIZE_HEADING, color=COLOR_OUTPUT)
    
    divider = Line(LEFT * 4, RIGHT * 4, color=COLOR_AID, stroke_width=2)
    
    meta_name = Text(f"Student: {STUDENT_NAME}", font_size=FONT_SIZE_LABEL, color=COLOR_INPUT)
    meta_id = Text(f"ID: {STUDENT_ID}", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING)
    meta_course = Text("Linear Algebra & Calculus (M3)", font_size=FONT_SIZE_SMALL, color=COLOR_AID)
    meta_group = VGroup(meta_name, Text(" | ", font_size=FONT_SIZE_LABEL, color=COLOR_AID), meta_id).arrange(RIGHT, buff=0.3)
    
    card = VGroup(title, subtitle, formula, divider, meta_group, meta_course).arrange(DOWN, buff=0.35)
    return card

def create_step_badge(step_num, title_text):
    """Creates a top banner for worked example steps."""
    badge = RoundedRectangle(corner_radius=0.15, height=0.6, width=1.5, fill_color=COLOR_INPUT, fill_opacity=1.0, stroke_width=0)
    badge_txt = Text(f"Step {step_num}", font_size=FONT_SIZE_SMALL, color=WHITE, weight=BOLD).move_to(badge)
    step_group = VGroup(badge, badge_txt)
    
    title = Text(title_text, font_size=FONT_SIZE_HEADING, color=WHITE, weight=BOLD)
    header = VGroup(step_group, title).arrange(RIGHT, buff=0.3)
    header.to_corner(UL, buff=0.5)
    return header

# -------------------------------------------------------------------------
# BaseScene with Voiceover & Pacing Abstraction
# -------------------------------------------------------------------------
class BaseM3Scene(Scene):
    """
    Standard Base Scene for all M3 animation scenes.
    Sets background color and manages beat narration and timing.
    """
    def setup(self):
        self.camera.background_color = COLOR_BG

    def play_beat(self, beat_text, *animations, wait_time=0.6, run_time=None, **kwargs):
        """
        Plays animations synchronized with narration beat.
        If VOICE_MODE == 'silent', uses natural speaking pace (~140 wpm, ~2.3 words/sec).
        """
        words = len(beat_text.split())
        calculated_duration = max(2.5, words / 2.3)
        actual_run_time = run_time if run_time is not None else min(calculated_duration - 0.4, 4.0)

        if len(animations) > 0:
            self.play(*animations, run_time=actual_run_time, **kwargs)
            remaining_wait = max(wait_time, calculated_duration - actual_run_time)
            self.wait(remaining_wait)
        else:
            self.wait(calculated_duration)
