"""
Generate Storyboard.pdf from docs/storyboard.md using ReportLab.
Produces a professional university assessment PDF document.
"""

import sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_storyboard_pdf(output_pdf_path):
    doc = SimpleDocTemplate(
        str(output_pdf_path),
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#475569'),
        spaceAfter=14
    )
    h2_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=12,
        spaceAfter=6
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1E293B')
    )
    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#0F172A'),
        backColor=colors.HexColor('#F1F5F9'),
        borderColor=colors.HexColor('#3B82F6'),
        borderWidth=1,
        borderPadding=8,
        spaceAfter=10
    )
    table_text = ParagraphStyle(
        'TableText',
        parent=styles['Normal'],
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1E293B')
    )
    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontSize=8.5,
        leading=11,
        fontName='Helvetica-Bold',
        textColor=colors.white
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("M3 Animation Video: Storyboard & Specification", title_style))
    story.append(Paragraph("<b>Course:</b> Linear Algebra & Calculus (M3) &nbsp;|&nbsp; <b>Student:</b> Abhinav Singh (ID: E25B070774) &nbsp;|&nbsp; <b>Example:</b> f(x) = x³ - 3x", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#3B82F6'), spaceAfter=12))

    # Learning Objective Box
    story.append(Paragraph("<b>Learning Objective:</b> By the end of this video, the viewer will be able to explain a function as an input-output rule and read the key features of its graph (domain and range, intercepts, symmetry, turning points, end behaviour), checking each one by substitution.<br/><br/><b>Guiding Question:</b> <i>Can a single algebraic formula describe an entire roller-coaster ride?</i>", callout_style))

    # Hand-checked Values Table
    story.append(Paragraph("1. Hand-Checked Values for Viva Defense (All analytically verified)", h2_style))
    
    math_table_data = [
        [
            Paragraph("x", table_header),
            Paragraph("-2", table_header),
            Paragraph("-√3 ≈ -1.73", table_header),
            Paragraph("-1", table_header),
            Paragraph("0", table_header),
            Paragraph("1", table_header),
            Paragraph("√3 ≈ 1.73", table_header),
            Paragraph("2", table_header),
        ],
        [
            Paragraph("<b>f(x) = x³ - 3x</b>", table_text),
            Paragraph("<b>-2</b>", table_text),
            Paragraph("<b>0</b>", table_text),
            Paragraph("<b>2</b>", table_text),
            Paragraph("<b>0</b>", table_text),
            Paragraph("<b>-2</b>", table_text),
            Paragraph("<b>0</b>", table_text),
            Paragraph("<b>2</b>", table_text),
        ],
        [
            Paragraph("Feature Note", table_text),
            Paragraph("Left bound", table_text),
            Paragraph("x-intercept", table_text),
            Paragraph("Local Max", table_text),
            Paragraph("Origin (0,0)", table_text),
            Paragraph("Local Min", table_text),
            Paragraph("x-intercept", table_text),
            Paragraph("Right bound", table_text),
        ]
    ]

    t_math = Table(math_table_data, colWidths=[100, 60, 75, 60, 60, 60, 75, 60])
    t_math.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E293B')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#F8FAFC'), colors.HexColor('#EDF2F7')]),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_math)
    story.append(Spacer(1, 14))

    # 6 Scenes Storyboard Table
    story.append(Paragraph("2. Detailed 6-Scene Storyboard", h2_style))

    scene_data = [
        [
            Paragraph("#", table_header),
            Paragraph("Scene", table_header),
            Paragraph("Time", table_header),
            Paragraph("On-Screen Visuals", table_header),
            Paragraph("Mathematical Content", table_header),
        ],
        [
            Paragraph("1", table_text),
            Paragraph("<b>Hook / Context</b>", table_text),
            Paragraph("0:00–0:35", table_text),
            Paragraph("Title card (4s: Course, Name, ID). Axes appear. Teal curve y = x³ - 3x drawn. Styled coaster car travels along curve.", table_text),
            Paragraph("Height at ground position x is f(x). Guiding question: Can one formula describe the whole ride?", table_text),
        ],
        [
            Paragraph("2", table_text),
            Paragraph("<b>Concept Intro</b>", table_text),
            Paragraph("0:35–1:15", table_text),
            Paragraph("Formal mapping f: X → Y. Two set ovals (X inputs, Y outputs) with arrows. Blue domain, orange range, uniqueness of arrows.", table_text),
            Paragraph("f: ℝ → ℝ. Uniqueness of output (no branching). Allowed inputs = domain; produced outputs = range.", table_text),
        ],
        [
            Paragraph("3", table_text),
            Paragraph("<b>Visual Intuition</b>", table_text),
            Paragraph("1:15–2:30", table_text),
            Paragraph("Function machine f: input 2 enters, arithmetic shown (8-6=2), 2 exits. Value table filled row-by-row with dots plotted on axes. Continuous slider dot traces curve. Vertical line sweeps across.", table_text),
            Paragraph("Graph as coordinate pairs (x, f(x)). Interpolation into continuous curve. Vertical line test proves function definition.", table_text),
        ],
        [
            Paragraph("4", table_text),
            Paragraph("<b>Worked Example</b>", table_text),
            Paragraph("2:30–4:00", table_text),
            Paragraph("Two-panel layout: Algebra on left, graph on right. 5 sequential steps: (1) Domain shaded on x-axis; (2) Intercepts at 0, ±√3; (3) 180° origin rotation (odd function); (4) Local max (-1,2) and min (1,-2); (5) Dominant term x³ for large |x|.", table_text),
            Paragraph("Every substitution shown line by line. Formal algebra: factoring x(x²-3)=0, odd proof f(-x)=-f(x), end limits ±∞.", table_text),
        ],
        [
            Paragraph("5", table_text),
            Paragraph("<b>Interpretation</b>", table_text),
            Paragraph("4:00–4:40", table_text),
            Paragraph("Horizontal line sweeps [-4, 4]. Freezes at y = 1 showing 3 intersections. Coaster hill and valley labelled with heights.", table_text),
            Paragraph("Range = ℝ (every height reached). Line y=1 cuts 3 times → NOT one-to-one. Physical local extrema.", table_text),
        ],
        [
            Paragraph("6", table_text),
            Paragraph("<b>Summary & Credits</b>", table_text),
            Paragraph("4:40–5:10", table_text),
            Paragraph("Three animated takeaway cards appear sequentially. Final credits card: Course, student info, tools, references, and AI disclosure.", table_text),
            Paragraph("Recap of input-output rule, graphical reading, and analytical verification by substitution.", table_text),
        ],
    ]

    t_scenes = Table(scene_data, colWidths=[20, 75, 55, 200, 180])
    t_scenes.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0F172A')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_scenes)

    doc.build(story)
    print(f"Successfully generated {output_pdf_path}")

if __name__ == '__main__':
    base_dir = Path(__file__).resolve().parent.parent
    pdf_path = base_dir / "Storyboard.pdf"
    generate_storyboard_pdf(pdf_path)
