#!/usr/bin/env python3
"""Return cue ideas for a movement pattern or error.

Usage:
  python cue_selector.py --query "squat knee valgus"
"""

from __future__ import annotations

import argparse
import json


CUES = {
    "squat knee valgus": [
        "Push the floor apart.",
        "Track knees over toes.",
        "Keep the whole foot heavy.",
    ],
    "squat heels rise": [
        "Keep the whole foot heavy.",
        "Sit between your feet.",
        "Slow down and own the bottom position.",
    ],
    "hinge bar drift": [
        "Keep the bar close.",
        "Pull the bar into you.",
        "Push the hips back while the bar stays near the legs.",
    ],
    "hinge rounding": [
        "Brace before you move.",
        "Move from the hips.",
        "Reset your spine, then start the rep.",
    ],
    "press wrist": [
        "Stack knuckles over forearm.",
        "Punch straight.",
        "Squeeze the handle evenly.",
    ],
    "pull shrug": [
        "Put shoulders in your back pockets.",
        "Pull elbows, not shoulders.",
        "Pause before you pull.",
    ],
    "lunge knee valgus": [
        "Knee follows shoelaces.",
        "Keep pressure through the big toe, little toe, and heel.",
        "Move slowly enough to control the knee.",
    ],
    "power early arm pull": [
        "Legs first.",
        "Arms are ropes.",
        "Finish the drive before the pull.",
    ],
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    args = parser.parse_args()

    query = args.query.lower()
    query_tokens = set(query.split())
    matches = {
        key: cues
        for key, cues in CUES.items()
        if query_tokens.issubset(set(key.split())) or set(key.split()).issubset(query_tokens)
    }
    print(json.dumps({"query": args.query, "matches": matches}, indent=2))


if __name__ == "__main__":
    main()
