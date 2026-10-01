#!/usr/bin/env python3
"""Calculate simple HRmax or HRR zones.

Usage:
  python zone_calculator.py --hrmax 190 --hrrest 55 --method hrr
"""

from __future__ import annotations

import argparse
import json


ZONE_RANGES = {
    "z1": (0.50, 0.60),
    "z2": (0.60, 0.70),
    "z3": (0.70, 0.80),
    "z4": (0.80, 0.90),
    "z5": (0.90, 1.00),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hrmax", type=float, required=True)
    parser.add_argument("--hrrest", type=float, default=0)
    parser.add_argument("--method", choices=["max", "hrr"], default="hrr")
    args = parser.parse_args()

    if args.hrmax <= 0:
        raise SystemExit("--hrmax must be positive")
    if args.method == "hrr" and args.hrrest <= 0:
        raise SystemExit("--hrrest is required for HRR")
    if args.hrrest >= args.hrmax:
        raise SystemExit("--hrrest must be less than --hrmax")

    zones = {}
    for zone, (low, high) in ZONE_RANGES.items():
        if args.method == "hrr":
            reserve = args.hrmax - args.hrrest
            low_hr = args.hrrest + low * reserve
            high_hr = args.hrrest + high * reserve
        else:
            low_hr = low * args.hrmax
            high_hr = high * args.hrmax
        zones[zone] = {"low": round(low_hr), "high": round(high_hr)}

    print(json.dumps({"method": args.method, "zones": zones}, indent=2))


if __name__ == "__main__":
    main()
