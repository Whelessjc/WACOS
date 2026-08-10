from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import BaseDocTemplate, Frame, HRFlowable, PageBreak, PageTemplate, Paragraph, Spacer

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "01_Curriculum" / "Culinary_1" / "Week_01_2026"
OUT = ROOT / "output" / "pdf" / "Culinary_1_Week_1_Print_Packet.pdf"
NAVY, BLUE, GRAY = colors.HexColor("#17365D"), colors.HexColor("#2F75B5"), colors.HexColor("#666666")

ss = getSampleStyleSheet()
S = {
    "title": ParagraphStyle("title", parent=ss["Title"], fontName="Helvetica-Bold", fontSize=24, leading=28, textColor=NAVY, alignment=1, spaceAfter=12),
    "sub": ParagraphStyle("sub", parent=ss["Normal"], fontName="Helvetica", fontSize=12, leading=16, textColor=GRAY, alignment=1, spaceAfter=8),
    "h1": ParagraphStyle("h1", parent=ss["Heading1"], fontName="Helvetica-Bold", fontSize=17, leading=20, textColor=NAVY, spaceAfter=8, keepWithNext=True),
    "h2": ParagraphStyle("h2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=12, leading=14, textColor=BLUE, spaceBefore=8, spaceAfter=3, keepWithNext=True),
    "h3": ParagraphStyle("h3", parent=ss["Heading3"], fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=NAVY, spaceBefore=6, spaceAfter=2, keepWithNext=True),
    "body": ParagraphStyle("body", parent=ss["BodyText"], fontName="Helvetica", fontSize=9.1, leading=11.5, spaceAfter=3),
    "bullet": ParagraphStyle("bullet", parent=ss["BodyText"], fontName="Helvetica", fontSize=9, leading=11.3, leftIndent=15, firstLineIndent=-8, bulletIndent=3, spaceAfter=2),
    "number": ParagraphStyle("number", parent=ss["BodyText"], fontName="Helvetica", fontSize=9, leading=11.3, leftIndent=18, firstLineIndent=-12, spaceAfter=2),
    "callout": ParagraphStyle("callout", parent=ss["BodyText"], fontName="Helvetica-Bold", fontSize=9.5, leading=12, borderColor=colors.HexColor("#E6B800"), borderWidth=.8, borderPadding=7, backColor=colors.HexColor("#FFF2CC"), spaceBefore=7, spaceAfter=8),
}

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline(s):
    s = (s.replace("â€œ", '"').replace("â€", '"')
           .replace("â€™", "'").replace("â€“", "-").replace("â€”", "-"))
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", s)

def markdown(path, inject_recipe=False):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    out = []
    recipe_inserted = False
    for raw in lines:
        line = raw.strip()
        if not line:
            out.append(Spacer(1, 2)); continue
        if inject_recipe and not recipe_inserted and set(line) == {"_"} and len(line) > 20:
            out += recipe_block(); recipe_inserted = True
            continue
        if inject_recipe and recipe_inserted and set(line) == {"_"} and len(line) > 20:
            continue
        if line.startswith("# "): out.append(Paragraph(inline(line[2:]), S["h1"]))
        elif line.startswith("## "): out.append(Paragraph(inline(line[3:]), S["h2"]))
        elif line.startswith("### "): out.append(Paragraph(inline(line[4:]), S["h3"]))
        elif line.startswith("> "):
            if "Drafted for instructor review" not in line: out.append(Paragraph(inline(line[2:]), S["callout"]))
        elif re.match(r"^\d+\.\s", line):
            n, t = line.split(".", 1); out.append(Paragraph(inline(t.strip()), S["number"], bulletText=n + "."))
        elif line.startswith("- [ ] "): out.append(Paragraph("____  " + inline(line[6:]), S["bullet"]))
        elif line.startswith("- "): out.append(Paragraph(inline(line[2:]), S["bullet"], bulletText="-"))
        elif set(line) == {"_"} and len(line) > 20:
            out += [Spacer(1, 7), HRFlowable(width="100%", thickness=.5, color=GRAY), Spacer(1, 5)]
        else: out.append(Paragraph(inline(line), S["body"]))
    return out

def recipe_block():
    ingredients = ["5 cups self-rising flour", "1/2 cup sugar", "2 cups milk", "2 cups buttermilk", "4 eggs", "4 Tbsp vegetable oil"]
    method = ["Preheat the griddle to medium.", "Whisk together the flour and sugar.", "In a separate bowl, whisk the milk, buttermilk, eggs, and oil.", "Add the wet ingredients to the dry and whisk for 10 seconds, or until the batter barely comes together. The batter will be lumpy.", "Use a #12 scoop (green) to portion batter onto the griddle.", "Cook until craters form.", "Do not add toppings for this Week 1 lab.", "When ready, flip the pancakes and cook until done."]
    out = [Paragraph("Instructor-Approved Pancake Recipe", S["h2"]), Paragraph("Ingredients", S["h3"])]
    out += [Paragraph(x, S["bullet"], bulletText="-") for x in ingredients]
    out.append(Paragraph("Method", S["h3"]))
    out += [Paragraph(x, S["number"], bulletText=str(i) + ".") for i, x in enumerate(method, 1)]
    return out

def header_footer(c, d):
    c.saveState()
    if d.page > 1:
        c.setFont("Helvetica", 8); c.setFillColor(GRAY)
        c.drawString(.65*inch, 10.64*inch, "Culinary 1 | Week 1 | August 11-14, 2026")
        c.drawRightString(7.85*inch, .35*inch, f"Page {d.page}")
    c.restoreState()

def divider(title, subtitle):
    return [Spacer(1, 2.2*inch), Paragraph(title, S["title"]), Paragraph(subtitle, S["sub"]), HRFlowable(width="60%", thickness=2, color=BLUE), PageBreak()]

def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(str(OUT), pagesize=letter, leftMargin=.68*inch, rightMargin=.68*inch, topMargin=.62*inch, bottomMargin=.58*inch, title="Culinary 1 Week 1 Print Packet", author="WACOS")
    doc.addPageTemplates([PageTemplate(id="main", frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")], onPage=header_footer)])
    story = [Spacer(1,.7*inch), Paragraph("CULINARY 1", S["sub"]), Paragraph("Week 1 Print Packet", S["title"]), Paragraph("August 11-14, 2026 | Four instructional days", S["sub"]), Spacer(1,.2*inch), HRFlowable(width="72%", thickness=2, color=BLUE), Spacer(1,.2*inch), Paragraph("Contents", S["h2"]), Paragraph("Four Daily Teaching Guides; four student masters; Week 1 projection reference.", S["body"]), Paragraph("RECIPE CONFIRMED: The supplied Pancakes recipe has been inserted into the Day 3 student preparation sheet. For this Week 1 lab, the curriculum direction of no added toppings is retained.", S["callout"]), Paragraph("Suggested printing", S["h2"]), Paragraph("Print one full packet for the instructor. Print each student-master section separately at the quantity needed for each class. The projection reference does not need student copies.", S["body"]), PageBreak()]
    for f in ["Day_01_Welcome_and_Kitchen_Orientation_DTG.md", "Day_02_Kitchen_Mode_and_Basic_Routines_DTG.md", "Day_03_Read_Before_You_Cook_DTG.md", "Day_04_First_Lab_Pancakes_DTG.md"]:
        story += markdown(SRC/f) + [PageBreak()]
    story += divider("Student Masters", "Print the needed quantity for each class")
    students = ["Day_01_Kitchen_Orientation_Challenge.md", "Day_02_Kitchen_Mode_Quick_Practice.md", "Day_03_Pancake_Recipe_Reading_and_Preparation.md", "Day_04_Pancake_Lab_and_Reflection.md"]
    for f in students:
        story += markdown(SRC/"Student_Materials"/f, inject_recipe=("Day_03" in f)) + [PageBreak()]
    story += divider("Projection Reference", "Week 1 classroom slide source")
    story += markdown(SRC/"Slides"/"Culinary_1_Week_01_Slide_Source.md")
    doc.build(story)
    print(OUT)

if __name__ == "__main__": build()
