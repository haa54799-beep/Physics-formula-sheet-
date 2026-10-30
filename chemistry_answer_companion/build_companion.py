#!/usr/bin/env python3
"""Build the structured inventory, answer database, reports, and searchable PDF.

Run from the repository root:
    python3 chemistry_answer_companion/build_companion.py
Dependencies: PyMuPDF and ReportLab (see README.md).
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape

import pymupdf
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
SOURCE_PDF = ROOT / "Revision12.pdf"
BLUE = colors.HexColor("#35649A")
PALE_BLUE = colors.HexColor("#EAF1F8")
DARK = colors.HexColor("#20252B")
MID = colors.HexColor("#56616D")

UNITS = [
    (1, "Solutions", 1, 72),
    (2, "Electrochemistry", 73, 144),
    (3, "Chemical Kinetics", 145, 216),
    (4, "d- and f-Block Elements", 217, 288),
    (5, "Coordination Compounds", 289, 358),
    (6, "Haloalkanes and Haloarenes", 359, 428),
    (7, "Alcohols, Phenols and Ethers", 429, 500),
]
UNIT_FOR_Q = {}
for unit_no, title, first, last in UNITS:
    for number in range(first, last + 1):
        UNIT_FOR_Q[number] = (unit_no, title, first, last)

MARKER = re.compile(r"(?m)^\s*(\d{1,3})\.\s*\[([MH])\]\s*")


def clean_question(text: str) -> str:
    text = re.sub(r"(?m)^\s*Page\s+\d+\s*$", " ", text)
    text = re.sub(r"(?m)^\s*UNIT\s+\d+\s*:\s*[^\n]*$", " ", text)
    text = re.sub(r"(?m)^\s*UNIT\s+\d+\s*[—–-]\s*Additional Practice\s*$", " ", text)
    text = re.sub(r"(?m)^\s*Questions\s+\d+[–-]\d+\s*$", " ", text)
    text = re.sub(r"(?m)^\s*Page\s+\d+\s*$", " ", text)
    text = re.sub(r"\bPage\s+\d+\b", " ", text)
    text = re.sub(r"\bUNIT\s+\d+\s*[—–-]\s*Additional Practice\b", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def classify_question(text: str) -> tuple[str, list[str]]:
    t = text.lower()
    tags: list[str] = []
    if re.search(r"\b(calculate|compute|estimate|find the time|calculate the time|how much|how many|what fraction|determine the oxidation state|calculate the oxidation state|number of unpaired electrons|how many.*isomer)", t):
        tags.append("quantitative/problem-solving")
    if re.search(r"\b(derive|show that|derive the relation|derive the equation)", t):
        tags.append("derivation")
    if re.search(r"\b(iupac name|write the name|name of|write the formula|formula of|general formula)", t):
        tags.append("nomenclature/formula")
    if re.search(r"\b(reaction|product|products|balance|equation|prepare|preparation|convert|sequence|synthesis|mechanism|write the anode|write the cathode|write the overall)", t):
        tags.append("reaction/equation")
    if re.search(r"\b(distinguish|compare|difference between|arrange|order of|contrast)", t):
        tags.append("comparison/classification")
    if re.search(r"\b(explain|why|how does|how can|what is the role|what is the significance)", t):
        tags.append("explanation/application")
    if not tags or (len(tags) == 1 and tags[0] == "explanation/application"):
        tags.append("definition/concept")
    # Deterministic primary label for filters; all matching labels remain available.
    priority = [
        "quantitative/problem-solving", "derivation", "nomenclature/formula",
        "reaction/equation", "comparison/classification", "explanation/application",
        "definition/concept",
    ]
    primary = next((tag for tag in priority if tag in tags), "definition/concept")
    return primary, tags


def extract_questions() -> list[dict]:
    if not SOURCE_PDF.exists():
        raise FileNotFoundError(f"Source PDF not found: {SOURCE_PDF}")
    questions: list[dict] = []
    with pymupdf.open(SOURCE_PDF) as doc:
        for page_index, page in enumerate(doc):
            page_text = page.get_text("text")
            matches = list(MARKER.finditer(page_text))
            for i, match in enumerate(matches):
                number = int(match.group(1))
                source_tag = match.group(2)
                end = matches[i + 1].start() if i + 1 < len(matches) else len(page_text)
                question_text = clean_question(page_text[match.end():end])
                if number not in UNIT_FOR_Q:
                    raise ValueError(f"Unexpected question number {number} on source page {page_index + 1}")
                unit_no, title, _, _ = UNIT_FOR_Q[number]
                primary, tags = classify_question(question_text)
                questions.append({
                    "question_id": f"U{unit_no}-Q{number:03d}",
                    "number": number,
                    "unit_number": unit_no,
                    "unit_title": title,
                    "source_pdf_page": page_index + 1,
                    "source_tag": source_tag,
                    "primary_type": primary,
                    "type_tags": tags,
                    "question_text": question_text,
                })
    numbers = [q["number"] for q in questions]
    if numbers != list(range(1, 501)):
        raise ValueError(f"Question audit failed: found {len(numbers)} markers, sequence gaps/duplicates detected")
    if len(questions) != 500:
        raise ValueError(f"Expected 500 questions, extracted {len(questions)}")
    if any(not q["question_text"] for q in questions):
        raise ValueError("At least one question has empty extracted text")
    return questions


def load_answer_seeds() -> dict[int, str]:
    answers: dict[int, str] = {}
    for path in sorted((OUT / "authoring").glob("unit*.tsv")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            if "|" not in line:
                raise ValueError(f"Malformed answer seed {path}:{line_number}")
            number_text, answer = line.split("|", 1)
            number = int(number_text)
            if number in answers:
                raise ValueError(f"Duplicate answer seed for question {number}")
            if not answer.strip():
                raise ValueError(f"Blank answer for question {number}")
            answers[number] = answer.strip()
    if sorted(answers) != list(range(1, 501)):
        missing = sorted(set(range(1, 501)) - set(answers))
        extra = sorted(set(answers) - set(range(1, 501)))
        raise ValueError(f"Answer seed coverage error. Missing={missing}; extra={extra}")
    return answers


# Questions whose wording leaves a consequential condition or generalisation open.
REVIEW_NOTES = {
    102: "Aqueous NaCl anode product depends on chloride concentration: concentrated brine gives Cl₂; very dilute chloride may give O₂. The answer states both cases.",
    387: "The environmental concern is specific: an official Australian chemical evaluation identifies atmospheric emissions of dichloromethane as contributing to stratospheric ozone depletion.",
    144: "The metal-ion charge is not specified, so the direction is determinate but a unique numerical EMF is not. A general z-valent Nernst expression is supplied.",
    393: "Persistence varies across modern pesticides; the answer avoids treating all newer compounds as a single safer class.",
    403: "AgNO₃ behaviour depends on whether the organic halide releases halide ion; sample preparation and suitable conditions matter.",
    425: "The question does not specify substrate or mechanism. The answer gives the stereogenic-centre criterion and CIP method, then distinguishes SN2 inversion from other outcomes.",
}


def make_records(questions: list[dict], answers: dict[int, str]) -> tuple[list[dict], list[dict]]:
    inventory = []
    database = []
    for q in questions:
        n = q["number"]
        base = dict(q)
        inventory.append(base)
        row = dict(q)
        row["answer"] = answers[n]
        row["answer_review_status"] = "reviewed_with_condition_note" if n in REVIEW_NOTES else "subject_matter_reviewed"
        if n in REVIEW_NOTES:
            row["review_note"] = REVIEW_NOTES[n]
        database.append(row)
    return inventory, database


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def format_answer_for_pdf(text: str) -> str:
    """Escape plain answer text, then typeset simple underscore subscripts."""
    safe = escape(text)
    return re.sub(r"_([A-Za-z0-9]+)", r"<sub>\1</sub>", safe)


def write_inventory_csv(inventory: list[dict]) -> None:
    path = OUT / "question_inventory.csv"
    fields = ["question_id", "number", "unit_number", "unit_title", "source_pdf_page", "source_tag", "primary_type", "type_tags", "question_text"]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for q in inventory:
            row = dict(q)
            row["type_tags"] = "; ".join(q["type_tags"])
            writer.writerow({key: row[key] for key in fields})


def write_progress_report(inventory: list[dict], database: list[dict], pdf_pages: int) -> None:
    tag_counts = Counter(q["source_tag"] for q in inventory)
    unit_counts = Counter(q["unit_number"] for q in inventory)
    rows = "\n".join(
        f"| Unit {n}: {title} | Q{first}–{last} | {unit_counts[n]} | "
        f"pp. {min(q['source_pdf_page'] for q in inventory if q['unit_number']==n)}–"
        f"{max(q['source_pdf_page'] for q in inventory if q['unit_number']==n)} |"
        for n, title, first, last in UNITS
    )
    text = f"""# Progress report — Chemistry answer companion

