#!/usr/bin/env python3
"""Estimate 1RM from a submaximal set.

Usage:
  python estimate_1rm.py --load 100 --reps 5 --unit kg
"""

from __future__ import annotations

import argparse
import json


def epley(load: float, reps: int) -> float:
    return load * (1 + reps / 30)


def brzycki(load: float, reps: int) -> float:
    return load * 36 / (37 - reps)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--load", type=float, required=True)
    parser.add_argument("--reps", type=int, required=True)
    parser.add_argument("--unit", default="")
    args = parser.parse_args()

    if args.load <= 0:
        raise SystemExit("--load must be positive")
    if args.reps < 1 or args.reps >= 37:
        raise SystemExit("--reps must be between 1 and 36")

    if args.reps == 1:
        estimates = {"direct_1rm": args.load}
        average = args.load
    else:
        estimates = {
            "epley": epley(args.load, args.reps),
            "brzycki": brzycki(args.load, args.reps),
        }
        average = sum(estimates.values()) / len(estimates)

    result = {
        "input": {"load": args.load, "reps": args.reps, "unit": args.unit},
        "estimates": {k: round(v, 2) for k, v in estimates.items()},
        "average_estimated_1rm": round(average, 2),
        "caution": "Estimates are less reliable at higher repetition counts; prefer technically sound sets of 10 reps or fewer.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
