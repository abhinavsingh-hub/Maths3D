"""
Scene 2: Concept Introduction (0:35 - 1:15)
Concept: Formal definition of a function, mapping diagrams, domain, codomain, range.
Mathematics: f : X -> Y, each input has exactly one output; f : R -> R, f(x) = x^3 - 3x.
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
from helpers import BaseM3Scene, MathOrText
from narration import NARRATION

NARR = NARRATION["scene2"]

class Scene2Concept(BaseM3Scene):
    def construct(self):
        # -------------------------------------------------------------
        # Part 1: Section Header
        # -------------------------------------------------------------
        header = Text("Definition: Function & Mapping", font_size=FONT_SIZE_HEADING, color=WHITE, weight=BOLD)
        header.to_edge(UP, buff=0.5)
        self.play(Write(header), run_time=0.8)

        # -------------------------------------------------------------
        # Part 2: Two-Set Mapping Diagram (X -> Y)
        # -------------------------------------------------------------
        # Left set oval X (Domain)
        oval_x = Ellipse(width=2.4, height=4.0, color=COLOR_INPUT, stroke_width=3.0).shift(LEFT * 3.5 + DOWN * 0.2)
        label_x = Text("Input Set X", font_size=FONT_SIZE_LABEL, color=COLOR_INPUT).next_to(oval_x, UP, buff=0.2)
        
        # Right set oval Y (Codomain)
        oval_y = Ellipse(width=2.8, height=4.4, color=COLOR_SECONDARY, stroke_width=3.0).shift(RIGHT * 3.5 + DOWN * 0.2)
        label_y = Text("Output Set Y", font_size=FONT_SIZE_LABEL, color=COLOR_SECONDARY).next_to(oval_y, UP, buff=0.2)

        # Dots inside X
        dot_x1 = Dot(oval_x.get_center() + UP * 1.0, color=COLOR_INPUT, radius=0.09)
        dot_x2 = Dot(oval_x.get_center(), color=COLOR_INPUT, radius=0.09)
        dot_x3 = Dot(oval_x.get_center() + DOWN * 1.0, color=COLOR_INPUT, radius=0.09)
        
        txt_x1 = Text("x₁", font_size=FONT_SIZE_SMALL, color=WHITE).next_to(dot_x1, LEFT, buff=0.15)
        txt_x2 = Text("x₂", font_size=FONT_SIZE_SMALL, color=WHITE).next_to(dot_x2, LEFT, buff=0.15)
        txt_x3 = Text("x₃", font_size=FONT_SIZE_SMALL, color=WHITE).next_to(dot_x3, LEFT, buff=0.15)

        # Dots inside Y
        dot_y1 = Dot(oval_y.get_center() + UP * 1.2, color=COLOR_OUTPUT, radius=0.09)
        dot_y2 = Dot(oval_y.get_center() + UP * 0.1, color=COLOR_OUTPUT, radius=0.09)
        dot_y3 = Dot(oval_y.get_center() + DOWN * 1.0, color=COLOR_OUTPUT, radius=0.09)
        dot_y4 = Dot(oval_y.get_center() + DOWN * 1.6, color=COLOR_AID, radius=0.07)

        txt_y1 = Text("f(x₁)", font_size=FONT_SIZE_SMALL, color=COLOR_OUTPUT).next_to(dot_y1, RIGHT, buff=0.15)
        txt_y2 = Text("f(x₂)", font_size=FONT_SIZE_SMALL, color=COLOR_OUTPUT).next_to(dot_y2, RIGHT, buff=0.15)
        txt_y3 = Text("f(x₃)", font_size=FONT_SIZE_SMALL, color=COLOR_OUTPUT).next_to(dot_y3, RIGHT, buff=0.15)

        # Directed mapping arrows
        arrow1 = Arrow(dot_x1.get_center(), dot_y1.get_center(), color=COLOR_CURVE, buff=0.12, stroke_width=3.0)
        arrow2 = Arrow(dot_x2.get_center(), dot_y2.get_center(), color=COLOR_CURVE, buff=0.12, stroke_width=3.0)
        arrow3 = Arrow(dot_x3.get_center(), dot_y3.get_center(), color=COLOR_CURVE, buff=0.12, stroke_width=3.0)

        # Center rule badge
        rule_box = RoundedRectangle(corner_radius=0.15, height=1.0, width=2.8, fill_color="#0F172A", fill_opacity=0.9, stroke_color=COLOR_CURVE, stroke_width=2)
        rule_text = MathOrText(r"f : X \to Y", "f : X → Y", font_size=FONT_SIZE_HEADING, color=WHITE).move_to(rule_box)
        rule_group = VGroup(rule_box, rule_text).shift(DOWN * 0.2)

        # Beat 0: "A function f from a set X to a set Y is a rule that assigns to each input x in X exactly one output, written f of x, in Y."
        # Mathematical concept: Every input has a unique assigned image.
        self.play_beat(
            NARR[0],
            Create(oval_x), Write(label_x),
            Create(oval_y), Write(label_y),
            FadeIn(VGroup(dot_x1, dot_x2, dot_x3, txt_x1, txt_x2, txt_x3)),
            FadeIn(VGroup(dot_y1, dot_y2, dot_y3, dot_y4, txt_y1, txt_y2, txt_y3)),
            FadeIn(rule_group),
            GrowArrow(arrow1), GrowArrow(arrow2), GrowArrow(arrow3),
            run_time=4.0
        )

        # Highlight the uniqueness: no branching
        unique_note = Text("Each input x has EXACTLY ONE arrow", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING)
        unique_note.next_to(rule_group, DOWN, buff=0.35)

        # Beat 1: "We write f from the real numbers to the real numbers."
        real_notation = MathOrText(r"f : \mathbb{R} \to \mathbb{R}", "f : ℝ → ℝ", font_size=FONT_SIZE_HEADING, color=COLOR_TURNING).move_to(rule_box)
        self.play_beat(
            NARR[1],
            FadeIn(unique_note, shift=UP * 0.2),
            Transform(rule_text, real_notation),
            run_time=2.5
        )

        # -------------------------------------------------------------
        # Part 3: Domain, Codomain, and Range Definitions
        # -------------------------------------------------------------
        # Range sub-region highlighting inside Y
        range_subregion = Ellipse(width=2.4, height=3.0, color=COLOR_OUTPUT, fill_color=COLOR_OUTPUT, fill_opacity=0.2, stroke_width=2.0)
        range_subregion.move_to(oval_y.get_center() + UP * 0.1)
        range_badge = Text("Range", font_size=FONT_SIZE_LABEL, color=COLOR_OUTPUT, weight=BOLD).next_to(range_subregion, UP, buff=0.1)

        domain_badge = Text("Domain (Inputs)", font_size=FONT_SIZE_LABEL, color=COLOR_INPUT, weight=BOLD).next_to(oval_x, DOWN, buff=0.2)

        # Beat 2: "The set of allowed inputs is the domain. The set of outputs the rule actually produces is the range."
        self.play_beat(
            NARR[2],
            FadeIn(range_subregion),
            FadeIn(range_badge),
            FadeIn(domain_badge),
            run_time=3.2
        )

        # -------------------------------------------------------------
        # Part 4: Our Specific Function & Learning Goals
        # -------------------------------------------------------------
        self.play(
            FadeOut(oval_x), FadeOut(label_x), FadeOut(domain_badge),
            FadeOut(oval_y), FadeOut(label_y), FadeOut(range_subregion), FadeOut(range_badge),
            FadeOut(dot_x1), FadeOut(dot_x2), FadeOut(dot_x3), FadeOut(txt_x1), FadeOut(txt_x2), FadeOut(txt_x3),
            FadeOut(dot_y1), FadeOut(dot_y2), FadeOut(dot_y3), FadeOut(dot_y4), FadeOut(txt_y1), FadeOut(txt_y2), FadeOut(txt_y3),
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3),
            FadeOut(rule_group), FadeOut(unique_note),
            run_time=0.8
        )

        func_card = RoundedRectangle(corner_radius=0.15, height=1.2, width=8.5, fill_color="#1E293B", fill_opacity=0.9, stroke_color=COLOR_OUTPUT, stroke_width=2.5)
        func_card.shift(UP * 1.5)
        func_math = MathOrText(r"f(x) = x^3 - 3x", "f(x) = x³ - 3x", font_size=FONT_SIZE_TITLE, color=COLOR_OUTPUT).move_to(func_card)
        func_group = VGroup(func_card, func_math)

        # Beat 3: "Our example is f of x equals x cubed minus three x."
        self.play_beat(
            NARR[3],
            FadeIn(func_group, shift=DOWN * 0.3),
            run_time=2.2
        )

        # Roadmap Goals Checklist
        goals_title = Text("What we will read from its graph:", font_size=FONT_SIZE_BODY, color=WHITE, weight=BOLD)
        g1 = Text("1. Domain & Range (allowed inputs and reached heights)", font_size=FONT_SIZE_LABEL, color=COLOR_INPUT)
        g2 = Text("2. Intercepts (crossings on x and y axes)", font_size=FONT_SIZE_LABEL, color=COLOR_INTERCEPT)
        g3 = Text("3. Symmetry (odd 180° origin symmetry)", font_size=FONT_SIZE_LABEL, color=COLOR_AID)
        g4 = Text("4. Turning Points (local peak and valley)", font_size=FONT_SIZE_LABEL, color=COLOR_TURNING)
        g5 = Text("5. End Behaviour (behaviour for huge |x|)", font_size=FONT_SIZE_LABEL, color=COLOR_CURVE)
        
        goals_box = VGroup(goals_title, g1, g2, g3, g4, g5).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        goals_box.next_to(func_group, DOWN, buff=0.4)

        # Beat 4: "By the end, you'll be able to read from its graph where it crosses the axes, its symmetry, its turning points, how it behaves far out to either side, and its domain and range."
        self.play_beat(
            NARR[4],
            FadeIn(goals_box, shift=UP * 0.3),
            run_time=3.8
        )

        # Clean exit
        self.play(FadeOut(header), FadeOut(func_group), FadeOut(goals_box), run_time=0.8)