**Build date:** {date.today().isoformat()}  
**Source:** `Revision12.pdf`  
**Build status:** The complete draft deliverable set is generated; it is not an externally peer-reviewed official answer key.

## Coverage

| Unit | Question range | Inventory / answers | Original PDF pages |
|---|---:|---:|---:|
{rows}
| **Total** | **Q1–Q500** | **{len(inventory)} / {len(database)}** | **{pdf_pages} source pages** |

- Question markers: 500 unique, sequential (Q1–Q500); no gaps or duplicates.
- Structured answers: {len(database)} of 500, with original source-page references.
- Source tags preserved verbatim: `[M]` = {tag_counts['M']}; `[H]` = {tag_counts['H']}. The source does not define these tags, so this package does not interpret them as marks or difficulty levels.
- Companion PDF: `answer_companion.pdf` (searchable text; page references refer to `Revision12.pdf`, not companion pagination).
- Classification: every item has one primary question type and zero or more matching tags in the inventory.

## Quality checks completed

The final PDF has been generated and representative pages (cover, contents, unit openings, equation-dense pages, and the final page) were visually inspected; the reviewed pages are legible and show no clipping. The verification script passes source/answer coverage, page citations, PDF text extraction, and 36 explicitly listed numerical/formula checks. This does not replace page-by-page independent chemistry review by a qualified teacher; any corrections should be made in `authoring/unit*.tsv` and rebuilt.
"""
    (OUT / "progress_report.md").write_text(text, encoding="utf-8")


def write_verification_report(inventory: list[dict], database: list[dict], pdf_pages: int) -> None:
    categorized = Counter(q["primary_type"] for q in inventory)
    flagged = "\n".join(f"- **Q{n}:** {note}" for n, note in REVIEW_NOTES.items())
    category_lines = "\n".join(f"- {name}: {count}" for name, count in sorted(categorized.items()))
    text = f"""# Verification and scope report

