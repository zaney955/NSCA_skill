#!/usr/bin/env python3
"""Standardize test scores from a CSV file.

CSV columns required: athlete,score
Optional: lower_is_better can be passed as a flag.

Usage:
  python standardize_scores.py results.csv --lower-is-better
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    parser.add_argument("--lower-is-better", action="store_true")
    args = parser.parse_args()

    rows = []
    with open(args.csv_file, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rows.append({"athlete": row["athlete"], "score": float(row["score"])})

    if len(rows) < 2:
        raise SystemExit("Need at least two rows to standardize scores")

    scores = [row["score"] for row in rows]
    mean = statistics.mean(scores)
    sd = statistics.stdev(scores)
    if sd == 0:
        raise SystemExit("Standard deviation is zero; cannot standardize")

    output = []
    for row in rows:
        z = (row["score"] - mean) / sd
        if args.lower_is_better:
            z = -z
        output.append(
            {
                "athlete": row["athlete"],
                "score": row["score"],
                "z_score": round(z, 3),
                "t_score": round(50 + 10 * z, 1),
            }
        )

    output.sort(key=lambda item: item["t_score"], reverse=True)
    print(json.dumps({"mean": mean, "sd": sd, "results": output}, indent=2))


if __name__ == "__main__":
    main()
