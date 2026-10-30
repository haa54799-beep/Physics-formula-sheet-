#!/usr/bin/env python3
"""Reproducible coverage, calculation, citation, and PDF text audit."""
from __future__ import annotations

import json
import math
import re
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent

# Independently recomputed formula checks; each answer must contain the stated rounded result.
NUMERIC_CHECKS = {
    11: (5.85 / 58.44 / 0.500, 0.200, "0.200"),
    12: (0.1 / 10.1, 0.00990, "0.00990"),
    38: (1.86 * 0.20, 0.372, "0.372"),
    39: (0.279 / (1.86 * 0.1), 1.50, "1.50"),
    40: ((1.0 / ((0.0246 * 0.100) / (0.0821 * 300))), 1.00e4, "1.00×10⁴"),
    51: (100 * 12 / (12 + 108), 10.0, "10.0%"),
    54: ((5 / 60.06) / 0.095, 0.877, "0.877"),
    60: (50 / 1.0e5, 5.0e-4, "5.0×10⁻⁴"),
    62: (0.512 * 0.50, 0.256, "0.256"),
    64: (1.23 / (0.05 * 0.0821 * 300), 1.00, "0.999"),
    66: (1 + 0.60 * (3 - 1), 2.20, "2.20"),
    72: (3 * 0.512 * 0.20, 0.307, "0.307"),
    83: (-(2 * 96500 * 1.10) / 1000, -212.3, "−212.3"),
    99: (96500.0, 9.65e4, "9.65×10⁴"),
    100: ((2.0 * 1800 / (2 * 96500)) * 63.5, 1.18, "1.18 g"),
    119: (1.25 / 200, 0.00625, "0.00625"),
    120: (1.5e-3 * 1000 / 0.01, 150.0, "150 S cm² mol⁻¹"),
    124: (0.34 - (-0.76), 1.10, "1.10 V"),
    130: (0.50 - (0.05916 / 2) * math.log10(100), 0.44084, "0.44084 V"),
    134: (0.005 * 0.8, 0.0040, "0.0040 S cm⁻¹"),
    138: ((1.08 / 108 * 96500) / 1.0, 965.0, "965 s"),
    159: (40 / 2, 20.0, "20 min"),
    160: (math.log(1 / 0.20) / 30, 0.0536, "0.0536 min⁻¹"),
    161: ((0.10 - 0.04) / 0.002, 30.0, "30 s"),
    176: (8.314 * math.log(2) / (1 / 300 - 1 / 310) / 1000, 53.6, "53.6 kJ"),
    188: (math.log(2) / 6.93e-3, 100.0, "100 min"),
    190: ((0.10 - 0.06) / 20, 0.0020, "0.0020 M min⁻¹"),
    198: (math.log(10) / 50, 0.0461, "0.0461 min⁻¹"),
    200: (0.80 / (2 * 0.02), 20.0, "20 min"),
    212: (math.log(10) / 0.0231, 99.7, "99.7 min"),
    216: (math.log(100) / math.log(2), 6.64, "6.64 half-lives"),
    229: (math.sqrt(3 * (3 + 2)), 3.87, "3.87 BM"),
    262: (math.sqrt(5 * (5 + 2)), 5.92, "5.92 BM"),
    312: (3 * 0.4, 1.2, "1.2Δ_o"),
    316: (math.sqrt(4 * (4 + 2)), 4.90, "4.90 BM"),
    343: (math.sqrt(4 * (4 + 2)), 4.90, "4.90 BM"),
}


def main() -> None:
    inventory = json.loads((HERE / "question_inventory.json").read_text(encoding="utf-8"))
    database = json.loads((HERE / "answer_database.json").read_text(encoding="utf-8"))
    assert len(inventory) == len(database) == 500
    assert [q["number"] for q in inventory] == list(range(1, 501))
    assert [q["number"] for q in database] == list(range(1, 501))
    by_num = {row["number"]: row for row in database}
    assert all(by_num[n]["answer"].strip() for n in range(1, 501))
    assert all(1 <= q["source_pdf_page"] <= 28 for q in inventory)
    assert all(q["source_pdf_page"] == by_num[q["number"]]["source_pdf_page"] for q in inventory)

    for number, (actual, expected, snippet) in NUMERIC_CHECKS.items():
        assert math.isclose(actual, expected, rel_tol=0.005, abs_tol=0.0005), (number, actual, expected)
        assert snippet in by_num[number]["answer"], (number, snippet, by_num[number]["answer"])

    pdf_path = HERE / "answer_companion.pdf"
    with pymupdf.open(pdf_path) as pdf:
        assert pdf.page_count >= 20
        companion_page_count = pdf.page_count
        texts = [page.get_text("text") for page in pdf]
        assert all(text.strip() for text in texts), "A PDF page has no extractable text"
        normalized = re.sub(r"\s+", " ", " ".join(texts))
        pattern = re.compile(r"Question\s+(\d+)\s+\[([MH])\]\s+·\s+Original PDF p\.\s+(\d+)")
        labels = [(int(m.group(1)), m.group(2), int(m.group(3))) for m in pattern.finditer(normalized)]
        assert len(labels) == 500, f"PDF contains {len(labels)} extractable question labels"
        assert [n for n, _, _ in labels] == list(range(1, 501))
        for n, tag, source_page in labels:
            row = by_num[n]
            assert tag == row["source_tag"] and source_page == row["source_pdf_page"], (n, tag, source_page)

    print("PASS: 500 source questions, 500 answers, sequential IDs, valid original-page citations.")
    print(f"PASS: {len(NUMERIC_CHECKS)} independently recomputed numerical/formula checks.")
    print(f"PASS: searchable companion PDF with {companion_page_count} pages and all 500 answer labels extractable.")


if __name__ == "__main__":
    main()
