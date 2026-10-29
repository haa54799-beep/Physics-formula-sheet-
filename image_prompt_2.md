# Image-generation prompt — page 2 of 2

## Before you generate

**Preferred model:** Google Gemini Nano Banana 2.1 (stable API model code `gemini-nano-banana-2.1`); another image generator that accepts two reference images may also be used. Gemini API parameter availability can differ from its consumer UI.

Attach **both** repository images as reference inputs to this request:

1. `formula_sheet_1.png`
2. `formula_sheet_2.png`

Use them only to match the coordinated visual identity, palette, typography hierarchy, panel language and page-to-page continuity. **Do not copy, infer, transcribe, repair or treat any equation in either reference image as authoritative.** The complete content below and the NCERT/syllabus notation encoded here are authoritative. Generate only page 2. Do not generate page 1 again or a two-page composite.

## Paste-ready prompt

```text
Create ONE portrait educational formula-sheet image: page 2 of 2 in the same coordinated Class XII Physics revision set.

EXACT TITLE (typeset on two lines if needed):
RAY OPTICS & OPTICAL INSTRUMENTS
FORMULA SHEET

PAGE MARKER: 2/2
Language: English. This is the continuation of page 1. The approved formula text below is immutable. Treat both attached existing pages only as visual references; do not copy their equation content.

CANVAS / STYLE
Use a portrait 3:4 composition. If the tool exposes output controls, choose 3:4 and 2K; do not claim or simulate a setting the interface does not offer. Match the warm ivory, navy, teal/cyan/violet/amber palette, clean sans-serif headings, math-serif equations, rounded pale topic cards, fine separators and safe margins of page 1. Improve the references’ uneven density, large blank panel interiors and crowded/cut right-edge footer. Use balanced content-sized panels, not large fixed empty boxes. Keep page number/footer well inside the safe area. Formula content should dominate, annotation should support it.

Use a crisp mathematical serif/LaTeX-like face for equations and a clean sans-serif for headings/definitions. Render fractions and all subscripts/superscripts clearly, with explicit signs. Never use handwriting for equations, symbols or units. Keep background quiet behind math; no decorative clutter.

LAYOUT / CHAPTER SEQUENCE
Continue NCERT order with these headings, exactly:
1. 9.5.2–9.5.4 THIN LENSES
2. 9.6 REFRACTION THROUGH A PRISM
3. 9.7.1 MICROSCOPES — SIMPLE AND COMPOUND
4. 9.7.2 ASTRONOMICAL TELESCOPE — REFRACTING AND REFLECTING
Use a balanced portrait layout: lens equations may occupy a wide upper panel; group prism formulae together; keep microscope cases together and telescope at the end. Do not split a formula from its symbol/condition note. Keep longer equations on a wide line; do not force tiny narrow columns.

APPROVED FORMULAS — PRINT THESE EXACTLY, WITHOUT ADDITIONS OR OMISSIONS

9.5.2–9.5.4 THIN LENSES
[RO-019] Lens-maker formula in a surrounding medium:  1/f = (n_2/n_1 - 1)(1/R_1 - 1/R_2)
[RO-020] Lens-maker formula in air:  1/f = (n - 1)(1/R_1 - 1/R_2)
[RO-021] Thin-lens equation:  1/v - 1/u = 1/f
[RO-022] Linear magnification:  m = h_i/h_o = v/u
[RO-023] Lens power:  P = 1/f_m;  P(D) = 100/f_cm;  1 D = 1 m^-1
[RO-024] Thin lenses in contact:  1/F = sum_j(1/f_j);  P = sum_j P_j
[RO-025] Lens-combination magnification:  m_total = m_1 m_2 m_3 ...

9.6 REFRACTION THROUGH A PRISM
[RO-026] Prism geometry:  A = r_1 + r_2
[RO-027] Deviation:  delta = i + e - A
[RO-028] At minimum deviation:  i=e; r_1=r_2=A/2;  n_21 = sin[(A+delta_m)/2]/sin(A/2)
[RO-029] Thin prism:  delta approximately (n_21 - 1)A

9.7.1 MICROSCOPES — SIMPLE AND COMPOUND
[RO-030] Angular magnification definition:  M = theta_i/theta_o
[RO-031] Simple microscope, final image at near point:  M = 1 + D/f
[RO-032] Simple microscope, final image at infinity:  M = D/f
[RO-033] Compound microscope objective:  m_o = v_o/u_o approximately -L/f_o
[RO-034] Compound microscope eyepiece, final image at near point:  M_e = 1 + D/f_e
[RO-035] Compound microscope eyepiece, final image at infinity:  M_e = D/f_e
[RO-036] Compound microscope total, final image at near point:  M = m_o M_e = (v_o/u_o)(1 + D/f_e)
[RO-037] Compound microscope total, final image at infinity:  M approximately -(L/f_o)(D/f_e)

9.7.2 ASTRONOMICAL TELESCOPE — REFRACTING AND REFLECTING
[RO-038] Angular magnification:  M = -f_o/f_e; magnifying-power magnitude |M| = f_o/f_e
[RO-039] Normal adjustment (final image at infinity):  s_tel = f_o + f_e
Use positive focal-length magnitudes f_o and f_e in these instrument expressions; the leading minus sign denotes an inverted final image. For a reflecting telescope, f_o is the magnitude of the concave objective mirror’s focal length.

SYMBOL KEY / UNITS / CONDITIONS
Include a concise key near the relevant panels:
- n_1 is surrounding-medium index and n_2 lens index in RO-019; n is lens index relative to air in RO-020. Refractive indices are dimensionless.
- u,v are signed object/image distances from the optical centre; f is signed lens focal length; R_1,R_2 are signed radii. Use metres in SI or one common length unit. Thin-lens and lens-maker relations assume a thin lens and paraxial rays.
- h_o,h_i are signed object/image heights; m is dimensionless. Do not copy the mirror magnification minus sign into RO-022.
- Power P is in dioptres when f is in metres: 1 D=1 m^-1. P positive for a converging lens and negative for a diverging lens. F,f_j are focal lengths of thin lenses in contact; the power sum is algebraic.
- A is prism refracting angle; i and e are incidence and emergence angles; r_1,r_2 are the internal refraction angles; delta is deviation; delta_m is minimum deviation; n_21 is prism index relative to its surrounding medium. Angles are in radians in SI; use one angle unit consistently. RO-029 is a small-angle/thin-prism approximation only.
- theta_i/theta_o are image/object viewing angles; M is dimensionless angular magnification. D is the least distance of distinct vision, approximately 25 cm for a normal eye.
- For the compound microscope, f_o,f_e are objective/eyepiece focal lengths; u_o,v_o are signed object/image distances for the objective; L is the tube length between the objective’s second focus and eyepiece’s first focus. The minus sign in the objective relation records the inverted intermediate image. The L/f_o total-power forms are approximations.
- In the telescope formulas, f_o and f_e are positive focal-length magnitudes, s_tel is objective-to-eyepiece separation in normal adjustment, and negative signed M marks an inverted final image. All lengths in each ratio must use the same unit.

DIAGRAM
Use no more than one small optional physical diagram: either (a) a triangular prism with arrowed incident/internal/emergent ray and labels A, i, r_1, r_2, e, delta, or (b) a normal-adjustment astronomical telescope with an objective, eyepiece, principal axis and image at infinity. Do not add formula labels not listed above. No dispersion/rainbow diagram. If the diagram cannot be accurate, omit it.

STRICT CONTENT / NEGATIVE INSTRUCTIONS
Title, 2/2 marker, headings/order, all formulas, symbols, definitions, units, conditions, approximations and sign notes above are immutable. Do not invent, omit, derive, simplify, rearrange, duplicate, combine or alter equations. Do not add dispersion or dispersive power, separated-lens combinations, terrestrial/Galilean telescope formulas, human-eye formulas, wave optics or unsupported extras. Do not change signs, subscript indices, Greek letters, approximation markers, units or variable roles. Do not assign units to dimensionless indices or magnifications. No garbled/illegible text, incorrect symbols, duplicate formulas, clipping, overlaps, colliding labels, broken fractions, tiny type, excessive whitespace, excessive decoration, watermark, off-edge footer or crop. Avoid cramped columns and keep all formulas readable at normal zoom. Return only one finished page image.

IMPORTANT HONESTY RULE
Even a strong image model can alter a subscript, minus sign or fraction in dense scientific text. Do not claim formula integrity without checking every RO-019–RO-039 expression against the prompt/manifest. If any text is not exact, use the deterministic typesetting fallback in the package quality checklist.
```

## Manifest mapping

Page 2 contains exactly `RO-019`–`RO-039`, in the topic sequence above. Source metadata, conditions and audit status are in `formula_manifest.json`.
