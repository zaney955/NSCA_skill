#!/usr/bin/env python3
"""Summarize simple recovery risk flags.

Inputs are 1-5 ratings where 1 is poor/high concern and 5 is good/low concern,
except soreness where 1 is none/low and 5 is severe/high.

Usage:
  python recovery_flags.py --sleep 2 --fatigue 2 --mood 3 --soreness 4 --performance-drop
"""

from __future__ import annotations

import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sleep", type=int, required=True)
    parser.add_argument("--fatigue", type=int, required=True)
    parser.add_argument("--mood", type=int, required=True)
    parser.add_argument("--soreness", type=int, required=True)
    parser.add_argument("--performance-drop", action="store_true")
    args = parser.parse_args()

    values = [args.sleep, args.fatigue, args.mood, args.soreness]
    if any(value < 1 or value > 5 for value in values):
        raise SystemExit("All ratings must be 1-5")

    flags = []
    if args.sleep <= 2:
        flags.append("poor sleep")
    if args.fatigue <= 2:
        flags.append("high fatigue")
    if args.mood <= 2:
        flags.append("low mood/readiness")
    if args.soreness >= 4:
        flags.append("high soreness")
    if args.performance_drop:
        flags.append("reported performance drop")

    if len(flags) >= 4 or (args.performance_drop and len(flags) >= 2):
        concern = "high"
    elif len(flags) >= 2:
        concern = "moderate"
    else:
        concern = "low"

    result = {
        "concern": concern,
        "flags": flags,
        "note": "This is a training-support screen, not a diagnosis.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
