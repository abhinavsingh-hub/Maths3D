"""
Scene 1: Hook / Context (0:00 - 0:35)
Concept: Roller-coaster profile as an intuitive hook for single-variable functions.
Mathematics: Each horizontal coordinate x has exactly one height y = f(x) = x^3 - 3x.
Student: Abhinav Singh (ID: E25B070774)
"""

from manim import *
import numpy as np

from config import (
    COLOR_BG, COLOR_TEXT, COLOR_INPUT, COLOR_OUTPUT, COLOR_CURVE,
    COLOR_INTERCEPT, COLOR_TURNING, COLOR_AID, FONT_SIZE_TITLE,
    FONT_SIZE_SUBTITLE, FONT_SIZE_HEADING, FONT_SIZE_BODY,
    FONT_SIZE_LABEL, FONT_SIZE_MATH
)
from helpers import (
    BaseM3Scene, f_func, get_standard_axes, get_curve,
    create_roller_coaster_car, create_title_card, MathOrText
)
from narration import NARRATION

NARR = NARRATION["scene1"]

class Scene1Hook(BaseM3Scene):
    def construct(self):
        # -------------------------------------------------------------
        # Part 1: Mandatory 4-Second Title Card
        # Displays: Title, Subtitle, Student Name, and ID
        # -------------------------------------------------------------
        title_card = create_title_card()
        self.play(FadeIn(title_card, shift=UP * 0.3), run_time=1.0)
        self.wait(3.0)  # Total display time: 4 seconds
        self.play(FadeOut(title_card, shift=DOWN * 0.3), run_time=0.8)

        # -------------------------------------------------------------
        # Part 2: Coordinate Axes & Roller Coaster Track Setup
        # Sets up standard coordinate system: x in [-3, 3], y in [-4, 4]
        # -------------------------------------------------------------
        axes, axis_labels = get_standard_axes()
        curve = get_curve(axes, x_min=-2.2, x_max=2.2, stroke_width=5.5)

        # Track labels
        track_label = Text("Roller-Coaster Track", font_size=FONT_SIZE_LABEL, color=COLOR_CURVE)
        track_label.to_corner(UL, buff=0.6)

        # Beat 0: "Picture a roller coaster. At every point along the ground, the track has exactly one height."
        # Mathematical concept: Input-output relationship along the horizontal ground.
        self.play_beat(
            NARR[0],
            Create(axes),
            Write(axis_labels),
            Create(curve),
            Write(track_label),
            run_time=3.2
        )

        # -------------------------------------------------------------
        # Part 3: Car Animation Along the Track
        # Moves a car smoothly along y = x^3 - 3x illustrating changes in height
        # -------------------------------------------------------------
        car = create_roller_coaster_car(color=COLOR_OUTPUT, scale=0.45)
        # Position car initially at start of curve
        start_pt = axes.c2p(-2.15, f_func(-2.15))
        car.move_to(start_pt)

        # Beat 1: "Slide forward, and the height changes: up, down, and up again."
        # Mathematical concept: Monotonicity and changing sign of gradient.
        self.play_beat(
            NARR[1],
            FadeIn(car, scale=0.8),
            MoveAlongPath(car, curve, run_time=3.5, rate_func=linear)
        )

        # -------------------------------------------------------------
        # Part 4: The Guiding Question
        # Poses the central question: Can one formula describe the whole ride?
        # -------------------------------------------------------------
        question_banner = RoundedRectangle(
            corner_radius=0.15, height=1.0, width=10.0,
            fill_color="#1E293B", fill_opacity=0.9, stroke_color=COLOR_TURNING, stroke_width=2
        ).to_edge(DOWN, buff=0.5)
        question_text = Text(
            "Can a single formula describe that entire ride?",
            font_size=FONT_SIZE_BODY, color=WHITE
        ).move_to(question_banner)
        question_group = VGroup(question_banner, question_text)

        # Beat 2: "Here is the question: could a single formula describe that entire ride?"
        self.play_beat(
            NARR[2],
            FadeIn(question_group, shift=UP * 0.4),
            run_time=2.2
        )

        # -------------------------------------------------------------
        # Part 5: Formula Revelation & Presenter Intro
        # Introduces f(x) = x^3 - 3x and student introduction
        # -------------------------------------------------------------
        formula_badge = RoundedRectangle(
            corner_radius=0.15, height=1.1, width=7.0,
            fill_color="#0F172A", fill_opacity=0.95, stroke_color=COLOR_CURVE, stroke_width=2.5
        ).move_to(question_banner)
        formula_text = MathOrText(
            r"f(x) = x^3 - 3x", "f(x) = x³ - 3x",
            font_size=FONT_SIZE_HEADING, color=COLOR_OUTPUT
        ).move_to(formula_badge)
        formula_group = VGroup(formula_badge, formula_text)

        # Beat 3: "It can. That formula is called a function, and its graph is the picture of the ride."
        self.play_beat(
            NARR[3],
            ReplacementTransform(question_group, formula_group),
            run_time=2.2
        )

        # Roadmap caption
        intro_text = Text(
            "Learn to read a function's graph like a map",
            font_size=FONT_SIZE_LABEL, color=COLOR_INPUT
        ).next_to(formula_badge, UP, buff=0.3)

        # Beat 4: "I'm Abhinav, and in the next five minutes you'll learn to read a function's graph like a map."
        self.play_beat(
            NARR[4],
            FadeIn(intro_text, shift=UP * 0.2),
            run_time=2.0
        )

        # Clean transition
        self.play(
            FadeOut(axes),
            FadeOut(axis_labels),
            FadeOut(curve),
            FadeOut(car),
            FadeOut(track_label),
            FadeOut(formula_group),
            FadeOut(intro_text),
            run_time=0.8
        )
