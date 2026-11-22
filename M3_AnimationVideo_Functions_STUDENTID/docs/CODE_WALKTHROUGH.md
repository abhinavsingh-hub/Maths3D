# Code Walkthrough & Viva Defense Guide

**Course:** Linear Algebra & Calculus (M3)  
**Assessment:** Animation Video — Single-Variable Functions & Graphs  
**Student:** Abhinav Singh (ID: E25B070774)  

---

## 1. Project Architecture Overview

The repository is modular and structured cleanly so that no complex or opaque abstractions are used:
```
M3_AnimationVideo_Functions_STUDENTID/
  README.md
  M3_Video.mp4                 (final stitched 1080p MP4)
  Storyboard.pdf               (6-scene storyboard table & mathematical specs)
  M3_Code/
    config.py                  (colors, fonts, resolution, voice settings)
    narration.py               (verbatim script split into synchronized beats)
    helpers.py                 (mathematical definitions, standard axes, car, base scene)
    scene1_hook.py             (Hook: title card and roller-coaster ride)
    scene2_concept.py          (Concept: formal mapping, domain, codomain, range)
    scene3_intuition.py        (Intuition: function machine, table, slider, vertical line test)
    scene4_worked_example.py   (Worked Example: 5-step algebraic and graphical breakdown)
    scene5_interpretation.py   (Interpretation: horizontal line test, range, extrema)
    scene6_summary.py          (Summary & Credits: 3 takeaways and complete citations)
    tests/test_math.py         (automated SymPy verification tests)
    build.sh                   (compilation and concatenation script)
  docs/
    storyboard.md              (source storyboard document)
    CODE_WALKTHROUGH.md        (this viva guide)
    AI_DISCLOSURE.md           (academic integrity disclosure)
```

---

## 2. Mathematical Definitions (`helpers.py` & `tests/test_math.py`)

### What does this do?
- Defines the single source of truth for our example function: $f(x) = x^3 - 3x$.
- Both symbolic (`f_sympy = x**3 - 3*x`) and numerical (`def f_func(x): return x**3 - 3.0*x`) versions are provided.
- `TABLE_POINTS` stores the hand-calculated points: $(-2, -2)$, $(-\sqrt{3}, 0)$, $(-1, 2)$, $(0, 0)$, $(1, -2)$, $(\sqrt{3}, 0)$, $(2, 2)$.

### How to explain this in the Viva:
> *"To ensure mathematical consistency across all six scenes, the coordinates and function definition are centralized in `helpers.py`. The scenes import `f_func` and `TABLE_POINTS` rather than hardcoding numbers. Before rendering, `tests/test_math.py` executes SymPy assertions to rigorously verify that the roots, symmetry, limits, and extrema are analytically exact."*

---

## 3. Scene-by-Scene Explanation

### Scene 1: Hook (`scene1_hook.py`)
- **Visuals:** Displays a 4-second title frame with course details, student name, and student ID. Transitions to standard coordinate axes, plots $f(x) = x^3 - 3x$, and animates a roller-coaster car moving along the track using `MoveAlongPath`.
- **Key Code Concept:**
  - `create_title_card()` generates the introductory slate.
  - `get_curve(axes)` constructs the parametric graph of $f(x)$.
  - `MoveAlongPath(car, curve)` smoothly translates and orients the roller coaster car along the trajectory.
- **Viva Explanation:**
  > *"Scene 1 introduces the visual intuition: a roller-coaster profile. At every horizontal coordinate $x$, the track has a unique height $f(x)$. This motivates the fundamental definition of a single-variable function."*

---

### Scene 2: Concept Introduction (`scene2_concept.py`)
- **Visuals:** Shows the formal mathematical definition $f: X \to Y$. Renders two set ovals ($X$ and $Y$) with elements and directed arrows. Illustrates that no input element maps to more than one output. Labels domain (inputs), codomain (target set), and range (actual outputs reached).
- **Key Code Concept:**
  - `Ellipse()` and `Dot()` represent elements in sets $X$ and $Y$.
  - `Arrow()` visually demonstrates mapping rules.
  - Highlighting emphasizes that an input cannot branch into multiple outputs.
- **Viva Explanation:**
  > *"Scene 2 establishes mathematical rigor. A function is a rule assigning to each input $x \in X$ exactly one output $f(x) \in Y$. We distinguish between the codomain (the target set $\mathbb{R}$) and the range (the actual values achieved)."*

---

### Scene 3: Visual Intuition (`scene3_intuition.py`)
- **Visuals:**
  1. **Function Machine:** A rounded box labelled $f$. The input $2$ enters from the left, intermediate operations ($2^3 = 8$, $3 \times 2 = 6$, $8 - 6 = 2$) are computed, and output $2$ emerges.
  2. **Table of Values:** Fills row-by-row for $x \in \{-2, -1, 0, 1, 2\}$; corresponding dots appear on the coordinate axes.
  3. **Continuous Slider:** A `ValueTracker` updates an input dot on the $x$-axis, a vertical dashed line, and a live readout $(x, f(x))$, tracing out the continuous curve.
  4. **Vertical Line Test:** A vertical line sweeps from left to right across the domain, highlighting that it never intersects the curve at more than one point.
