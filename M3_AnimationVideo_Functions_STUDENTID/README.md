# M3 Animation Video: Single-Variable Functions & Graphs
**University Internal Assessment — Linear Algebra & Calculus (M3)**  
**Student Name:** Abhinav Singh  
**Student ID:** E25B070774  
**Example Function:** $f(x) = x^3 - 3x$  
**Target Duration:** ~5:10 (Hard max 7:00 / 420 seconds)  
**Render Quality:** 1080p (1920×1080), 30 fps, 16:9 MP4  

> **PUBLIC REPOSITORY REMINDER:**  
> This repository must remain **PUBLIC** for submission and grading verification.

---

## 1. Project Overview & Pedagogical Goals

This project is a complete, runnable mathematical animation video developed with **Manim Community Edition** (Python). It explores the fundamentals of single-variable functions through the cubic polynomial:
$$f(x) = x^3 - 3x$$

### Key Learning Objective:
By the end of this video, the viewer will be able to explain a function as an input-output rule and read the key features of its graph:
1. **Domain & Range:** Allowed inputs ($\mathbb{R}$) and achieved outputs ($\mathbb{R}$).
2. **Intercepts:** $y$-intercept $(0, 0)$ and $x$-intercepts $(0, 0)$, $(\sqrt{3}, 0)$, $(-\sqrt{3}, 0)$.
3. **Symmetry:** Analytical proof that $f(-x) = -f(x)$ (odd function with $180^\circ$ rotational symmetry about origin).
4. **Turning Points:** Local maximum at $(-1, 2)$ and local minimum at $(1, -2)$.
5. **End Behaviour:** Cubic dominance for large $|x|$: $f(x) \to \pm\infty$ as $x \to \pm\infty$.
6. **Horizontal Line Test:** $y = 1$ intersects 3 times, demonstrating $f$ is **not one-to-one (not injective)**.

---

## 2. Repository Layout

```
M3_AnimationVideo_Functions_STUDENTID/
├── README.md                  # Complete documentation and viva guide
├── M3_Video.mp4               # Final stitched 1080p video output
├── Storyboard.pdf             # 6-scene storyboard table & specification (ReportLab)
├── M3_Code/
│   ├── requirements.txt       # Python dependencies (manim, sympy, pytest, numpy, reportlab)
│   ├── config.py              # Central config (colors, resolution, voice settings)
│   ├── narration.py           # Exact verbatim script split into beats
│   ├── helpers.py             # Math definitions, standard axes, coaster car, BaseM3Scene
│   ├── scene1_hook.py         # Scene 1: Title card & roller-coaster hook
│   ├── scene2_concept.py      # Scene 2: Formal mapping, domain, codomain, range
│   ├── scene3_intuition.py    # Scene 3: Function machine, table, slider, vertical line test
│   ├── scene4_worked_example.py # Scene 4: 5-step algebra and feature reading
│   ├── scene5_interpretation.py # Scene 5: Horizontal line test, range, coaster extrema
│   ├── scene6_summary.py      # Scene 6: Three takeaways and complete credits
│   ├── generate_storyboard_pdf.py # Generates Storyboard.pdf from docs
│   ├── build.sh               # Automated build & render script (macOS/Linux)
│   ├── build.ps1              # Automated build & render script (Windows)
│   ├── tests/
│   │   └── test_math.py       # SymPy unit tests for all mathematical claims
│   └── audio/                 # Optional: student voiceover WAV files
└── docs/
    ├── storyboard.md          # 6-scene storyboard source markdown
    ├── CODE_WALKTHROUGH.md    # Plain-English viva defense guide
    └── AI_DISCLOSURE.md       # Academic integrity statement
```

---

## 3. Quick Start & Build Instructions

### Prerequisites
1. **Python 3.10+** (Python 3.11 recommended)
2. **FFmpeg, Pango, Cairo:**
   - **macOS:** `brew install ffmpeg pango cairo`
   - **Ubuntu/Debian:** `sudo apt update && sudo apt install -y ffmpeg libpango1.0-dev libcairo2-dev`
   - **Windows:** `choco install ffmpeg`

### Automated Build Commands
Navigate to `M3_Code/`:
```bash
cd M3_Code
chmod +x build.sh
```

- **Fast Preview (854×480, 15 fps — recommended during editing):**
  ```bash
  ./build.sh preview
  ```

- **Full Production Render (1920×1080, 30 fps — university submission):**
  ```bash
  ./build.sh
  ```

The script automatically:
1. Executes `pytest tests/test_math.py` (halts build if any assertion fails).
2. Renders all 6 scenes sequentially.
3. Compiles `Storyboard.pdf`.
4. Concatenates scenes with FFmpeg into `../M3_Video.mp4`.
5. Verifies and displays the total runtime.

---

## 4. Voiceover & Audio Options

The project is designed with modular audio in `config.py`:
- `VOICE_MODE = "silent"` *(Default)*: Visual animations are paced naturally to a ~140 wpm spoken cadence (~5:05 total). Perfect for student live presentation or external microphone recording.
- `VOICE_MODE = "recorded"`: Syncs with `audio/scene1.wav` ... `audio/scene6.wav`.
- `VOICE_MODE = "gtts"`: Uses Google Text-to-Speech via `manim-voiceover`.

Optional background music placed in `M3_Code/music/bg.mp3` will automatically be mixed at -25 dB under narration by `build.sh`.

---

## 5. Mathematical Summary Table (Viva Reference)

| $x$ | Hand Substitution: $f(x) = x^3 - 3x$ | $f(x)$ | Geometric Feature |
| :---: | :--- | :---: | :--- |
| **$-2$** | $(-2)^3 - 3(-2) = -8 + 6$ | **$-2$** | Boundary point |
| **$-\sqrt{3}$** | $(-\sqrt{3})^3 - 3(-\sqrt{3}) = -3\sqrt{3} + 3\sqrt{3}$ | **$0$** | Negative $x$-intercept ($\approx -1.732$) |
| **$-1$** | $(-1)^3 - 3(-1) = -1 + 3$ | **$2$** | **Local Maximum** (Peak height $= 2$) |
| **$0$** | $0^3 - 3(0) = 0$ | **$0$** | **Origin Intercept** $(0, 0)$ |
| **$1$** | $1^3 - 3(1) = 1 - 3$ | **$-2$** | **Local Minimum** (Valley depth $= -2$) |
| **$\sqrt{3}$** | $(\sqrt{3})^3 - 3(\sqrt{3}) = 3\sqrt{3} - 3\sqrt{3}$ | **$0$** | Positive $x$-intercept ($\approx 1.732$) |
| **$2$** | $2^3 - 3(2) = 8 - 6$ | **$2$** | Boundary point |

---

## 6. Academic Integrity
Refer to [docs/AI_DISCLOSURE.md](docs/AI_DISCLOSURE.md) for the complete disclosure regarding the use of AI tools for scaffolding and script review.
