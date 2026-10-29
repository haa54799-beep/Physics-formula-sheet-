# Image-generation prompt — page 1 of 2

## Before you generate

**Preferred model:** Google Gemini Nano Banana 2.1 (stable API model code `gemini-nano-banana-2.1`); another image generator that accepts two reference images may also be used. Gemini API parameter availability can differ from its consumer UI.

Attach **both** repository images as reference inputs to this request:

1. `formula_sheet_1.png`
2. `formula_sheet_2.png`

Use them only to match the coordinated visual identity, palette, typography hierarchy, panel language and page-to-page continuity. **Do not copy, infer, transcribe, repair or treat any equation in either reference image as authoritative.** The complete content below and the NCERT/syllabus notation encoded here are authoritative. Generate only page 1. Do not generate a second page or a two-page composite.

## Paste-ready prompt

```text
Create ONE portrait educational formula-sheet image: page 1 of 2 in a coordinated Class XII Physics revision set.

EXACT TITLE (typeset on two lines if needed):
RAY OPTICS & OPTICAL INSTRUMENTS
FORMULA SHEET

PAGE MARKER: 1/2
Language: English. Topic order and all formula content below are locked. Treat the two attached pages only as visual references for style. Never copy their math; use only this approved specification.

CANVAS / STYLE
Use a portrait 3:4 composition. If the tool exposes output controls, choose 3:4 and 2K; do not claim or simulate a setting the interface does not offer. Warm ivory paper, deep-navy type, restrained teal/cyan/violet/amber accents, pale tinted section panels, fine separators, generous outer safe margins, and a clear page marker. Match the useful calm, coordinated, academic look of the two references, but improve their large unused card interiors, uneven density and footer crowding. Use content-sized panels and balanced columns. The footer/page mark must stay well inside the canvas edge.

Use clean sans-serif topic headings and annotations; use a crisp, mathematically literate serif/LaTeX-like face for equations. Fractions must be visibly fraction-like, not run-on slash text where space permits. Keep superscripts/subscripts, Greek letters, minus signs, primes and inequality signs exact. Equations must be larger than explanatory copy. Handwritten accents may appear only as tiny decorative emphasis, never for equations, variable labels, units or conditions. Keep background quiet behind math.

LAYOUT / CHAPTER SEQUENCE
Arrange four topic panels in exactly this NCERT order:
1. 9.2 REFLECTION OF LIGHT BY SPHERICAL MIRRORS
2. 9.3 REFRACTION
3. 9.4 TOTAL INTERNAL REFLECTION
4. 9.5.1 REFRACTION AT A SPHERICAL SURFACE
Include one shared, compact “NCERT Cartesian sign convention” callout near the lower/outer edge. Balance panel heights to the content; do not leave giant blank card areas. A two-column layout is suitable, with the refraction panel allowed extra width or height.

APPROVED FORMULAS — PRINT THESE EXACTLY, WITHOUT ADDITIONS OR OMISSIONS

9.2 REFLECTION OF LIGHT BY SPHERICAL MIRRORS
[RO-001] Law of reflection:  i = r
[RO-002] Focal length:  f = R/2  (paraxial rays)
[RO-003] Mirror equation:  1/v + 1/u = 1/f = 2/R
[RO-004] Linear magnification:  m = h_i/h_o = -v/u

9.3 REFRACTION
[RO-005] Absolute refractive index:  n = c/v_light
[RO-006] Wavelength form:  n = lambda_0/lambda
[RO-007] Snell’s law:  n_21 = sin(i)/sin(r) = n_2/n_1; equivalently n_1 sin(i) = n_2 sin(r)
[RO-008] Relative-index reciprocity/chaining:  n_12 = 1/n_21;  n_31 = n_32 n_21
[RO-009] Near-normal apparent depth:  n_21 ≈ real depth/apparent depth; for viewing from air, apparent depth ≈ real depth/n
[RO-010] Plane-parallel slab lateral shift:  d = t sin(i-r)/cos(r)
[RO-011] Near-normal apparent rise:  apparent shift = t(1-1/n); for stacked layers, total apparent shift ≈ sum_j t_j(1-1/n_j)
Mark RO-005, RO-006, RO-010 and RO-011 with a very small “supplementary” tag, not as new syllabus mandates. Keep that tag beside the relevant content, not attached to the equation ambiguously.

9.4 TOTAL INTERNAL REFLECTION
[RO-012] Critical angle:  sin(i_c) = n_r/n_d; for a rarer medium that is air, n_d ≈ 1/sin(i_c)
[RO-013] TIR conditions:  n_d > n_r and i > i_c
[RO-014] Optical fibre index condition:  n_core > n_cladding
At i=i_c, the refracted ray grazes the interface (r=90 degrees); that limiting case is not the i>i_c TIR condition.

9.5.1 REFRACTION AT A SPHERICAL SURFACE
[RO-015]  n_2/v - n_1/u = (n_2-n_1)/R
[RO-016] Supplementary surface power:  P_s = (n_2-n_1)/R; in air, P_s=(n-1)/R
[RO-017] Supplementary first principal focal length:  f_1 = -n_1 R/(n_2-n_1)
[RO-018] Supplementary second principal focal length and ratio:  f_2 = n_2 R/(n_2-n_1);  f_2/f_1 = -n_2/n_1
Use a concise paraxial note for RO-015–RO-018. Never include the unresolved two-case spherical-interface expression from the supplement; the general NCERT equation above is the approved version.

SYMBOL KEY / UNITS / CONDITIONS
Define symbols once in a compact key and add a brief condition beside the relevant panel:
- u,v are signed object/image distances measured from the mirror pole or lens optical centre; f is signed focal length; R,R_1,R_2 are signed radii of curvature. Use metres in SI; any common length unit may be used consistently in a calculation.
- h_o,h_i are signed object/image heights. m is dimensionless.
- n=c/v_light is absolute refractive index; n_21=n_2/n_1 is the index of medium 2 relative to medium 1. Refractive indices are dimensionless. lambda_0 and lambda are vacuum and in-medium wavelengths, in metres; frequency is unchanged across a stationary interface.
- i,r are incidence/refraction angles measured from the normal; i_c is the critical angle; n_d,n_r mean denser/rarer optical media. Angles are dimensionless in radians (degrees may be used consistently in school problems).
- t,d are slab thickness and lateral displacement, both in metres. Apparent-depth and shift expressions are near-normal approximations.
- P_s is spherical-surface power in m^-1 (dioptre); R must be in metres for SI power.
- RO-002, RO-003, RO-015–RO-018 use the paraxial/small-aperture approximation.

SHARED SIGN-CONVENTION CALLOUT — include this concise text accurately
“NCERT Cartesian convention: measure from the pole/optical centre. Along incident light: positive; opposite: negative. Heights above the principal axis: positive; below: negative. Concave mirror: f,R<0; convex mirror: f,R>0. Apply signs to known values; do not guess the sign of an unknown.”

DIAGRAM
Include at most one small explanatory TIR ray diagram, and only if it can be physically correct. It must show light travelling in the denser medium toward a denser–rarer boundary, a clearly marked normal, an arrow on the incident ray, an arrow on the reflected ray staying in the denser medium, labels n_d>n_r and i>i_c, and no transmitted ray. If any of those details cannot be drawn clearly, omit the diagram. Do not use the unlabelled decorative convergence motif from the references.

STRICT CONTENT / NEGATIVE INSTRUCTIONS
The following are immutable scientific text, not creative suggestions: title, page number, topic order, every formula, subscript, superscript, sign, approximation, symbol definition, unit, condition and sign convention above. Do not invent, omit, derive, simplify, rearrange, duplicate or modify formulas. Do not add prism dispersion, separated-lens combinations, terrestrial/Galilean telescopes, human-eye optics, wave optics or any unsupported content. Do not change n_21 to n_12, u to v, a minus to a dash, or i_c to an unlabeled angle. Do not assign units to dimensionless n, m or M. No illegible/garbled text, tiny type, duplicated formula, misspelling, unsupported symbol, clipped heading/footer, overlapping panels, colliding labels, decorative clutter, excessive empty space, watermark, or crop at the page edge. Prioritize mathematical correctness over decoration. Return only one finished page image.

IMPORTANT HONESTY RULE
Image generation may still introduce character-level formula errors even when instructed not to. Do not present the result as verified merely because it looks polished. If exact formula integrity is not achieved, use the deterministic typesetting fallback described in the package quality checklist.
```

## Manifest mapping

Page 1 contains exactly `RO-001`–`RO-018`, in the topic sequence above. Source metadata, conditions and audit status are in `formula_manifest.json`.
