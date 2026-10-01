#!/usr/bin/env python3
"""Estimate broad performance nutrition macro ranges.

Usage:
  python macro_estimator.py --body-mass 80 --training-load high
"""

from __future__ import annotations

import argparse
import json


RANGES = {
    "low": {"carb": (3, 5), "protein": (1.4, 1.8), "fat": (0.8, 1.2)},
    "moderate": {"carb": (5, 7), "protein": (1.6, 2.0), "fat": (0.8, 1.2)},
    "high": {"carb": (6, 10), "protein": (1.6, 2.2), "fat": (0.8, 1.2)},
}


def scale_range(body_mass: float, values: tuple[float, float]) -> dict:
    low, high = values
    return {
        "g_per_kg": [low, high],
        "grams_per_day": [round(low * body_mass), round(high * body_mass)],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--body-mass", type=float, required=True)
    parser.add_argument("--training-load", choices=sorted(RANGES), required=True)
    args = parser.parse_args()

    if args.body_mass <= 0:
        raise SystemExit("--body-mass must be positive")

    selected = RANGES[args.training_load]
    result = {
        "body_mass": args.body_mass,
        "training_load": args.training_load,
        "carbohydrate": scale_range(args.body_mass, selected["carb"]),
        "protein": scale_range(args.body_mass, selected["protein"]),
        "fat": scale_range(args.body_mass, selected["fat"]),
        "caution": "Broad education ranges only; adjust with athlete response and qualified nutrition support.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