- **Key Code Concept:**
  - `ValueTracker` with `always_redraw()` dynamically computes $(x, f(x))$ in real-time.
  - `VGroup` constructs the table and function machine.
- **Viva Explanation:**
  > *"Scene 3 bridges discrete arithmetic and continuous geometry. The function machine illustrates substitution. The table shows discrete points, which interpolate into a continuous curve as $x$ varies. The vertical line test geometrically reinforces the single-output rule."*

---

### Scene 4: Worked Example (`scene4_worked_example.py`)
- **Visuals:** A two-panel layout: Left panel shows algebraic derivations; right panel shows the coordinate axes highlighting the corresponding geometric feature.
  1. **Step 1 (Domain):** Explains that polynomials have no division by zero or even roots $\implies \text{Domain} = \mathbb{R}$. Shading highlights the entire $x$-axis.
  2. **Step 2 (Intercepts):** Computes $y$-intercept $f(0) = 0$. Solves $x(x^2 - 3) = 0 \implies x = 0, \pm\sqrt{3}$. Verifies $f(\sqrt{3}) = 3\sqrt{3} - 3\sqrt{3} = 0$. Plots green intercept dots.
  3. **Step 3 (Symmetry):** Proves $f(-x) = -f(x)$. Rotates the curve by $180^\circ$ about the origin to demonstrate point symmetry.
  4. **Step 4 (Turning Points):** Uses table values to identify local max at $(-1, 2)$ and local min at $(1, -2)$. Clearly notes: *"Calculus (derivatives) will tell us why these occur at $x = \pm 1$."*
  5. **Step 5 (End Behaviour):** Evaluates $f(10) = 970$ and $f(-10) = -970$. Shows that as $x \to \pm\infty$, the cubic term $x^3$ dominates.
- **Viva Explanation:**
  > *"Scene 4 demonstrates how to analytically read and verify all key graph features step by step. We show every line of algebraic substitution before marking the feature on the graph."*

---

### Scene 5: Interpretation (`scene5_interpretation.py`)
- **Visuals:** Sweeps a horizontal line $y = c$ upward across the graph. At $y = 1$, three distinct intersection points appear. Connects back to the roller coaster, labelling the hill at height $2$ and the valley at depth $-2$.
- **Key Code Concept:**
  - `Intersection` dots computed via roots of $x^3 - 3x - 1 = 0$.
  - Horizontal line test proves that the function is **not injective (not one-to-one)** because multiple distinct inputs yield the same output.
  - Demonstrates that the **range is all real numbers** ($\mathbb{R}$) since every horizontal line $y = c$ intersects the curve at least once.
- **Viva Explanation:**
  > *"Scene 5 explores range and injectivity. Because every horizontal line intersects the curve, the range is all reals. Because some horizontal lines intersect the curve more than once (e.g. $y = 1$), the function is not one-to-one."*

---

### Scene 6: Summary & Credits (`scene6_summary.py`)
- **Visuals:** Presents the three core takeaways in clear cards, followed by full academic citations, software acknowledgements, and AI disclosure.
- **Viva Explanation:**
  > *"Scene 6 synthesizes the pedagogical takeaways: the input-output rule, the graphical interpretation, and analytical verification by substitution."*

---

## 4. Common Viva Questions & Model Answers

**Q1: Why did you choose $f(x) = x^3 - 3x$ instead of a simpler quadratic or linear function?**  
*Answer:* A linear function doesn't have turning points, and a quadratic only has one extremum and is symmetric across a vertical line. A cubic function exhibits rich features: three real roots, odd origin symmetry, both a local maximum and a local minimum, and opposite end behaviour, while keeping integer values at $x = -2, -1, 0, 1, 2$ for clean on-screen arithmetic.

**Q2: How do you know the turning points are exactly at $x = -1$ and $x = 1$?**  
*Answer:* In pre-calculus, the table of integer values reveals that the function climbs up to $2$ at $x = -1$ and falls to $-2$ at $x = 1$. In calculus, we set the derivative $f'(x) = 3x^2 - 3 = 0 \implies x^2 = 1 \implies x = \pm 1$. The second derivative $f''(x) = 6x$ confirms $f''(-1) = -6 < 0$ (local maximum) and $f''(1) = 6 > 0$ (local minimum).

**Q3: How does the code synchronize animations with speech?**  
*Answer:* In `helpers.py`, `BaseM3Scene` provides `play_beat(beat_text, *animations)`. It measures the word count of each beat in `narration.py` and scales the run time and wait time based on a natural speaking pace of 140 words per minute (~2.3 words/sec). When voiceover mode is activated, it syncs directly to the audio tracker.
