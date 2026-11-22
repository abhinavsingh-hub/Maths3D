"""
Scene 6: Summary and Credits (4:40 - 5:10)
Concept: Three key pedagogical takeaways and final academic credits.
Mathematics: Synthesis of input-output rule, graphical sets, and feature reading.
Student: Abhinav Singh (ID: E25B070774)
"""

from manim import *

from config import (
    COLOR_BG, COLOR_TEXT, COLOR_INPUT, COLOR_OUTPUT, COLOR_CURVE,
    COLOR_INTERCEPT, COLOR_TURNING, COLOR_AID, COLOR_SECONDARY,
    FONT_SIZE_TITLE, FONT_SIZE_SUBTITLE, FONT_SIZE_HEADING,
    FONT_SIZE_BODY, FONT_SIZE_LABEL, FONT_SIZE_SMALL,
    STUDENT_NAME, STUDENT_ID
)
from helpers import BaseM3Scene
from narration import NARRATION

NARR = NARRATION["scene6"]

class Scene6Summary(BaseM3Scene):
    def construct(self):
        # -------------------------------------------------------------
        # Part 1: Three Core Takeaways
        # -------------------------------------------------------------
        title = Text("Summary: Three Key Takeaways", font_size=FONT_SIZE_HEADING, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=0.5)

        # Beat 0: "Three takeaways."
        self.play_beat(
            NARR[0],
            Write(title),
            run_time=1.5
        )

        # Card 1: Input-Output Rule
        card1 = RoundedRectangle(corner_radius=0.15, height=1.3, width=11.0, fill_color="#1E293B", fill_opacity=0.9, stroke_color=COLOR_INPUT, stroke_width=2.5)
        c1_num = Text("1", font_size=FONT_SIZE_HEADING, color=COLOR_INPUT, weight=BOLD).move_to(card1.get_left() + RIGHT * 0.5)
        c1_t1 = Text("One Input → Exactly One Output", font_size=FONT_SIZE_BODY, color=WHITE, weight=BOLD)
        c1_t2 = Text("Domain defines allowed inputs; Range defines values actually reached.", font_size=FONT_SIZE_SMALL, color=COLOR_AID)
        c1_txt = VGroup(c1_t1, c1_t2).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(c1_num, RIGHT, buff=0.4)
        c1_group = VGroup(card1, c1_num, c1_txt).move_to(UP * 1.5)

        # Beat 1: "One: a function gives each input exactly one output, and its domain and range say what goes in and what comes out."
        self.play_beat(
            NARR[1],
            FadeIn(c1_group, shift=UP * 0.3),
            run_time=3.5
        )

        # Card 2: Geometric Graph & Vertical Line Test
        card2 = RoundedRectangle(corner_radius=0.15, height=1.3, width=11.0, fill_color="#1E293B", fill_opacity=0.9, stroke_color=COLOR_CURVE, stroke_width=2.5)
        c2_num = Text("2", font_size=FONT_SIZE_HEADING, color=COLOR_CURVE, weight=BOLD).move_to(card2.get_left() + RIGHT * 0.5)
        c2_t1 = Text("Graph as Pairs (x, f(x)) & Vertical Line Test", font_size=FONT_SIZE_BODY, color=WHITE, weight=BOLD)
        c2_t2 = Text("A vertical line intersects at most once everywhere along the domain.", font_size=FONT_SIZE_SMALL, color=COLOR_AID)
        c2_txt = VGroup(c2_t1, c2_t2).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(c2_num, RIGHT, buff=0.4)
        c2_group = VGroup(card2, c2_num, c2_txt).move_to(ORIGIN)

        # Beat 2: "Two: the graph is every point x, f of x, and the vertical line test checks it."
        self.play_beat(
            NARR[2],
            FadeIn(c2_group, shift=UP * 0.3),
            run_time=3.5
        )

        # Card 3: Reading Features & Analytical Substitution
        card3 = RoundedRectangle(corner_radius=0.15, height=1.3, width=11.0, fill_color="#1E293B", fill_opacity=0.9, stroke_color=COLOR_TURNING, stroke_width=2.5)
        c3_num = Text("3", font_size=FONT_SIZE_HEADING, color=COLOR_TURNING, weight=BOLD).move_to(card3.get_left() + RIGHT * 0.5)
        c3_t1 = Text("Read & Verify by Substitution", font_size=FONT_SIZE_BODY, color=WHITE, weight=BOLD)
        c3_t2 = Text("Intercepts, symmetry, turning points, and end behaviour checked algebraically.", font_size=FONT_SIZE_SMALL, color=COLOR_AID)
        c3_txt = VGroup(c3_t1, c3_t2).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(c3_num, RIGHT, buff=0.4)
        c3_group = VGroup(card3, c3_num, c3_txt).move_to(DOWN * 1.5)

        # Beat 3: "Three: you can read a graph's features, which are intercepts, symmetry, turning points and end behaviour, and confirm each one by substitution. Thanks for watching."
        self.play_beat(
            NARR[3],
            FadeIn(c3_group, shift=UP * 0.3),
            run_time=4.0
        )

        # Transition to Credits Card
        self.play(
            FadeOut(title),
            FadeOut(c1_group),
            FadeOut(c2_group),
            FadeOut(c3_group),
            run_time=0.8
        )

        # -------------------------------------------------------------
        # Part 2: Credits & Academic Integrity Slide
        # -------------------------------------------------------------
        credits_title = Text("Course Assessment Credits", font_size=FONT_SIZE_TITLE, color=WHITE, weight=BOLD)
        course_name = Text("Linear Algebra & Calculus (M3)", font_size=FONT_SIZE_SUBTITLE, color=COLOR_CURVE)
        student_info = Text(f"Student: {STUDENT_NAME}  |  ID: {STUDENT_ID}", font_size=FONT_SIZE_LABEL, color=COLOR_INPUT, weight=BOLD)
        
        divider = Line(LEFT * 4.5, RIGHT * 4.5, color=COLOR_AID, stroke_width=1.5)

        cr_ref = Text("References: M3 Course Notes & Manim Community Documentation", font_size=FONT_SIZE_SMALL, color=WHITE)
        cr_tools = Text("Tools: Python 3.11, Manim Community Edition, SymPy, NumPy, FFmpeg", font_size=FONT_SIZE_SMALL, color=COLOR_AID)
        cr_voice = Text("Voiceover: Recorded by Student (Abhinav Singh) / optional gTTS", font_size=FONT_SIZE_SMALL, color=COLOR_AID)
        cr_ai = Text("AI Disclosure: Code scaffolding and script structuring assisted by AI (see docs/AI_DISCLOSURE.md)", font_size=FONT_SIZE_SMALL, color=COLOR_TURNING)

        credits_box = VGroup(
            credits_title,
            course_name,
            student_info,
            divider,
            cr_ref,
            cr_tools,
            cr_voice,
            cr_ai
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)

        self.play(FadeIn(credits_box, shift=UP * 0.4), run_time=1.2)
        self.wait(4.0)
        self.play(FadeOut(credits_box), run_time=0.8)
