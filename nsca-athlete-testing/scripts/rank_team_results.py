#!/usr/bin/env python3
"""Rank team results from a CSV file.

CSV columns required: athlete,score

Usage:
  python rank_team_results.py results.csv --lower-is-better
"""

from __future__ import annotations

import argparse
import csv
import json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    parser.add_argument("--lower-is-better", action="store_true")
    args = parser.parse_args()

    rows = []
    with open(args.csv_file, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rows.append({"athlete": row["athlete"], "score": float(row["score"])})

    rows.sort(key=lambda row: row["score"], reverse=not args.lower_is_better)
    for index, row in enumerate(rows, start=1):
        row["rank"] = index

    print(json.dumps({"results": rows}, indent=2))


if __name__ == "__main__":
    main()
