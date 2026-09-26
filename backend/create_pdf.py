from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

# Where the PDF will be created
pdf_path = "../frontend/pdf/trigonometry.pdf"

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=45,
    bottomMargin=45
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Title"],
    fontSize=26,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#243b7a"),
    spaceAfter=12
)

heading_style = ParagraphStyle(
    "HeadingStyle",
    parent=styles["Heading2"],
    fontSize=17,
    textColor=colors.HexColor("#243b7a"),
    spaceBefore=15,
    spaceAfter=8
)

body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontSize=11,
    leading=17,
    spaceAfter=8
)

center_style = ParagraphStyle(
    "CenterStyle",
    parent=body_style,
    alignment=TA_CENTER
)

story = []

# -------------------------
# TITLE
# -------------------------

story.append(Paragraph("LearnIQ", title_style))

story.append(
    Paragraph(
        "TRIGONOMETRY LEARNING GUIDE",
        ParagraphStyle(
            "SubTitle",
            parent=body_style,
            fontSize=15,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#52607a")
        )
    )
)

story.append(Spacer(1, 20))

story.append(
    Paragraph(
        "Learn at your level. Learn your way.",
        center_style
    )
)

# -------------------------
# INTRODUCTION
# -------------------------

story.append(
    Paragraph("1. What is Trigonometry?", heading_style)
)

story.append(
    Paragraph(
        "Trigonometry is the study of the relationship between "
        "the sides and angles of triangles. It is widely used in "
        "engineering, construction, architecture, navigation and science.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Main idea:</b> If we know some sides or angles of a "
        "right triangle, trigonometry can help us find the unknown parts.",
        body_style
    )
)

# -------------------------
# TRIANGLE SIDES
# -------------------------

story.append(
    Paragraph("2. Parts of a Right Triangle", heading_style)
)

triangle_data = [
    ["Side", "Meaning"],
    ["Hypotenuse", "Side opposite the 90° angle"],
    ["Opposite", "Side opposite the angle θ"],
    ["Adjacent", "Side next to θ, excluding the hypotenuse"]
]

triangle_table = Table(
    triangle_data,
    colWidths=[150, 300]
)

triangle_table.setStyle(
    TableStyle([
        (
            "BACKGROUND",
            (0, 0),
            (-1, 0),
            colors.HexColor("#dfe6ff")
        ),
        (
            "FONTNAME",
            (0, 0),
            (-1, 0),
            "Helvetica-Bold"
        ),
        (
            "GRID",
            (0, 0),
            (-1, -1),
            0.6,
            colors.grey
        ),
        (
            "PADDING",
            (0, 0),
            (-1, -1),
            8
        )
    ])
)

story.append(triangle_table)

story.append(Spacer(1, 12))

story.append(
    Paragraph(
        "Tip: First find the angle you are working with. "
        "Then identify the opposite, adjacent and hypotenuse sides.",
        body_style
    )
)

# -------------------------
# TRIG RATIOS
# -------------------------

story.append(
    Paragraph(
        "3. The Three Trigonometric Ratios",
        heading_style
    )
)

ratio_data = [
    ["Ratio", "Formula", "Sides Used"],
    ["sin θ", "Opposite / Hypotenuse", "O and H"],
    ["cos θ", "Adjacent / Hypotenuse", "A and H"],
    ["tan θ", "Opposite / Adjacent", "O and A"]
]

ratio_table = Table(
    ratio_data,
    colWidths=[90, 210, 120]
)

ratio_table.setStyle(
    TableStyle([
        (
            "BACKGROUND",
            (0, 0),
            (-1, 0),
            colors.HexColor("#dfe6ff")
        ),
        (
            "FONTNAME",
            (0, 0),
            (-1, 0),
            "Helvetica-Bold"
        ),
        (
            "GRID",
            (0, 0),
            (-1, -1),
            0.6,
            colors.grey
        ),
        (
            "ALIGN",
            (0, 0),
            (-1, -1),
            "CENTER"
        ),
        (
            "PADDING",
            (0, 0),
            (-1, -1),
            8
        )
    ])
)

story.append(ratio_table)

story.append(Spacer(1, 12))

