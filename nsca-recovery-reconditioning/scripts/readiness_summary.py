#!/usr/bin/env python3
"""Aggregate simple readiness ratings.

Inputs are 1-5 where 1 is poor and 5 is excellent.

Usage:
  python readiness_summary.py --sleep 4 --energy 3 --mood 4 --stress 2
"""

from __future__ import annotations

import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sleep", type=int, required=True)
    parser.add_argument("--energy", type=int, required=True)
    parser.add_argument("--mood", type=int, required=True)
    parser.add_argument("--stress", type=int, required=True, help="1 high stress, 5 low stress")
    args = parser.parse_args()

    ratings = {
        "sleep": args.sleep,
        "energy": args.energy,
        "mood": args.mood,
        "stress": args.stress,
    }
    if any(value < 1 or value > 5 for value in ratings.values()):
        raise SystemExit("All ratings must be 1-5")

    score = sum(ratings.values()) / len(ratings)
    if score >= 4:
        recommendation = "normal plan likely appropriate if performance and symptoms are normal"
    elif score >= 3:
        recommendation = "consider reducing accessory volume or using autoregulated loading"
    else:
        recommendation = "consider reducing training stress and checking for referral flags"

    print(
        json.dumps(
            {
                "ratings": ratings,
                "readiness_score": round(score, 2),
                "recommendation": recommendation,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