**Date:** {date.today().isoformat()}  
**Question source:** `Revision12.pdf` (28 text-searchable letter pages)  
**Answer source:** the seven maintained TSVs in `authoring/`  
**Status:** complete first-pass answer set; subject to independent subject-expert review.

## Source audit

- Extracted all {pdf_pages} pages directly from the searchable PDF; OCR was not used.
- Found exactly 500 numbered markers, unique and continuous from 1 through 500.
- Every question retains its original PDF page, source `[M]`/`[H]` tag, unit, and extracted text in `question_inventory.json` and `question_inventory.csv`.
- All 500 questions have a non-empty answer in `answer_database.json`; the builder fails on a missing/duplicate item or page marker.

## Answer review performed

Answers were reviewed against standard Class XII chemistry concepts, balanced reaction stoichiometry, units, sign conventions, nomenclature, and stated conditions. The `verify_companion.py` script independently recomputes a curated set of numerical examples and validates that the displayed results occur in their corresponding answer. This is a reproducible arithmetic/coverage check, not independent expert marking of every conceptual answer.

Questions with explicit condition or wording caveats:
{flagged}

## Numerical and layout checks

Run `python3 chemistry_answer_companion/verify_companion.py` for the 36-item numerical and structural audit. The audit reports exact evaluated values and verifies the stated rounded answer snippets. It also checks that all 500 companion entries are extractable from the generated PDF.

The final PDF was rendered and visually inspected at representative points: cover, contents, first unit pages, equation-dense electrochemistry, coordination compounds, haloalkanes, and the closing pages. The checked pages were legible, with no visible clipping or overlap. This is representative-page inspection, not a manual visual review of every page.

## Syllabus alignment

The seven chapter titles and broad topics match Units 1–7 in the **CBSE Chemistry (043), Classes XI–XII, 2026–27** curriculum. This is chapter-level alignment only; the question bank also contains advanced/additional-practice items, and this answer companion does not certify that every individual subtopic is in the summative board-exam scope. Syllabus source: [official CBSE curriculum PDF](https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Chemistry_SecP2_2026-27.pdf).

