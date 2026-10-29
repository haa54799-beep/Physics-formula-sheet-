# Formula-sheet generation and quality-control checklist

This checklist distinguishes the **existing repository sheets** (already inspected as visual references) from any **new image-model outputs** (not generated or validated by this package). The manifest is the approved source of truth. Never mark a future generated output “verified” based only on appearance.

## 1. Files to use

For **each** independent generation request, upload/attach these two files as image references:

- `formula_sheet_1.png`
- `formula_sheet_2.png`

Then paste the full contents of only the corresponding prompt:

- First request: `image_prompt_1.md` → generate only page 1, marker `1/2`.
- Separate second request: `image_prompt_2.md` → generate only page 2, marker `2/2`.

Attach both references to both requests so the model can match the set. Do not use page 1’s newly generated output as a replacement style reference for the second request; always attach the same two existing repository pages. The prompts are self-contained; the JSON is optional for auditing, not a required text/image upload to the model.

**Current suggested Gemini model:** Nano Banana 2.1 (`gemini-nano-banana-2.1`). Current official documentation reports image input and multi-image reference fusion and supports enhanced text/infographic rendering; these capabilities improve the workflow but do **not** guarantee exact math. When the interface/API exposes output controls, use portrait 3:4 and 2K; otherwise choose the closest portrait option actually offered. Do not assume a third-party model has the same controls.

## 2. Baseline audit of existing repository images

Both source reference PNGs were visually inspected at their 2000 × 2800 pixel size. They are used below only as visual references; formula acceptance is based on `formula_manifest.json` and the supplied source documents.

### Visual findings

- Strengths: coherent warm ivory/navy/teal/cyan/violet/amber palette; clear page markers; consistent rounded topic panels; sans-serif headings with serif-style equations; NCERT topic sequence flows across two pages.
- Fix in the new design: large unused interiors in multiple cards; density/spacing is uneven; bottom-right footer/brand text is pressed against or clipped by the page edge; top decorative convergence motif has no instructional labels; TIR rays lack arrowheads and their direction is ambiguous; page 2 lacks a useful physical diagram. Improve these without shrinking equations to illegibility or adding filler.
- Math review: every topic/ID has its principal relationship represented on its intended existing page, but the references are not fully complete against the expanded manifest. Two small variants are visibly absent: RO-018’s ratio `f_2/f_1=-n_2/n_1` and RO-023’s centimetre conversion `P(D)=100/f_cm`. RO-014’s core/cladding condition is written in prose (“core index > cladding index”), not as an explicit equation. Add these as exact math in any regenerated version. Important visible notation/signs checked include `1/v+1/u=1/f` for mirrors, `1/v-1/u=1/f` for lenses, the opposite mirror/lens magnification sign, the `n_21` medium order, `n_d/n_r` at critical angle, prism minimum deviation, microscope image-orientation signs, and telescope signed `M`. The TIR figure’s missing arrows are a diagram-quality issue, not a formula correction.
- Supplemental content already on the current pages (e.g. wavelength index relation, slab shift, surface focal lengths) is accepted only where it is separately marked in the manifest; excluded or unresolved source expressions must not enter a generated image.

## 3. Formula-by-formula audit matrix

**Baseline:** `Yes` means fully present; `Partial` means the principal relationship is shown but a listed equivalent form is missing; `Prose only` means the concept appears without the required explicit equation. **New output:** leave unchecked until a new generation is manually compared character-by-character, including all signs, indices, exponents, fractions, units and conditions.

| ID | Expected page | Existing reference present/intact | New output: present | New output: exact / intact |
|---|---:|---|---|---|
| RO-001 | 1 | Yes | [ ] | [ ] |
| RO-002 | 1 | Yes | [ ] | [ ] |
| RO-003 | 1 | Yes | [ ] | [ ] |
| RO-004 | 1 | Yes | [ ] | [ ] |
| RO-005 | 1 | Yes | [ ] | [ ] |
| RO-006 | 1 | Yes | [ ] | [ ] |
| RO-007 | 1 | Yes | [ ] | [ ] |
| RO-008 | 1 | Yes | [ ] | [ ] |
| RO-009 | 1 | Yes | [ ] | [ ] |
| RO-010 | 1 | Yes | [ ] | [ ] |
| RO-011 | 1 | Yes | [ ] | [ ] |
| RO-012 | 1 | Yes | [ ] | [ ] |
| RO-013 | 1 | Yes | [ ] | [ ] |
| RO-014 | 1 | Prose only; add explicit equation | [ ] | [ ] |
| RO-015 | 1 | Yes | [ ] | [ ] |
| RO-016 | 1 | Yes | [ ] | [ ] |
| RO-017 | 1 | Yes | [ ] | [ ] |
| RO-018 | 1 | Partial; f_2/f_1 ratio absent | [ ] | [ ] |
| RO-019 | 2 | Yes | [ ] | [ ] |
| RO-020 | 2 | Yes | [ ] | [ ] |
| RO-021 | 2 | Yes | [ ] | [ ] |
| RO-022 | 2 | Yes | [ ] | [ ] |
| RO-023 | 2 | Partial; cm conversion absent | [ ] | [ ] |
| RO-024 | 2 | Yes | [ ] | [ ] |
| RO-025 | 2 | Yes | [ ] | [ ] |
| RO-026 | 2 | Yes | [ ] | [ ] |
| RO-027 | 2 | Yes | [ ] | [ ] |
| RO-028 | 2 | Yes | [ ] | [ ] |
| RO-029 | 2 | Yes | [ ] | [ ] |
| RO-030 | 2 | Yes | [ ] | [ ] |
| RO-031 | 2 | Yes | [ ] | [ ] |
| RO-032 | 2 | Yes | [ ] | [ ] |
| RO-033 | 2 | Yes | [ ] | [ ] |
| RO-034 | 2 | Yes | [ ] | [ ] |
| RO-035 | 2 | Yes | [ ] | [ ] |
| RO-036 | 2 | Yes | [ ] | [ ] |
| RO-037 | 2 | Yes | [ ] | [ ] |
| RO-038 | 2 | Yes | [ ] | [ ] |
| RO-039 | 2 | Yes | [ ] | [ ] |

