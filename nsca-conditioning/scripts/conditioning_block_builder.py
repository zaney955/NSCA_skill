#!/usr/bin/env python3
"""Create a simple conditioning block scaffold.

Usage:
  python conditioning_block_builder.py --start 2026-06-01 --weeks 4 --sessions-per-week 2
"""

from __future__ import annotations

import argparse
import datetime as dt
import json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", required=True)
    parser.add_argument("--weeks", type=int, required=True)
    parser.add_argument("--sessions-per-week", type=int, required=True)
    args = parser.parse_args()

    if args.weeks < 1 or args.sessions_per_week < 1:
        raise SystemExit("weeks and sessions-per-week must be positive")

    start = dt.date.fromisoformat(args.start)
    weeks = []
    for week in range(1, args.weeks + 1):
        week_start = start + dt.timedelta(days=(week - 1) * 7)
        sessions = [
            {
                "session": session,
                "focus": "",
                "volume": "",
                "intensity": "",
                "notes": "",
            }
            for session in range(1, args.sessions_per_week + 1)
        ]
        weeks.append({"week": week, "start": week_start.isoformat(), "sessions": sessions})

    print(json.dumps({"weeks": weeks}, indent=2))


if __name__ == "__main__":
    main()
