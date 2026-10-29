# Visual design specification and reference-image audit

**Purpose:** source of visual direction for independently generating the two formula-sheet pages. The existing sheets are style/layout references only; all equation text must come from `formula_manifest.json` and the two page prompts.

## Existing references inspected

- `formula_sheet_1.png` — PNG, 2000 × 2800 px (portrait, approximately 5:7).
- `formula_sheet_2.png` — PNG, 2000 × 2800 px (portrait, approximately 5:7).

Both were opened and reviewed visually. Their visible mathematical content was cross-checked against the supplied NCERT chapter and Class XII syllabus, rather than assumed correct because it appears in the images.

## What to preserve

- **Identity:** warm-white paper, dark navy title and equations, restrained teal/cyan/violet/amber accents, thin separators, rounded topic cards, clean page-number pill.
- **Hierarchy:** strong two-line chapter title; NCERT section numbers in panel headers; formulas more prominent than annotations; compact 1/2 and 2/2 markers.
- **Type treatment:** readable sans-serif headings and annotations, serif-style equation lines, consistent subscripts/superscripts, no handwriting for formula characters.
- **Sequence:** page 1 handles mirrors → refraction → TIR → spherical surface; page 2 continues through lenses → prism → microscopes → astronomical telescope.
- **Useful style:** the neutral background and calm accent palette keep contrast strong; the simple cards make a dense reference page scannable.

Approximate palette to reproduce, not a demand for exact sampled pixels: warm ivory `#FBFAF6`, navy `#142B45`, teal `#138B91`, cyan `#4EB8C0`, violet `#7763A8`, amber `#D79631`, pale teal `#EEF6F4`, pale blue `#F0F3FA`, pale amber `#FBF2E3`, and white card surfaces.

## Weaknesses to correct in generated revisions

1. **Excess unused space:** both pages have large blank areas inside cards and between content blocks. Tighten panel heights and vertical gaps; distribute approved content more evenly. Do not solve this by shrinking equations to microtext or adding unsupported filler.
2. **Footer crop:** the rightmost footer/brand text reaches or crosses the safe edge on the existing pages. Keep all marks inside a generous safe margin; omit nonessential footer wording if it risks clipping.
3. **Diagram ambiguity:** the page-1 TIR sketch has no arrowheads, so ray direction is not immediately explicit. Its labels are visually separated from the ray paths. Add clear arrows, a normal, `i > i_c`, and explicit denser/rarer labels, or omit the diagram if it cannot be rendered correctly.
4. **Decorative top motif:** the small unlabelled converging-ray mark is attractive but not strongly informative. Replace it with a useful physical sketch or remove it.
5. **Page 2 diagram scarcity:** the current second sheet has no explanatory diagram. If space permits, use one small accurate prism ray path or a normal-adjustment telescope layout with labelled objective/eyepiece; equations still take priority.
6. **Formula typography:** the existing equation sizes are readable when enlarged, but subscript-heavy lines can become small at ordinary screen scale. Keep formulas large, use explicit fraction bars and crisp subscripts, align equals signs, and wrap long expressions deliberately.
7. **Notation clarity:** use the exact manifest notation, especially `n_21=n_2/n_1`, `i_c`, `n_d`, `n_r`, the minus signs in signed magnifications, and positive focal-length magnitudes in telescope formulae. Never let the generator infer notation from the visual reference.
8. **Information density:** the visual style is polished but less space-efficient than the requested high-density revision sheet. Use content-sized panels, balanced columns, tighter prose and equation-first layout; retain adequate line spacing and safe margins.

## Layout and rendering targets

- **Orientation:** portrait; use a supported **3:4** image ratio when the selected model exposes that setting. The current reference pages are about 5:7, but 5:7 is not listed in the current Gemini image-generation ratios.
- **Gemini API setting (when available):** 3:4, 2K. The current Google documentation lists 3:4 among available ratios and 2K as an output size; the documented 2K 3:4 raster is 1792 × 2400 px. A UI or third-party model may expose different controls, so choose its closest portrait option rather than claiming a fixed size is universal.
- **Safe area:** at least 5% inset on all sides; no text, page marker or footer near the crop boundary.
- **Suggested structure:** page 1 uses two balanced columns with the long refraction section allowed a wider panel; page 2 uses wide lens/prism content and a dedicated instrument column/region. Avoid narrow columns for long equations.
- **Typography:** equations in a high-legibility math serif or LaTeX-style face; headings/definitions in a neutral sans serif. Body annotation should remain readable at normal zoom. Use one math size for primary equations and a smaller but still legible size for brief conditions.
- **Annotations:** keep each definition/condition adjacent to the formula it qualifies. Put the shared Cartesian convention in one compact callout on page 1 and repeat only essential instrument-specific interpretation on page 2.
- **Diagrams:** page 1 may include one ray sketch for TIR; page 2 may include one prism or telescope diagram. Use thin navy/cyan/violet rays, directional arrowheads and clear labels. Diagrams are subordinate and optional: remove them if they compete with mathematical text.
- **No source references on the visual sheets** unless space allows a tiny NCERT label; source details stay in the manifest.

## Generator capability notes (checked 2026-10-29)

Google’s current model page identifies **Nano Banana 2.1**, model code `gemini-nano-banana-2.1`, as a stable image-generation and conversational-editing model. It accepts image inputs and supports multi-image fusion (up to 14 reference images); its page describes improved text rendering and infographic layout, while the general guide supports text-and-image inputs and output-format configuration. That makes attaching both existing pages as visual references a supported workflow. This is not a guarantee of character-perfect mathematics.

The Gemini image-generation guide documents aspect-ratio and image-size settings, including 3:4 and 2K. For API usage, those controls belong in image output configuration; in a consumer UI, use them only if actually exposed. A prompt cannot force unsupported settings.

Sources:

- [Gemini Nano Banana 2.1 model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1) — model identifier, image inputs, reference-image fusion and text/layout capability notes.
- [Gemini image-generation documentation](https://ai.google.dev/gemini-api/docs/image-generation) — reference image workflow, aspect-ratio/image-size configuration and image output examples.
- [Gemini 3.1 Flash Image model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image) — previous-generation related model information.

## Exactness boundary

**Immutable:** title/page number, NCERT section sequence, each formula and sign, all IDs, symbol definitions, conditions, units and sign-convention notes in the applicable prompt and manifest. Do not allow the model to rewrite any of them.

**Creative latitude:** card shapes, accent placement, subtle grid/optical motifs, diagram style within stated physical constraints, typography pairing and micro-spacing. Creativity must never add content or interfere with formulas.

**Fallback:** if any mathematical glyph, fraction, subscript, unit, sign or annotation is wrong, do not accept the attractive image as a final scientific sheet. Use the deterministic typesetting/compositing workflow documented in `quality_checklist.md`.