### Out-of-scope and unresolved guardrail

Confirm none of the following appears as if it were an approved core formula:

- The unresolved photographed second “denser-to-rarer” special-case surface equation. It remains `[VERIFY]`; use only RO-015’s general NCERT form.
- Separated-lens focal length/power relations (syllabus says lenses in contact).
- Prism-dispersion, angular-dispersion or dispersive-power relations (not explicit in the supplied chapter-9 syllabus entry).
- Terrestrial/Galilean telescope formulae.
- Plane-mirror rotation relation, wave-optics or unrelated formulas.

## 4. Mathematical verification checklist

For each generated page, inspect at full size and compare every `RO-###` with the exact `expression` in `formula_manifest.json`:

- [ ] No formula omitted, duplicated, extra, reordered across topic boundaries or altered.
- [ ] All minus signs, equality signs, approximate signs, inequalities, brackets and reciprocal placements match.
- [ ] Every subscript is correct (`n_21` versus `n_12`; `f_o` versus `f_e`; `r_1` versus `r_2`; `i_c`).
- [ ] Mirror and lens equations/magnifications are not interchanged.
- [ ] Source labels/notations are consistent; no mixed definitions of incident and transmitted media.
- [ ] Units are correct: distance/radius/focal length in m (or consistently common length units); lens/surface power in m⁻¹ (D); angles measured from normal; `n`, `m`, `M` dimensionless.
- [ ] Conditions and approximations remain adjacent and correct: paraxial mirror/surface/lens; near-normal apparent depth/shift; thin-prism small angle; microscope near-point/infinity cases; telescope normal adjustment.
- [ ] Signed magnification and absolute magnifying-power magnitude are distinguished, especially for compound microscope and telescope.
- [ ] Every supplementary mark is retained where specified; no `[VERIFY]` or excluded expression appears.

If any symbol is uncertain at display scale, treat it as a failure, not a pass. Do not infer an ambiguous glyph from context and call the image accurate.

## 5. Diagram and visual inspection checklist

- [ ] Portrait page, correct page number and title; same palette, margins and typography between pages.
- [ ] 3:4 layout if supported; use 2K only if model/interface exposes it. Confirm actual dimensions after saving.
- [ ] All content fits within safe margins; footer/page marker are not clipped.
- [ ] Text remains readable at normal viewing scale; no tiny equation text to force a fit.
- [ ] No overlap, broken words, broken fractions, characters substituted by boxes, excessive blank cards or decorative clutter.
- [ ] Any TIR diagram has incident/reflected arrowheads, correct denser-to-rarer direction, normal, `i>i_c`, index labels and no transmitted ray.
- [ ] Any prism diagram uses correctly directed rays and labels consistent with the prism angle/deviation equations; telescope diagram has objective/eyepiece and correct normal-adjustment orientation.
- [ ] Remove a diagram rather than keep one that is ambiguous or physically inconsistent.

## 6. Deterministic typesetting/compositing fallback

If a direct generated image fails even one formula-integrity check, use this fallback rather than accepting it:

1. Ask the image generator for **background, card layout inspiration and decorative ray/prism artwork only**. Explicitly reserve blank content areas; do not let it draw letters, formulas, labels or numbers.
2. Use `formula_manifest.json` as immutable copy. Typeset formula strings with LaTeX/KaTeX/MathJax into SVG/PDF or another deterministic math-rendering system. Use Unicode-safe text fonts for definitions, units and panel headings.
3. Lay out title, formula blocks, definitions, conditions and symbols in an SVG or document-layout tool (e.g. Inkscape, Figma, Affinity, ReportLab/HTML+SVG). Keep every equation as deterministic vector/text output. Add labels to diagrams with the same text/layout tool, not the image model.
4. Composite those layers over the generated background. Export a portrait PNG at the chosen available resolution; do not upscale a small output and claim it is native high resolution.
5. Re-run the full matrix in section 3 and the checks in sections 4–5. Preserve the two-page allocation in the manifest. If any line does not fit, rebalance panel sizes or shorten only nontechnical annotation that the manifest marks as nonformula prose; do not rewrite formulas or drop conditions.

## 7. Completion record

Current status: **prompt package complete; existing source images audited; no fresh model-generated outputs are part of this package.** The table’s new-output columns are intentionally blank. Complete them only after independently generating and inspecting the two pages. The manifest enumerates every approved formula exactly once across the two pages: `RO-001`–`RO-018` on page 1 and `RO-019`–`RO-039` on page 2.
