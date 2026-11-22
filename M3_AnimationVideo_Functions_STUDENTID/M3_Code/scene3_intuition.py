"""
Scene 3: Visual Intuition (1:15 - 2:30)
Concept: Function machine, table of values, continuous graph tracing, vertical line test.
Mathematics: Arithmetic evaluation, points (x, f(x)), continuity, and vertical line test.
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
    BaseM3Scene, f_func, get_standard_axes, get_curve, MathOrText
)
from narration import NARRATION

NARR = NARRATION["scene3"]

class Scene3Intuition(BaseM3Scene):
    def construct(self):
        # -------------------------------------------------------------
        # Part 1: Header & Function Machine Box
        # -------------------------------------------------------------
        header = Text("Function Machine & Discrete Values", font_size=FONT_SIZE_HEADING, color=WHITE, weight=BOLD)
        header.to_edge(UP, buff=0.45)
        self.play(Write(header), run_time=0.8)

        # Machine Body
        machine_box = RoundedRectangle(
            corner_radius=0.25, height=2.6, width=4.8,
            fill_color="#1E293B", fill_opacity=0.95, stroke_color=COLOR_CURVE, stroke_width=3
        ).shift(UP * 0.2)
        machine_label = Text("Function Machine f", font_size=FONT_SIZE_BODY, color=COLOR_CURVE, weight=BOLD).next_to(machine_box.get_top(), DOWN, buff=0.25)
        machine_rule = Text("f(x) = x³ - 3x", font_size=FONT_SIZE_BODY, color=WHITE).next_to(machine_label, DOWN, buff=0.15)
        machine_group = VGroup(machine_box, machine_label, machine_rule)

        # Input number 2
        input_num = Text("x = 2", font_size=FONT_SIZE_HEADING, color=COLOR_INPUT, weight=BOLD)
        input_num.move_to(LEFT * 5.2 + UP * 0.2)
        in_arrow = Arrow(LEFT * 4.4 + UP * 0.2, machine_box.get_left(), color=COLOR_INPUT, stroke_width=3)

        # Beat 0: "Think of f as a machine. Feed in 2."
        # Mathematical concept: Input substitution into the rule.
        self.play_beat(
            NARR[0],
            FadeIn(machine_group),
            FadeIn(input_num, shift=RIGHT * 0.5),
            GrowArrow(in_arrow),
            run_time=2.5
        )

        # Slide input into the machine
        self.play(
            input_num.animate.move_to(machine_box.get_center() + UP * 0.3).set_opacity(0),
            FadeOut(in_arrow),
            run_time=1.0
        )

        # Internal calculation lines
        calc1 = Text("1. Cube: 2³ = 8", font_size=FONT_SIZE_LABEL, color=COLOR_INPUT)
        calc2 = Text("2. Multiply: 3(2) = 6", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING)
        calc3 = Text("3. Subtract: 8 - 6 = 2", font_size=FONT_SIZE_LABEL, color=COLOR_OUTPUT, weight=BOLD)
        calcs = VGroup(calc1, calc2, calc3).arrange(DOWN, buff=0.15).move_to(machine_box.get_center() + DOWN * 0.1)

        # Output number 2 exits to the right
        out_arrow = Arrow(machine_box.get_right(), RIGHT * 4.4 + UP * 0.2, color=COLOR_OUTPUT, stroke_width=3)
        output_num = Text("f(2) = 2", font_size=FONT_SIZE_HEADING, color=COLOR_OUTPUT, weight=BOLD).move_to(RIGHT * 5.2 + UP * 0.2)
        coord_pair = Text("Point on Graph: (2, 2)", font_size=FONT_SIZE_LABEL, color=COLOR_INTERCEPT, weight=BOLD).next_to(machine_box, DOWN, buff=0.4)

        # Beat 1: "Cube it: eight. Subtract three times two, which is six. Out comes 2. So the pair two, two is a point on the graph."
        # Mathematical concept: Arithmetic operations produce the coordinate pair (x, f(x)).
        self.play_beat(
            NARR[1],
            FadeIn(calcs, shift=DOWN * 0.2),
            GrowArrow(out_arrow),
            FadeIn(output_num, shift=RIGHT * 0.4),
            FadeIn(coord_pair, shift=UP * 0.2),
            run_time=4.5
        )

        # Clean machine before table & axes
        self.play(
            FadeOut(machine_group),
            FadeOut(calcs),
            FadeOut(out_arrow),
            FadeOut(output_num),
            FadeOut(coord_pair),
            FadeOut(header),
            run_time=0.8
        )

        # -------------------------------------------------------------
        # Part 2: Table of Values & Discrete Points on Axes
        # Left side: Table | Right side: Axes
        # -------------------------------------------------------------
        axes, axis_labels = get_standard_axes(x_length=5.5, y_length=5.0)
        axes_group = VGroup(axes, axis_labels).shift(RIGHT * 3.2 + DOWN * 0.2)

        # Table Layout
        table_title = Text("Table of Values", font_size=FONT_SIZE_LABEL, color=WHITE, weight=BOLD).move_to(LEFT * 4.0 + UP * 2.3)
        col_headers = VGroup(
            Text("x", font_size=FONT_SIZE_LABEL, color=COLOR_INPUT, weight=BOLD),
            Text("f(x)", font_size=FONT_SIZE_LABEL, color=COLOR_OUTPUT, weight=BOLD)
        ).arrange(RIGHT, buff=1.4).next_to(table_title, DOWN, buff=0.25)
        table_line = Line(LEFT * 5.4, LEFT * 2.6, color=COLOR_AID, stroke_width=2).next_to(col_headers, DOWN, buff=0.15)

        table_static = VGroup(table_title, col_headers, table_line)
        self.play(
            Create(axes), Write(axis_labels),
            FadeIn(table_static),
            run_time=1.5
        )

        # Row entries and corresponding points
        discrete_data = [
            (-2, -2),
            (-1, 2),
            (0, 0),
            (1, -2),
            (2, 2)
        ]

        table_rows = []
        axes_dots = []
        dot_labels = []

        start_y = table_line.get_center()[1] - 0.4
        for i, (xv, yv) in enumerate(discrete_data):
            tx = Text(str(xv), font_size=FONT_SIZE_LABEL, color=COLOR_INPUT).move_to([-4.7, start_y - i * 0.55, 0])
            ty = Text(str(yv), font_size=FONT_SIZE_LABEL, color=COLOR_OUTPUT).move_to([-3.3, start_y - i * 0.55, 0])
            table_rows.append(VGroup(tx, ty))

            # Dot on axes
            dot_color = COLOR_INTERCEPT if yv == 0 else (COLOR_TURNING if abs(yv) == 2 and abs(xv) == 1 else COLOR_OUTPUT)
            dot = Dot(axes.c2p(xv, yv), color=dot_color, radius=0.1)
            lbl = Text(f"({xv}, {yv})", font_size=FONT_SIZE_SMALL, color=WHITE)
            lbl.next_to(dot, UR if yv >= 0 else DR, buff=0.12)
            axes_dots.append(dot)
            dot_labels.append(lbl)

        # Beat 2: "Let's try more inputs: minus 2 gives minus 2, minus 1 gives 2, 0 gives 0, 1 gives minus 2."
        # Mathematical concept: Populating sample points across the domain.
        self.play_beat(
            NARR[2],
            FadeIn(table_rows[0]), FadeIn(axes_dots[0]), FadeIn(dot_labels[0]),
            FadeIn(table_rows[1]), FadeIn(axes_dots[1]), FadeIn(dot_labels[1]),
            FadeIn(table_rows[2]), FadeIn(axes_dots[2]), FadeIn(dot_labels[2]),
            FadeIn(table_rows[3]), FadeIn(axes_dots[3]), FadeIn(dot_labels[3]),
            run_time=4.5
        )

        # Beat 3: "Each pair becomes a point, x across and f of x up."
        # Show final row (2, 2) with explicit across-and-up guidance
        h_guideline = DashedLine(axes.c2p(0, 0), axes.c2p(2, 0), color=COLOR_INPUT, stroke_width=2.5)
        v_guideline = DashedLine(axes.c2p(2, 0), axes.c2p(2, 2), color=COLOR_OUTPUT, stroke_width=2.5)

        self.play_beat(
            NARR[3],
            FadeIn(table_rows[4]),
            Create(h_guideline),
            Create(v_guideline),
            FadeIn(axes_dots[4]),
            FadeIn(dot_labels[4]),
            run_time=3.5
        )
        self.play(FadeOut(h_guideline), FadeOut(v_guideline), run_time=0.5)

        # -------------------------------------------------------------
        # Part 3: Continuous Slider & Curve Tracing
        # -------------------------------------------------------------
        # Remove table and shift axes to center
        self.play(
            FadeOut(table_static),
            *[FadeOut(r) for r in table_rows],
            *[FadeOut(lbl) for lbl in dot_labels],
            axes_group.animate.move_to(ORIGIN),
            *[dot.animate.shift(LEFT * 3.2 + UP * 0.2) for dot in axes_dots],
            run_time=1.0
        )

        curve = get_curve(axes, x_min=-2.2, x_max=2.2, color=COLOR_CURVE, stroke_width=4.5)

        # Dynamic ValueTracker for slider
        x_tracker = ValueTracker(-2.2)

        slider_x_dot = always_redraw(lambda: Dot(axes.c2p(x_tracker.get_value(), 0), color=COLOR_INPUT, radius=0.09))
        curve_dot = always_redraw(lambda: Dot(axes.c2p(x_tracker.get_value(), f_func(x_tracker.get_value())), color=COLOR_OUTPUT, radius=0.11))
        vertical_stem = always_redraw(lambda: DashedLine(
            axes.c2p(x_tracker.get_value(), 0),
            axes.c2p(x_tracker.get_value(), f_func(x_tracker.get_value())),
            color=COLOR_AID, stroke_width=2.5
        ))
        live_label = always_redraw(lambda: Text(
            f"x = {x_tracker.get_value():.2f},  f(x) = {f_func(x_tracker.get_value()):.2f}",
            font_size=FONT_SIZE_LABEL, color=WHITE
        ).to_edge(UP, buff=0.4))

        # Beat 4: "Now let x slide continuously. The dot's height is f of x, and the curve it traces is our roller coaster."
        # Mathematical concept: Continuous extension of discrete points into the graph {(x, f(x)) | x in R}.
        self.add(slider_x_dot, curve_dot, vertical_stem, live_label)
        self.play_beat(
            NARR[4],
            Create(curve, run_time=4.5, rate_func=linear),
            x_tracker.animate.set_value(2.2),
            run_time=4.8
        )
        self.remove(slider_x_dot, curve_dot, vertical_stem, live_label)

        # -------------------------------------------------------------
        # Part 4: Vertical Line Test
        # -------------------------------------------------------------
        v_line = Line(axes.c2p(-2.2, -3.8), axes.c2p(-2.2, 3.8), color=COLOR_TURNING, stroke_width=3.5)
        vlt_banner = Text("Vertical Line Test: Exactly ONE output per input", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING, weight=BOLD)
        vlt_banner.to_edge(UP, buff=0.4)

        # Beat 5: "Notice that a vertical line always cuts the curve exactly once. One input, one output. That is the vertical line test."
        # Mathematical concept: Geometric criterion confirming graph is a single-valued function.
        self.play(FadeIn(vlt_banner), Create(v_line), run_time=1.0)
        self.play_beat(
            NARR[5],
            v_line.animate.move_to(axes.c2p(2.2, 0)),
            run_time=4.2,
            rate_func=linear
        )

        # Clean exit
        self.play(
            FadeOut(axes), FadeOut(axis_labels), FadeOut(curve),
            FadeOut(v_line), FadeOut(vlt_banner),
            *[FadeOut(dot) for dot in axes_dots],
            run_time=0.8
        )
