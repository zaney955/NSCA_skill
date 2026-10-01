#!/usr/bin/env python3
"""Summarize plyometric foot contacts.

Usage:
  python plyometric_volume_checker.py --drill "box jump:3x5" --drill "bounds:4x10"
"""

from __future__ import annotations

import argparse
import json


def parse_drill(value: str) -> dict:
    try:
        name, prescription = value.split(":", 1)
        sets_text, reps_text = prescription.lower().split("x", 1)
        sets = int(sets_text)
        reps = int(reps_text)
    except ValueError as exc:
        raise SystemExit(f"Invalid drill format: {value}") from exc
    if sets < 1 or reps < 1:
        raise SystemExit("Sets and reps must be positive")
    return {"name": name, "sets": sets, "reps": reps, "contacts": sets * reps}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--drill", action="append", required=True, help="name:setsxreps")
    args = parser.parse_args()

    drills = [parse_drill(value) for value in args.drill]
    total = sum(drill["contacts"] for drill in drills)
    print(json.dumps({"drills": drills, "total_contacts": total}, indent=2))


if __name__ == "__main__":
    main()
