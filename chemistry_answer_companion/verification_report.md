# Verification and scope report

**Date:** 2026-10-30  
**Question source:** `Revision12.pdf` (28 text-searchable letter pages)  
**Answer source:** the seven maintained TSVs in `authoring/`  
**Status:** complete first-pass answer set; subject to independent subject-expert review.

## Source audit

- Extracted all 28 pages directly from the searchable PDF; OCR was not used.
- Found exactly 500 numbered markers, unique and continuous from 1 through 500.
- Every question retains its original PDF page, source `[M]`/`[H]` tag, unit, and extracted text in `question_inventory.json` and `question_inventory.csv`.
- All 500 questions have a non-empty answer in `answer_database.json`; the builder fails on a missing/duplicate item or page marker.

## Answer review performed

Answers were reviewed against standard Class XII chemistry concepts, balanced reaction stoichiometry, units, sign conventions, nomenclature, and stated conditions. The `verify_companion.py` script independently recomputes a curated set of numerical examples and validates that the displayed results occur in their corresponding answer. This is a reproducible arithmetic/coverage check, not independent expert marking of every conceptual answer.

Questions with explicit condition or wording caveats:
- **Q102:** Aqueous NaCl anode product depends on chloride concentration: concentrated brine gives Cl₂; very dilute chloride may give O₂. The answer states both cases.
- **Q387:** The environmental concern is specific: an official Australian chemical evaluation identifies atmospheric emissions of dichloromethane as contributing to stratospheric ozone depletion.
- **Q144:** The metal-ion charge is not specified, so the direction is determinate but a unique numerical EMF is not. A general z-valent Nernst expression is supplied.
- **Q393:** Persistence varies across modern pesticides; the answer avoids treating all newer compounds as a single safer class.
- **Q403:** AgNO₃ behaviour depends on whether the organic halide releases halide ion; sample preparation and suitable conditions matter.
- **Q425:** The question does not specify substrate or mechanism. The answer gives the stereogenic-centre criterion and CIP method, then distinguishes SN2 inversion from other outcomes.

## Numerical and layout checks

Run `python3 chemistry_answer_companion/verify_companion.py` for the 36-item numerical and structural audit. The audit reports exact evaluated values and verifies the stated rounded answer snippets. It also checks that all 500 companion entries are extractable from the generated PDF.

The final PDF was rendered and visually inspected at representative points: cover, contents, first unit pages, equation-dense electrochemistry, coordination compounds, haloalkanes, and the closing pages. The checked pages were legible, with no visible clipping or overlap. This is representative-page inspection, not a manual visual review of every page.

## Syllabus alignment

The seven chapter titles and broad topics match Units 1–7 in the **CBSE Chemistry (043), Classes XI–XII, 2026–27** curriculum. This is chapter-level alignment only; the question bank also contains advanced/additional-practice items, and this answer companion does not certify that every individual subtopic is in the summative board-exam scope. Syllabus source: [official CBSE curriculum PDF](https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Chemistry_SecP2_2026-27.pdf).

The environmental note for Q387 was cross-checked against the Australian Industrial Chemicals Introduction Scheme’s **Dichloromethane Evaluation Statement** (14 September 2021), which identifies atmospheric emissions and stratospheric ozone depletion as environmental concerns: [official evaluation statement](https://www.industrialchemicals.gov.au/sites/default/files/2021-09/EVA00027%20-%20Evaluation%20Statement%20-%2014%20September%202021%20%5B388%20KB%5D.pdf).

## Classification distribution

- comparison/classification: 43
- definition/concept: 117
- derivation: 9
- explanation/application: 159
- nomenclature/formula: 10
- quantitative/problem-solving: 46
- reaction/equation: 116

## Limitations

- `[M]` and `[H]` appear in the source but no key is provided; they are preserved without assuming they mean marks or a particular difficulty scale.
- Some reactions depend on concentration, solvent, temperature, or substrate. The answer notes those conditions where material; omitted conditions in a prompt are not silently treated as universal.
- Several responses are concise model answers rather than official marking-scheme allocations. Check local textbook/teacher conventions for examinable phrasing and named-reaction conditions.
- No independent human examiner or CBSE/NCERT official marking scheme was available for question-by-question validation. Do not treat this as a guaranteed official key.
