# Storyboard: Single-Variable Functions & Graphs

**Course:** Linear Algebra & Calculus (M3)  
**Student:** Abhinav Singh (ID: E25B070774)  
**Target Video Duration:** 5:05 (~305 seconds; hard max 7 minutes / 420 seconds)  
**Format:** 16:9, 1080p (1920×1080), 30 fps  
**Core Example:** $f(x) = x^3 - 3x$  

---

## 1. Learning Objective & Guiding Question

> **Learning Objective:**  
> By the end of this video, the viewer will be able to explain a function as an input-output rule and read the key features of its graph (domain and range, intercepts, symmetry, turning points, end behaviour), checking each one by substitution.

> **Guiding Question:**  
> *Can a single algebraic formula describe an entire roller-coaster ride?*

---

## 2. Hand-Checked Numbers for Viva Defense

All values of $f(x) = x^3 - 3x$ calculated and verified symbolically with SymPy:

| $x$ | $-2$ | $-\sqrt{3} \approx -1.732$ | $-1$ | $0$ | $1$ | $\sqrt{3} \approx 1.732$ | $2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Calculation** | $(-2)^3 - 3(-2) = -8 + 6$ | $(-\sqrt{3})^3 - 3(-\sqrt{3}) = -3\sqrt{3} + 3\sqrt{3}$ | $(-1)^3 - 3(-1) = -1 + 3$ | $0^3 - 3(0) = 0 - 0$ | $1^3 - 3(1) = 1 - 3$ | $(\sqrt{3})^3 - 3(\sqrt{3}) = 3\sqrt{3} - 3\sqrt{3}$ | $2^3 - 3(2) = 8 - 6$ |
| $f(x)$ | **$-2$** | **$0$** | **$2$** | **$0$** | **$-2$** | **$0$** | **$2$** |

### Key Mathematical Features:
1. **Domain:** $\mathbb{R}$ (all real numbers). A polynomial contains no denominators (no division by zero) and no even radicals.
2. **$y$-intercept:** $f(0) = 0^3 - 3(0) = 0 \implies (0, 0)$.
3. **$x$-intercepts (Roots):** $x^3 - 3x = 0 \iff x(x^2 - 3) = 0 \implies x = 0, \pm\sqrt{3} \approx \pm 1.732$.
4. **Symmetry:** $f(-x) = (-x)^3 - 3(-x) = -x^3 + 3x = -(x^3 - 3x) = -f(x)$. Since $f(-x) = -f(x)$, $f$ is an **odd function** with $180^\circ$ rotational symmetry about the origin.
5. **Turning Points:** A local maximum at $(-1, 2)$ and a local minimum at $(1, -2)$. Visible in the table where values peak and trough. *(Viva note: calculus $f'(x) = 3x^2 - 3 = 0$ rigorously proves these occur at $x = \pm 1$).*
6. **End Behaviour:** For large $|x|$, the degree 3 term dominates: $\lim_{x \to +\infty} f(x) = +\infty$, $\lim_{x \to -\infty} f(x) = -\infty$.
7. **Range:** $\mathbb{R}$ (all real numbers). Continuous polynomial traversing from $-\infty$ to $+\infty$.
8. **Horizontal Line Test:** The line $y = 1$ intersects the curve at three distinct real points, proving $f$ is **not one-to-one (not injective)**.

---

## 3. Storyboard (6 Scenes)

| # | Scene | Time | On-Screen Visuals | Mathematical Content |
|---|---|---|---|---|
| **1** | **Hook / Context** | 0:00–0:35 | Title card (4s) showing Name, ID, Course. Fade into coordinate axes where the roller-coaster curve $y = x^3 - 3x$ is drawn in teal. A detailed coaster car travels along the track. | Height at each ground position $x$ is given by $f(x)$. Guiding question: can one formula describe the ride? |
| **2** | **Concept Introduction** | 0:35–1:15 | Formal definition appears line by line. Two set ovals ($X$ and $Y$) with input-to-output mapping arrows. Blue domain highlight, orange range region inside codomain $Y$. | Formal mapping $f: X \to Y$. Uniqueness of output: no $x$ sends two arrows. Domain, codomain, range. |
| **3** | **Visual Intuition** | 1:15–2:30 | (a) Function machine box: input $2$ enters, intermediate arithmetic ($2^3 = 8$, $3 \times 2 = 6$, $8 - 6 = 2$) shown, output $2$ exits. (b) Value table populated row-by-row with points appearing on axes. (c) Dynamic slider dot with dashed vertical line tracing the curve. (d) Vertical line test sweep. | Arithmetic evaluation; graph as set of pairs $(x, f(x))$; continuous tracing; vertical line test confirming function definition. |
| **4** | **Worked Example** | 2:30–4:00 | Two-panel layout (Left: Step-by-step algebra; Right: Graph highlighting features). 5 distinct steps revealed sequentially: Domain, Intercepts, Symmetry, Turning Points, End Behaviour. | Complete algebraic derivation and hand-substitution for each feature. Explicitly noting calculus will later formalize turning points. |
| **5** | **Interpretation** | 4:00–4:40 | Horizontal line $y = c$ sweeping vertically across the range $[-4, 4]$. Line freezes at $y = 1$ revealing 3 intersections. Reconnect to coaster with hill (height 2) and valley (depth -2). | Range is all real numbers; horizontal line test proves function is not one-to-one; physical interpretation of local extrema. |
| **6** | **Summary & Credits** | 4:40–5:10 | Three structured takeaways appear sequentially. Final credits card: references, tools used, AI disclosure, and viva readiness statement. | Comprehensive recap of definitions, graph reading, and analytical verification by substitution. |
