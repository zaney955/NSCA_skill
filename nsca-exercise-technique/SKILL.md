---
name: nsca-exercise-technique
description: Use this skill to teach, audit, cue, regress, progress, and safely supervise NSCA-informed exercise technique for free weights, machines, warm-ups, mobility, flexibility, spotting, and common resistance training errors. Trigger when the user asks for exercise technique checklists, coaching cues, common errors, spotting guidance, safe setup, or warm-up and mobility technique.
---

# NSCA Exercise Technique

Use this skill to produce practical coaching guidance for safe and effective exercise execution. It supports instruction and supervision; it does not diagnose injuries or replace qualified in-person coaching.

## Scope

Use for:
- Exercise setup and execution checklists
- Coaching cues
- Common errors and likely corrections
- Spotting requirements
- Warm-up, mobility, and flexibility technique
- Regressions and progressions
- Machine setup and free weight safety

Do not use for:
- Diagnosing pain or injury
- Clearing athletes after injury
- Recommending loaded exercise against medical restrictions
- Spotting Olympic-style power exercises
- Creating exhaustive copyrighted exercise manuals

## Required Intake

Gather or infer:
- Exercise or movement pattern
- Athlete training status and skill level
- Goal of the exercise
- Equipment used
- Load/intensity context
- Observed error or concern
- Injury restrictions or pain reports
- Training environment and spotter availability

If the user reports pain, acute injury, neurological symptoms, or medical restrictions, stop technique prescription and recommend qualified evaluation.

## Reference Loading

Read as needed:
- `references/technique_fundamentals.md` for setup, grip, posture, ROM, speed, breathing, belts.
- `references/spotting_guidelines.md` for spotting rules.
- `references/resistance_exercise_checklists.md` for pattern-based exercise checklists.
- `references/mobility_flexibility_methods.md` for warm-up, mobility, and stretching.
- `references/common_errors_and_cues.md` for cue selection.

## Templates

Use:
- `assets/templates/exercise_teaching_template.md`
- `assets/templates/technique_audit_template.md`
- `assets/templates/spotting_plan_template.md`
- `assets/templates/warmup_mobility_session_template.md`

## Script

Use `scripts/cue_selector.py` to retrieve cue ideas by movement pattern or error.

## Core Workflow

1. Identify the exercise and objective.
2. Screen for safety:
   - pain, restrictions, load level, experience, environment, spotters.
3. Define setup:
   - stance, grip, alignment, machine settings, body contact points, bracing.
4. Define execution:
   - start, eccentric, transition, concentric, finish, breathing, tempo or velocity intent.
5. Identify errors:
   - observed faults, probable causes, and coaching corrections.
6. Add cues:
   - Use short external or task-oriented cues when possible.
7. Add regression/progression:
   - Modify load, ROM, complexity, speed, stability, or equipment.
8. Add spotting/safety:
   - State if spotters are needed and how they should communicate.
9. Bound the advice:
   - Note when in-person coaching or medical referral is required.

## Output Standards

For an exercise teaching request include:
- Purpose
- Setup
- Execution
- Breathing/bracing
- Common errors
- Coaching cues
- Regressions/progressions
- Spotting/safety

For a technique audit include:
- Observed issue
- Risk level
- Likely causes
- Corrections
- Next-session drill plan
- Stop/referral criteria

## Guardrails

- Do not spot power exercises. Teach the athlete how to miss safely in an appropriate environment.
- For overhead, over-face, bar-on-back, or front-racked heavy free weight exercises, address spotting or rack safety.
- For beginners, prioritize movement quality over load.
- For high-load structural exercises, discuss bracing and breathing carefully; do not encourage prolonged breath holding.
- If pain is present, distinguish technique coaching from medical evaluation and refer when needed.
