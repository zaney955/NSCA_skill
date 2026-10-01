#!/usr/bin/env python3
"""Generate a simple mesocycle calendar scaffold.

Usage:
  python generate_periodization_calendar.py --start 2026-06-01 --weeks 12 --mesocycle-length 4
"""

from __future__ import annotations

import argparse
import datetime as dt
import json


def parse_date(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", required=True, help="YYYY-MM-DD")
    parser.add_argument("--weeks", type=int, required=True)
    parser.add_argument("--mesocycle-length", type=int, default=4)
    args = parser.parse_args()

    if args.weeks < 1:
        raise SystemExit("--weeks must be positive")
    if args.mesocycle_length < 1:
        raise SystemExit("--mesocycle-length must be positive")

    start = parse_date(args.start)
    weeks = []
    for index in range(args.weeks):
        week_start = start + dt.timedelta(days=index * 7)
        week_end = week_start + dt.timedelta(days=6)
        weeks.append(
            {
                "week": index + 1,
                "mesocycle": index // args.mesocycle_length + 1,
                "start": week_start.isoformat(),
                "end": week_end.isoformat(),
                "emphasis": "",
                "notes": "",
            }
        )

    print(json.dumps({"weeks": weeks}, indent=2))


if __name__ == "__main__":
    main()
