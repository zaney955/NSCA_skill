#!/usr/bin/env python3
"""Calculate relative strength.

Usage:
  python calculate_relative_strength.py --load 140 --body-mass 80 --unit kg
"""

from __future__ import annotations

import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--load", type=float, required=True)
    parser.add_argument("--body-mass", type=float, required=True)
    parser.add_argument("--unit", default="")
    args = parser.parse_args()

    if args.load <= 0 or args.body_mass <= 0:
        raise SystemExit("--load and --body-mass must be positive")

    ratio = args.load / args.body_mass
    print(
        json.dumps(
            {
                "load": args.load,
                "body_mass": args.body_mass,
                "unit": args.unit,
                "relative_strength_ratio": round(ratio, 3),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