story.append(
    Paragraph(
        "<b>Easy memory trick:</b> SOH - CAH - TOA",
        ParagraphStyle(
            "Memory",
            parent=body_style,
            fontSize=14,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#243b7a")
        )
    )
)

story.append(
    Paragraph(
        "SOH → Sin = Opposite / Hypotenuse<br/>"
        "CAH → Cos = Adjacent / Hypotenuse<br/>"
        "TOA → Tan = Opposite / Adjacent",
        body_style
    )
)

# -------------------------
# IMPORTANT VALUES
# -------------------------

story.append(
    Paragraph(
        "4. Important Trigonometric Values",
        heading_style
    )
)

values = [
    ["Angle", "sin θ", "cos θ", "tan θ"],
    ["0°", "0", "1", "0"],
    ["30°", "1/2", "√3/2", "1/√3"],
    ["45°", "1/√2", "1/√2", "1"],
    ["60°", "√3/2", "1/2", "√3"],
    ["90°", "1", "0", "Undefined"]
]

value_table = Table(
    values,
    colWidths=[90, 100, 100, 100]
)

value_table.setStyle(
    TableStyle([
        (
            "BACKGROUND",
            (0, 0),
            (-1, 0),
            colors.HexColor("#dfe6ff")
        ),
        (
            "FONTNAME",
            (0, 0),
            (-1, 0),
            "Helvetica-Bold"
        ),
        (
            "GRID",
            (0, 0),
            (-1, -1),
            0.6,
            colors.grey
        ),
        (
            "ALIGN",
            (0, 0),
            (-1, -1),
            "CENTER"
        ),
        (
            "PADDING",
            (0, 0),
            (-1, -1),
            7
        )
    ])
)

story.append(value_table)

# -------------------------
# WORKED EXAMPLE
# -------------------------

story.append(
    Paragraph(
        "5. Worked Example",
        heading_style
    )
)

story.append(
    Paragraph(
        "<b>Question:</b> A right triangle has an angle of 30° "
        "and a hypotenuse of 10 cm. Find the opposite side.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Step 1:</b> We know the opposite side and hypotenuse "
        "are involved, so use sine.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Step 2:</b> sin 30° = Opposite / Hypotenuse",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Step 3:</b> 1/2 = Opposite / 10",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Step 4:</b> Opposite = 5 cm",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Answer: 5 cm</b>",
        ParagraphStyle(
            "Answer",
            parent=body_style,
            fontSize=13,
            textColor=colors.HexColor("#243b7a")
        )
    )
)

# -------------------------
# REAL WORLD
# -------------------------

story.append(
    Paragraph(
        "6. Trigonometry in the Real World",
        heading_style
    )
)

story.append(
    Paragraph(
        "Imagine standing some distance away from a tall building. "
        "You can measure the distance to the building and the angle "
        "from the ground to the top. Trigonometry can then help "
        "estimate the building's height.",
        body_style
    )
)

story.append(
    Paragraph(
        "Trigonometry is used in surveying, construction, robotics, "
        "navigation, engineering and astronomy.",
        body_style
    )
)

# -------------------------
# QUICK PRACTICE
# -------------------------

story.append(
    Paragraph(
        "7. Quick Practice",
        heading_style
    )
)

practice = [
    "1. What is sin 30°?",
    "2. What is cos 60°?",
    "3. What is tan 45°?",
    "4. Which ratio uses opposite and adjacent sides?",
    "5. Which side is opposite the 90° angle?"
]

for question in practice:
    story.append(
        Paragraph(question, body_style)
    )

story.append(Spacer(1, 15))

story.append(
    Paragraph(
        "<b>Answers:</b><br/>"
        "1. 1/2<br/>"
        "2. 1/2<br/>"
        "3. 1<br/>"
        "4. tan θ<br/>"
        "5. Hypotenuse",
        body_style
    )
)

# -------------------------
# FOOTER
# -------------------------

story.append(Spacer(1, 20))

story.append(
    Paragraph(
        "LearnIQ • Personalized learning for every student",
        center_style
    )
)

# CREATE PDF
doc.build(story)

print("===================================")
print("PDF CREATED SUCCESSFULLY!")
print("===================================")
print("File: frontend/pdf/trigonometry.pdf")