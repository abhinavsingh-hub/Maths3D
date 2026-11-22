"""
Scene 5: Interpretation (4:00 - 4:40)
Concept: Range, Horizontal Line Test (injectivity), and physical coaster extrema.
Mathematics: Range = R; y = 1 has 3 real solutions (not injective); local extrema.
Student: Abhinav Singh (ID: E25B070774)
"""

from manim import *
import numpy as np
import sympy as sp

from config import (
    COLOR_BG, COLOR_TEXT, COLOR_INPUT, COLOR_OUTPUT, COLOR_CURVE,
    COLOR_INTERCEPT, COLOR_TURNING, COLOR_AID, COLOR_SECONDARY,
    FONT_SIZE_TITLE, FONT_SIZE_SUBTITLE, FONT_SIZE_HEADING,
    FONT_SIZE_BODY, FONT_SIZE_LABEL, FONT_SIZE_SMALL, FONT_SIZE_MATH
)
from helpers import (
    BaseM3Scene, f_func, get_standard_axes, get_curve,
    create_roller_coaster_car, MathOrText, x_sym, f_sympy
)
from narration import NARRATION

NARR = NARRATION["scene5"]

class Scene5Interpretation(BaseM3Scene):
    def construct(self):
        # -------------------------------------------------------------
        # Part 1: Header & Standard Setup
        # -------------------------------------------------------------
        header = Text("Geometric Interpretation: Range & Extrema", font_size=FONT_SIZE_HEADING, color=WHITE, weight=BOLD)
        header.to_edge(UP, buff=0.45)
        self.play(Write(header), run_time=0.8)

        axes, axis_labels = get_standard_axes(x_length=6.2, y_length=5.6)
        axes_group = VGroup(axes, axis_labels).shift(DOWN * 0.15)
        curve = get_curve(axes, x_min=-2.2, x_max=2.2, color=COLOR_CURVE, stroke_width=4.5)

        # Beat 0: "Now let's connect the algebra back to the picture."
        self.play_beat(
            NARR[0],
            Create(axes),
            Write(axis_labels),
            Create(curve),
            run_time=2.5
        )

        # -------------------------------------------------------------
        # Part 2: Range = All Reals (Sweeping Horizontal Line)
        # -------------------------------------------------------------
        h_line = Line(axes.c2p(-2.8, -3.5), axes.c2p(2.8, -3.5), color=COLOR_OUTPUT, stroke_width=3.5)
        range_line = Line(axes.c2p(0, -3.8), axes.c2p(0, 3.8), color=COLOR_OUTPUT, stroke_width=7.0)
        range_banner = Text("Range: Every horizontal line intersects → Range = ℝ", font_size=FONT_SIZE_LABEL, color=COLOR_OUTPUT, weight=BOLD)
        range_banner.next_to(header, DOWN, buff=0.25)

        # Beat 1: "Because the curve is unbroken and runs from far below to far above, every height is reached, so the range is all real numbers."
        self.play_beat(
            NARR[1],
            FadeIn(range_banner),
            Create(h_line),
            Create(range_line),
            h_line.animate.move_to(axes.c2p(0, 3.5)),
            run_time=4.5
        )
        self.play(FadeOut(range_line), FadeOut(range_banner), run_time=0.5)

        # -------------------------------------------------------------
        # Part 3: Horizontal Line Test at y = 1 (Not One-to-One)
        # -------------------------------------------------------------
        # Freeze line at y = 1
        self.play(h_line.animate.move_to(axes.c2p(0, 1.0)).set_color(COLOR_TURNING), run_time=1.0)
        y_val_lbl = Text("y = 1", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING, weight=BOLD).next_to(h_line, RIGHT, buff=0.2)

        # Calculate exact roots of x^3 - 3x - 1 = 0
        roots_y1 = sp.real_roots(f_sympy - 1)
        float_roots = [float(r.evalf()) for r in roots_y1]

        dots_y1 = VGroup()
        for r in float_roots:
            d = Dot(axes.c2p(r, 1.0), color=COLOR_TURNING, radius=0.12)
            dots_y1.add(d)

        not_injective_card = RoundedRectangle(corner_radius=0.15, height=1.1, width=10.5, fill_color="#0F172A", fill_opacity=0.95, stroke_color=COLOR_TURNING, stroke_width=2.5)
        not_injective_t1 = Text("Horizontal Line Test: Cuts 3 times at y = 1", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING, weight=BOLD)
        not_injective_t2 = Text("Three different inputs give output 1  →  NOT One-to-One (Not Injective)", font_size=FONT_SIZE_SMALL, color=WHITE)
        not_injective_group = VGroup(not_injective_t1, not_injective_t2).arrange(DOWN, buff=0.1).move_to(not_injective_card)
        not_injective_box = VGroup(not_injective_card, not_injective_group).to_edge(UP, buff=0.4)

        # Beat 2: "Sweep a horizontal line upward: at height 1 it cuts the graph three times. Three different inputs give the same output, so this function is not one-to-one."
        self.play_beat(
            NARR[2],
            FadeIn(dots_y1),
            Write(y_val_lbl),
            Transform(header, not_injective_box),
            run_time=4.5
        )

        self.play(
            FadeOut(h_line), FadeOut(y_val_lbl), FadeOut(dots_y1),
            FadeOut(header), FadeOut(not_injective_box),
            run_time=0.6
        )

        # -------------------------------------------------------------
        # Part 4: Reconnecting to the Roller Coaster
        # -------------------------------------------------------------
        coaster_title = Text("Roller-Coaster Profile", font_size=FONT_SIZE_HEADING, color=COLOR_CURVE, weight=BOLD).to_edge(UP, buff=0.45)
        car = create_roller_coaster_car(color=COLOR_OUTPUT, scale=0.45)

        # Hill at (-1, 2)
        car.move_to(axes.c2p(-1, 2))
        hill_label = Text("Hill Peak: Height = +2", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING, weight=BOLD).next_to(axes.c2p(-1, 2), UP, buff=0.25)

        # Valley at (1, -2)
        valley_label = Text("Valley: Depth = -2", font_size=FONT_SIZE_LABEL, color=COLOR_OUTPUT, weight=BOLD).next_to(axes.c2p(1, -2), DOWN, buff=0.25)

        # Beat 3: "And for our roller coaster: a hill with peak height 2, a valley of depth minus 2, and then the track climbs forever."
        self.play(FadeIn(coaster_title), FadeIn(car), Write(hill_label), run_time=1.0)
        self.play_beat(
            NARR[3],
            car.animate.move_to(axes.c2p(1, -2)),
            FadeIn(valley_label),
            run_time=3.5
        )

        # Final climb forever
        self.play(
            car.animate.move_to(axes.c2p(2.15, f_func(2.15))),
            run_time=1.5
        )

        # Clean transition
        self.play(
            FadeOut(axes), FadeOut(axis_labels), FadeOut(curve),
            FadeOut(car), FadeOut(hill_label), FadeOut(valley_label),
            FadeOut(coaster_title),
            run_time=0.8
        )
