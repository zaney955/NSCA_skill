#!/usr/bin/env python3
"""Calculate target training loads and volume-load.

Usage:
  python calculate_training_load.py --one-rm 140 --percent 85 --sets 4 --reps 5 --unit kg
"""

from __future__ import annotations

import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--one-rm", type=float, required=True)
    parser.add_argument("--percent", type=float, required=True)
    parser.add_argument("--sets", type=int, default=1)
    parser.add_argument("--reps", type=int, default=1)
    parser.add_argument("--round-to", type=float, default=2.5)
    parser.add_argument("--unit", default="")
    args = parser.parse_args()

    if args.one_rm <= 0:
        raise SystemExit("--one-rm must be positive")
    if args.percent <= 0 or args.percent > 120:
        raise SystemExit("--percent must be in a reasonable range")
    if args.sets < 1 or args.reps < 1:
        raise SystemExit("--sets and --reps must be positive")
    if args.round_to <= 0:
        raise SystemExit("--round-to must be positive")

    raw_load = args.one_rm * args.percent / 100
    rounded_load = round(raw_load / args.round_to) * args.round_to
    volume_load = rounded_load * args.sets * args.reps

    result = {
        "input": {
            "one_rm": args.one_rm,
            "percent": args.percent,
            "sets": args.sets,
            "reps": args.reps,
            "unit": args.unit,
        },
        "raw_target_load": round(raw_load, 2),
        "rounded_target_load": round(rounded_load, 2),
        "volume_load": round(volume_load, 2),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
