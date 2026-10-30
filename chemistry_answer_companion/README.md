# Chemistry Question Bank — Answer Companion

This package contains a question-by-question study companion for the supplied `Revision12.pdf`. It preserves the source’s seven-unit sequence, original question numbers, and the PDF page on which each question appears.

## Deliverables

- `answer_companion.pdf` — searchable, typeset answer companion. It shows question number, the source `[M]`/`[H]` tag, answer, and **original `Revision12.pdf` page**. It does not reprint the question text.
- `question_inventory.json` — full extracted question text plus stable ID, unit, source page/tag, and type classification.
- `question_inventory.csv` — spreadsheet-friendly equivalent of the inventory.
- `answer_database.json` — structured records joining each question and source reference to its answer and review status.
- `progress_report.md` — coverage and current project status.
- `verification_report.md` — verification scope, caveats, syllabus alignment, and limitations.
- `build_companion.py` — reproducibly extracts the inventory, joins the maintained answer source, writes the structured data/reports, and builds the PDF.
- `verify_companion.py` — checks completeness, source-page references, the searchable PDF, and curated numerical results.
- `authoring/unit1.tsv` … `authoring/unit7.tsv` — canonical editable answers, one numbered answer per line. Edit these files, then rebuild.

## Rebuild

From the repository root, install Python 3 dependencies and run:

```bash
python3 -m venv .venv
.venv/bin/pip install pymupdf reportlab
.venv/bin/python chemistry_answer_companion/build_companion.py
.venv/bin/python chemistry_answer_companion/verify_companion.py
```

The PDF generator embeds DejaVu Sans to retain Greek letters, arrows, subscripts, superscripts, and searchable text. On a different operating system, install the DejaVu Sans TTF fonts at `/usr/share/fonts/truetype/dejavu/` or adjust the font paths in `build_companion.py`.

## Editorial and source notes

- Source audit found 28 searchable text pages and 500 unique, sequential questions (Q1–Q500); no OCR was needed. Page numbers in the companion refer to the source PDF, not the companion’s pagination.
- The source uses `[M]` and `[H]` but provides no legend. The tags are retained as printed and are **not** interpreted as marks or a defined difficulty scale.
- Chapter names align with Units 1–7 of the official CBSE Chemistry Subject Code 043 curriculum for Classes XI–XII, 2026–27: [official curriculum PDF](https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Chemistry_SecP2_2026-27.pdf). This is chapter-level alignment, not a guarantee that every advanced/additional-practice detail is in summative examination scope.
- The environmental statement in Q387 was cross-checked with the Australian Industrial Chemicals Introduction Scheme’s [Dichloromethane Evaluation Statement (2021)](https://www.industrialchemicals.gov.au/sites/default/files/2021-09/EVA00027%20-%20Evaluation%20Statement%20-%2014%20September%202021%20%5B388%20KB%5D.pdf), which identifies atmospheric emissions and stratospheric ozone depletion as concerns.
- Standard chemistry conventions and equations are used. The verification script recomputes a curated set of numerical answers and validates all 500 records and PDF references. It is not an independent expert re-marking of every conceptual answer.
- Questions with meaningful conditions or underspecified details are called out in `verification_report.md` and in their database records. In particular, the anode product in aqueous NaCl depends on chloride concentration, and the concentration-cell EMF needs the metal-ion charge.
- This is a reviewed study aid, not an official CBSE marking scheme. No human examiner or official question-specific marking scheme was available for independent validation.