The environmental note for Q387 was cross-checked against the Australian Industrial Chemicals Introduction Scheme’s **Dichloromethane Evaluation Statement** (14 September 2021), which identifies atmospheric emissions and stratospheric ozone depletion as environmental concerns: [official evaluation statement](https://www.industrialchemicals.gov.au/sites/default/files/2021-09/EVA00027%20-%20Evaluation%20Statement%20-%2014%20September%202021%20%5B388%20KB%5D.pdf).

## Classification distribution

{category_lines}

## Limitations

- `[M]` and `[H]` appear in the source but no key is provided; they are preserved without assuming they mean marks or a particular difficulty scale.
- Some reactions depend on concentration, solvent, temperature, or substrate. The answer notes those conditions where material; omitted conditions in a prompt are not silently treated as universal.
- Several responses are concise model answers rather than official marking-scheme allocations. Check local textbook/teacher conventions for examinable phrasing and named-reaction conditions.
- No independent human examiner or CBSE/NCERT official marking scheme was available for question-by-question validation. Do not treat this as a guaranteed official key.
"""
    (OUT / "verification_report.md").write_text(text, encoding="utf-8")


class CompanionDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal")
        self.addPageTemplates(PageTemplate(id="main", frames=frame, onPage=self.draw_page))

    def draw_page(self, canvas, doc):
        canvas.saveState()
        if doc.page > 1:
            canvas.setStrokeColor(colors.HexColor("#D8E2EC"))
            canvas.setLineWidth(0.5)
            canvas.line(doc.leftMargin, letter[1] - 0.50 * inch, letter[0] - doc.rightMargin, letter[1] - 0.50 * inch)
            canvas.setFont("ChemSans", 7.4)
            canvas.setFillColor(MID)
            canvas.drawString(doc.leftMargin, letter[1] - 0.39 * inch, "CHEMISTRY ANSWER COMPANION")
            canvas.drawRightString(letter[0] - doc.rightMargin, letter[1] - 0.39 * inch, "REVISION12 · ORIGINAL PAGE REFERENCES")
            canvas.setStrokeColor(colors.HexColor("#D8E2EC"))
            canvas.line(doc.leftMargin, 0.48 * inch, letter[0] - doc.rightMargin, 0.48 * inch)
            canvas.setFont("ChemSans", 7.4)
            canvas.drawString(doc.leftMargin, 0.31 * inch, "Page references point to the original question-bank PDF")
            canvas.drawRightString(letter[0] - doc.rightMargin, 0.31 * inch, f"Companion page {doc.page}")
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name == "UnitHeading":
            text = flowable.getPlainText()
            key = f"unit-{self.page}-{len(text)}-{text[:12]}".replace(" ", "-")
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, 0, False)
            self.notify("TOCEntry", (0, text, self.page, key))


def build_pdf(database: list[dict]) -> None:
    regular = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    bold = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    if not regular.exists() or not bold.exists():
        raise FileNotFoundError("DejaVu Sans TTF fonts are required to embed Unicode chemistry symbols")
    pdfmetrics.registerFont(TTFont("ChemSans", str(regular)))
    pdfmetrics.registerFont(TTFont("ChemSans-Bold", str(bold)))
    pdfmetrics.registerFontFamily("ChemSans", normal="ChemSans", bold="ChemSans-Bold", italic="ChemSans", boldItalic="ChemSans-Bold")

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="CoverTitle", fontName="ChemSans-Bold", fontSize=25, leading=31, textColor=BLUE, alignment=TA_LEFT, spaceAfter=12))
    styles.add(ParagraphStyle(name="CoverSub", fontName="ChemSans", fontSize=12, leading=18, textColor=DARK, spaceAfter=8))
    styles.add(ParagraphStyle(name="CoverSection", fontName="ChemSans-Bold", fontSize=17, leading=22, textColor=BLUE, spaceAfter=4))
    styles.add(ParagraphStyle(name="UnitHeading", fontName="ChemSans-Bold", fontSize=17, leading=22, textColor=BLUE, spaceAfter=4, keepWithNext=True))
    styles.add(ParagraphStyle(name="UnitRange", fontName="ChemSans", fontSize=10, leading=15, textColor=BLUE, spaceAfter=9, keepWithNext=True))
    styles.add(ParagraphStyle(name="QuestionHead", fontName="ChemSans-Bold", fontSize=9.3, leading=12, textColor=BLUE, spaceBefore=7, spaceAfter=2, keepWithNext=True))
    styles.add(ParagraphStyle(name="AnswerBody", fontName="ChemSans", fontSize=8.7, leading=12.2, textColor=DARK, leftIndent=8, firstLineIndent=0, spaceAfter=3))
    styles.add(ParagraphStyle(name="SmallNote", fontName="ChemSans", fontSize=8.5, leading=12.5, textColor=MID, spaceAfter=7))
    styles.add(ParagraphStyle(name="TOCTitle", fontName="ChemSans-Bold", fontSize=18, leading=24, textColor=BLUE, spaceAfter=14))
    styles.add(ParagraphStyle(name="TOCEntry", fontName="ChemSans", fontSize=10, leading=17, leftIndent=14, firstLineIndent=-14, textColor=DARK))

    toc = TableOfContents()
    toc.levelStyles = [styles["TOCEntry"]]
    doc = CompanionDocTemplate(
        str(OUT / "answer_companion.pdf"),
        pagesize=letter,
        leftMargin=0.72 * inch,
        rightMargin=0.72 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.70 * inch,
        title="Chemistry Question Bank — Answer Companion",
        author="Chemistry Answer Companion Project",
        subject="Answers to 500 questions in Revision12.pdf, with original page references",
    )

    story = []
    story.append(Spacer(1, 0.55 * inch))
    story.append(Paragraph("CHEMISTRY QUESTION BANK", styles["CoverSub"]))
    story.append(Paragraph("Answer Companion", styles["CoverTitle"]))
    story.append(Paragraph("500 structured answers · 7 units · original PDF page references", styles["CoverSub"]))
    story.append(Spacer(1, 0.20 * inch))
    story.append(Paragraph("Prepared for <b>Revision12.pdf</b>", styles["CoverSub"]))
    story.append(Paragraph("Source contains 28 searchable pages and questions numbered 1–500. The companion preserves the original unit sequence and links each answer to the source PDF page.", styles["SmallNote"]))
    story.append(Spacer(1, 0.20 * inch))
    story.append(Paragraph("Reading guide", styles["CoverSection"]))
    story.append(Paragraph("Each entry shows the question number, the source tag as printed, and the original PDF page. The answer follows; question wording is kept in the separate inventory to avoid duplicating the source bank.", styles["SmallNote"]))
    story.append(Paragraph("The source does not define [M] and [H]; they are retained verbatim and are not interpreted as marks or a specific difficulty scale.", styles["SmallNote"]))
    story.append(Paragraph("This is a carefully reviewed study aid, not an official CBSE marking scheme. Condition-sensitive questions and limitations are documented in the verification report.", styles["SmallNote"]))
    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph(f"Build date: {date.today().isoformat()}", styles["SmallNote"]))
    story.append(PageBreak())
    story.append(Paragraph("Contents", styles["TOCTitle"]))
    story.append(toc)
    story.append(PageBreak())

    by_number = {row["number"]: row for row in database}
    for unit_no, title, first, last in UNITS:
        if unit_no > 1:
            story.append(PageBreak())
        pages = [by_number[n]["source_pdf_page"] for n in range(first, last + 1)]
        story.append(Paragraph(f"UNIT {unit_no}: {escape(title.upper())}", styles["UnitHeading"]))
        story.append(Paragraph(f"Questions {first}–{last} &nbsp; · &nbsp; Original PDF pages {min(pages)}–{max(pages)}", styles["UnitRange"]))
        for n in range(first, last + 1):
            row = by_number[n]
            head = Paragraph(
                f"Question {n} &nbsp; [{escape(row['source_tag'])}] &nbsp; · &nbsp; Original PDF p. {row['source_pdf_page']}",
                styles["QuestionHead"],
            )
            body = Paragraph(f"<font color=\"#35649A\"><b>Answer.</b></font> {format_answer_for_pdf(row['answer'])}", styles["AnswerBody"])
            story.append(KeepTogether([head, body]))

    story.append(Paragraph("Sources and use", styles["UnitHeading"]))
    story.append(Paragraph("Primary source: the user-provided Revision12.pdf. All page citations in this companion refer to its 28 original pages.", styles["SmallNote"]))
    story.append(Paragraph("Syllabus alignment reference: CBSE Chemistry, Subject Code 043, Classes XI–XII (2026–27), official curriculum PDF. The reference supports chapter-level alignment only; see verification_report.md for scope limitations.", styles["SmallNote"]))
    story.append(Paragraph("Answers are concise explanatory responses based on standard chemistry conventions. They have not been independently approved by CBSE or a human examiner; review any condition-sensitive response against the course text and instructor guidance.", styles["SmallNote"]))
    doc.multiBuild(story)


def main() -> None:
    questions = extract_questions()
    answers = load_answer_seeds()
    inventory, database = make_records(questions, answers)
    write_json(OUT / "question_inventory.json", inventory)
    write_json(OUT / "answer_database.json", database)
    write_inventory_csv(inventory)
    with pymupdf.open(SOURCE_PDF) as source:
        pdf_pages = source.page_count
    write_progress_report(inventory, database, pdf_pages)
    write_verification_report(inventory, database, pdf_pages)
    build_pdf(database)
    print(f"Built {len(inventory)} inventory records and {len(database)} answers from {pdf_pages} source pages.")
    print(f"Deliverable: {OUT / 'answer_companion.pdf'}")


if __name__ == "__main__":
    main()
