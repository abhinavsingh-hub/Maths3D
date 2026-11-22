"""
Scene 4: Worked Example (2:30 - 4:00)
Concept: Step-by-step reading and algebraic verification of all key features.
Steps: 1. Domain, 2. Intercepts, 3. Symmetry, 4. Turning Points, 5. End Behaviour.
Student: Abhinav Singh (ID: E25B070774)
"""

from manim import *
import numpy as np

from config import (
    COLOR_BG, COLOR_TEXT, COLOR_INPUT, COLOR_OUTPUT, COLOR_CURVE,
    COLOR_INTERCEPT, COLOR_TURNING, COLOR_AID, COLOR_SECONDARY,
    FONT_SIZE_TITLE, FONT_SIZE_SUBTITLE, FONT_SIZE_HEADING,
    FONT_SIZE_BODY, FONT_SIZE_LABEL, FONT_SIZE_SMALL, FONT_SIZE_MATH
)
from helpers import (
    BaseM3Scene, f_func, get_standard_axes, get_curve,
    create_step_badge, MathOrText
)
from narration import NARRATION

NARR = NARRATION["scene4"]

class Scene4WorkedExample(BaseM3Scene):
    def construct(self):
        # -------------------------------------------------------------
        # Two-Panel Setup
        # Left Panel (x in [-7, -0.5]): Algebra & Explanations
        # Right Panel (x in [0, 6.5]): Coordinate Axes & Graph
        # -------------------------------------------------------------
        axes, axis_labels = get_standard_axes(x_length=5.6, y_length=5.2)
        axes_group = VGroup(axes, axis_labels).shift(RIGHT * 3.3 + DOWN * 0.1)
        curve = get_curve(axes, x_min=-2.2, x_max=2.2, color=COLOR_CURVE, stroke_width=4.5)

        self.play(Create(axes), Write(axis_labels), Create(curve), run_time=1.5)

        # =============================================================
        # STEP 1: DOMAIN
        # =============================================================
        badge1 = create_step_badge(1, "Domain: All Reals")
        alg1_line1 = Text("Formula: f(x) = x³ - 3x", font_size=FONT_SIZE_BODY, color=WHITE)
        alg1_line2 = Text("• Polynomial expression", font_size=FONT_SIZE_LABEL, color=COLOR_AID)
        alg1_line3 = Text("• No division by zero (no fractions)", font_size=FONT_SIZE_LABEL, color=COLOR_AID)
        alg1_line4 = Text("• No even roots (no negative roots)", font_size=FONT_SIZE_LABEL, color=COLOR_AID)
        alg1_res = Text("Domain = (-∞, +∞) = ℝ", font_size=FONT_SIZE_BODY, color=COLOR_INPUT, weight=BOLD)

        alg1_group = VGroup(alg1_line1, alg1_line2, alg1_line3, alg1_line4, alg1_res).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        alg1_group.next_to(badge1, DOWN, buff=0.4).to_edge(LEFT, buff=0.6)

        # Highlight entire x-axis
        domain_line = Line(axes.c2p(-3, 0), axes.c2p(3, 0), color=COLOR_INPUT, stroke_width=7.0)

        # Beat 0: "Step one, the domain. The formula only cubes, multiplies and subtracts. Nothing can break, so every real number is allowed."
        self.play_beat(
            NARR[0],
            FadeIn(badge1),
            FadeIn(alg1_group),
            Create(domain_line),
            run_time=3.5
        )
        self.play(FadeOut(alg1_group), FadeOut(badge1), FadeOut(domain_line), run_time=0.6)

        # =============================================================
        # STEP 2: INTERCEPTS
        # =============================================================
        badge2 = create_step_badge(2, "Intercepts")
        # y-intercept
        y_int_title = Text("y-intercept (set x = 0):", font_size=FONT_SIZE_LABEL, color=WHITE, weight=BOLD)
        y_int_calc = Text("f(0) = 0³ - 3(0) = 0  →  (0, 0)", font_size=FONT_SIZE_LABEL, color=COLOR_INTERCEPT)
        y_int_group = VGroup(y_int_title, y_int_calc).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        y_int_group.next_to(badge2, DOWN, buff=0.3).to_edge(LEFT, buff=0.6)

        dot_origin = Dot(axes.c2p(0, 0), color=COLOR_INTERCEPT, radius=0.12)
        lbl_origin = Text("(0, 0)", font_size=FONT_SIZE_SMALL, color=WHITE).next_to(dot_origin, UR, buff=0.15)

        # Beat 1: "Step two, the intercepts. At x equals 0, f of 0 is 0, so the graph crosses the y-axis at the origin."
        self.play_beat(
            NARR[1],
            FadeIn(badge2),
            FadeIn(y_int_group),
            FadeIn(dot_origin),
            Write(lbl_origin),
            run_time=3.0
        )

        # x-intercepts
        x_int_title = Text("x-intercepts (set f(x) = 0):", font_size=FONT_SIZE_LABEL, color=WHITE, weight=BOLD)
        x_int_1 = Text("x³ - 3x = 0", font_size=FONT_SIZE_LABEL, color=COLOR_OUTPUT)
        x_int_2 = Text("x(x² - 3) = 0  (factor out x)", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING)
        x_int_group1 = VGroup(x_int_title, x_int_1, x_int_2).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        x_int_group1.next_to(y_int_group, DOWN, buff=0.25).align_to(y_int_group, LEFT)

        # Beat 2: "To cross the x-axis, set x cubed minus 3x equal to 0. Factor out x: x times x squared minus 3 equals 0."
        self.play_beat(
            NARR[2],
            FadeIn(x_int_group1),
            run_time=3.0
        )

        x_int_3 = Text("x = 0  or  x² = 3", font_size=FONT_SIZE_LABEL, color=WHITE)
        x_int_4 = Text("x = 0,  ±√3  (≈ ±1.732)", font_size=FONT_SIZE_BODY, color=COLOR_INTERCEPT, weight=BOLD)
        x_int_group2 = VGroup(x_int_3, x_int_4).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        x_int_group2.next_to(x_int_group1, DOWN, buff=0.18).align_to(y_int_group, LEFT)

        sqrt3 = np.sqrt(3)
        dot_r = Dot(axes.c2p(sqrt3, 0), color=COLOR_INTERCEPT, radius=0.12)
        dot_l = Dot(axes.c2p(-sqrt3, 0), color=COLOR_INTERCEPT, radius=0.12)
        lbl_r = Text("(√3, 0)", font_size=FONT_SIZE_SMALL, color=WHITE).next_to(dot_r, UR, buff=0.12)
        lbl_l = Text("(-√3, 0)", font_size=FONT_SIZE_SMALL, color=WHITE).next_to(dot_l, UL, buff=0.12)

        # Beat 3: "So x is 0, or x squared is 3, giving x equal to plus or minus root 3, about 1.73."
        self.play_beat(
            NARR[3],
            FadeIn(x_int_group2),
            FadeIn(dot_r), Write(lbl_r),
            FadeIn(dot_l), Write(lbl_l),
            run_time=3.0
        )

        # Check step
        check_box = Text("Check: f(√3) = (√3)³ - 3√3 = 3√3 - 3√3 = 0 ✓", font_size=FONT_SIZE_SMALL, color=COLOR_INTERCEPT, weight=BOLD)
        check_box.next_to(x_int_group2, DOWN, buff=0.2).align_to(y_int_group, LEFT)

        # Beat 4: "Check: f of root 3 is 3 root 3 minus 3 root 3, which is 0."
        self.play_beat(
            NARR[4],
            FadeIn(check_box),
            run_time=2.5
        )

        self.play(
            FadeOut(badge2), FadeOut(y_int_group), FadeOut(x_int_group1), FadeOut(x_int_group2), FadeOut(check_box),
            FadeOut(dot_origin), FadeOut(lbl_origin), FadeOut(dot_r), FadeOut(lbl_r), FadeOut(dot_l), FadeOut(lbl_l),
            run_time=0.6
        )

        # =============================================================
        # STEP 3: SYMMETRY (ODD FUNCTION)
        # =============================================================
        badge3 = create_step_badge(3, "Symmetry: Odd Function")
        sym_line1 = Text("Test f(-x):", font_size=FONT_SIZE_LABEL, color=WHITE, weight=BOLD)
        sym_line2 = Text("f(-x) = (-x)³ - 3(-x)", font_size=FONT_SIZE_LABEL, color=COLOR_INPUT)
        sym_line3 = Text("     = -x³ + 3x", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING)
        sym_line4 = Text("     = -(x³ - 3x) = -f(x)", font_size=FONT_SIZE_BODY, color=COLOR_OUTPUT, weight=BOLD)
        sym_box = VGroup(sym_line1, sym_line2, sym_line3, sym_line4).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        sym_box.next_to(badge3, DOWN, buff=0.3).to_edge(LEFT, buff=0.6)

        # Beat 5: "Step three, symmetry. Replace x with minus x: minus x cubed plus 3x. That's exactly minus f of x."
        self.play_beat(
            NARR[5],
            FadeIn(badge3),
            FadeIn(sym_box),
            run_time=3.5
        )

        sym_expl = Text("• 180° rotational symmetry about origin", font_size=FONT_SIZE_LABEL, color=WHITE)
        num_chk = Text("Numeric check: f(2) = 2, f(-2) = -2", font_size=FONT_SIZE_LABEL, color=COLOR_INTERCEPT, weight=BOLD)
        sym_bottom = VGroup(sym_expl, num_chk).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        sym_bottom.next_to(sym_box, DOWN, buff=0.25).align_to(sym_box, LEFT)

        # 180-degree rotation of curve about origin
        origin_pt = axes.c2p(0, 0)
        self.play(FadeIn(sym_bottom), run_time=1.0)

        # Beat 6: "This is an odd function, so rotating the graph 180 degrees about the origin leaves it unchanged. Check with numbers: f of 2 is 2, and f of minus 2 is minus 2."
        self.play_beat(
            NARR[6],
            Rotate(curve, angle=PI, about_point=origin_pt, run_time=3.2),
            run_time=3.8
        )

        self.play(FadeOut(badge3), FadeOut(sym_box), FadeOut(sym_bottom), run_time=0.6)

        # =============================================================
        # STEP 4: TURNING POINTS
        # =============================================================
        badge4 = create_step_badge(4, "Turning Points")
        tp_t1 = Text("Table confirmations:", font_size=FONT_SIZE_LABEL, color=WHITE, weight=BOLD)
        tp_t2 = Text("f(-2) = -2  →  f(-1) = 2  →  f(0) = 0", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING)
        tp_t3 = Text("f(0) = 0   →  f(1) = -2  →  f(2) = 2", font_size=FONT_SIZE_LABEL, color=COLOR_OUTPUT)
        tp_group = VGroup(tp_t1, tp_t2, tp_t3).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        tp_group.next_to(badge4, DOWN, buff=0.3).to_edge(LEFT, buff=0.6)

        # Beat 7: "Step four, turning points. Look at the table: f of minus 2 is minus 2, f of minus 1 is 2, then f of 0 is 0, f of 1 is minus 2, f of 2 is 2."
        self.play_beat(
            NARR[7],
            FadeIn(badge4),
            FadeIn(tp_group),
            run_time=3.2
        )

        # Highlight local max and min
        dot_max = Dot(axes.c2p(-1, 2), color=COLOR_TURNING, radius=0.13)
        lbl_max = Text("Local Maximum (-1, 2)", font_size=FONT_SIZE_SMALL, color=COLOR_TURNING, weight=BOLD).next_to(dot_max, UP, buff=0.15)
        dot_min = Dot(axes.c2p(1, -2), color=COLOR_TURNING, radius=0.13)
        lbl_min = Text("Local Minimum (1, -2)", font_size=FONT_SIZE_SMALL, color=COLOR_TURNING, weight=BOLD).next_to(dot_min, DOWN, buff=0.15)

        # Beat 8: "The curve climbs to a peak at minus 1, 2, falls to a valley at 1, minus 2, and climbs again."
        self.play_beat(
            NARR[8],
            FadeIn(dot_max), Write(lbl_max),
            FadeIn(dot_min), Write(lbl_min),
            run_time=3.2
        )

        calc_note_box = RoundedRectangle(corner_radius=0.12, height=1.1, width=6.2, fill_color="#0F172A", fill_opacity=0.9, stroke_color=COLOR_AID, stroke_width=2)
        calc_note_t1 = Text("Why exactly at x = ±1?", font_size=FONT_SIZE_LABEL, color=WHITE, weight=BOLD)
        calc_note_t2 = Text("Calculus (derivatives) will explain why!", font_size=FONT_SIZE_SMALL, color=COLOR_TURNING)
        calc_note = VGroup(calc_note_t1, calc_note_t2).arrange(DOWN, buff=0.1).move_to(calc_note_box)
        calc_group = VGroup(calc_note_box, calc_note).next_to(tp_group, DOWN, buff=0.3).align_to(tp_group, LEFT)

        # Beat 9: "Calculus will later explain exactly why these happen at x equals plus or minus 1."
        self.play_beat(
            NARR[9],
            FadeIn(calc_group, shift=UP * 0.2),
            run_time=2.8
        )

        self.play(
            FadeOut(badge4), FadeOut(tp_group), FadeOut(calc_group),
            FadeOut(dot_max), FadeOut(lbl_max), FadeOut(dot_min), FadeOut(lbl_min),
            run_time=0.6
        )

        # =============================================================
        # STEP 5: END BEHAVIOUR
        # =============================================================
        badge5 = create_step_badge(5, "End Behaviour (x → ±∞)")
        eb_t1 = Text("Dominant Term Analysis:", font_size=FONT_SIZE_LABEL, color=WHITE, weight=BOLD)
        eb_t2 = Text("For large |x|, x³ dominates 3x", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING)
        eb_t3 = Text("f(10) = 10³ - 30 = 970", font_size=FONT_SIZE_LABEL, color=COLOR_INTERCEPT)
        eb_t4 = Text("f(-10) = (-10)³ + 30 = -970", font_size=FONT_SIZE_LABEL, color=COLOR_OUTPUT)
        eb_group = VGroup(eb_t1, eb_t2, eb_t3, eb_t4).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        eb_group.next_to(badge5, DOWN, buff=0.3).to_edge(LEFT, buff=0.6)

        # Beat 10: "Step five, end behaviour. When x is huge, x cubed overwhelms 3x."
        self.play_beat(
            NARR[10],
            FadeIn(badge5),
            FadeIn(eb_group),
            run_time=3.0
        )

        eb_res1 = Text("As x → +∞,  f(x) → +∞  (climbs up)", font_size=FONT_SIZE_LABEL, color=COLOR_INPUT, weight=BOLD)
        eb_res2 = Text("As x → -∞,  f(x) → -∞  (falls down)", font_size=FONT_SIZE_LABEL, color=COLOR_OUTPUT, weight=BOLD)
        eb_res_group = VGroup(eb_res1, eb_res2).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        eb_res_group.next_to(eb_group, DOWN, buff=0.25).align_to(eb_group, LEFT)

        # End arrows on the curve
        arrow_up = Arrow(axes.c2p(2.0, 2.0), axes.c2p(2.3, 3.8), color=COLOR_CURVE, stroke_width=4.5)
        arrow_down = Arrow(axes.c2p(-2.0, -2.0), axes.c2p(-2.3, -3.8), color=COLOR_CURVE, stroke_width=4.5)

        # Beat 11: "So as x grows large and positive, f grows large and positive. As x grows large and negative, f grows large and negative."
        self.play_beat(
            NARR[11],
            FadeIn(eb_res_group),
            GrowArrow(arrow_up),
            GrowArrow(arrow_down),
            run_time=3.5
        )

        # Clean transition
        self.play(
            FadeOut(badge5), FadeOut(eb_group), FadeOut(eb_res_group),
            FadeOut(arrow_up), FadeOut(arrow_down),
            FadeOut(axes), FadeOut(axis_labels), FadeOut(curve),
            run_time=0.8
        )
