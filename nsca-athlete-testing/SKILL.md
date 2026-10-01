---
name: nsca-athlete-testing
description: Use this skill to design NSCA-informed athlete test batteries, testing session plans, test order, administration standards, scoring, interpretation, monitoring protocols, and athlete profiles. Trigger when the user asks for strength, power, speed, agility, aerobic, anaerobic, mobility, balance, body composition, or team performance testing.
---

# NSCA Athlete Testing

Use this skill to select, organize, administer, score, and interpret athlete performance tests. The goal is to produce defensible testing plans and useful athlete profiles.

## Scope

Use for:
- Test battery selection
- Testing order and session logistics
- Test administration standards
- Basic scoring and interpretation
- Athlete profiling and team comparison
- Monitoring plans across a season
- Relative strength, T-score, z-score, and ranking calculations

Do not use for:
- Medical diagnosis or injury prediction claims
- Clinical screening beyond the strength and conditioning scope
- Treating movement deficits as medical conditions
- Claiming a test is valid without context
- Copying proprietary or textbook protocols verbatim

## Required Intake

Collect or infer:
- Testing purpose: talent ID, baseline, progress, readiness, return-to-training support, or monitoring
- Sport, position/event, age group, training status
- Tests under consideration
- Equipment and staff
- Time available
- Surface and facility constraints
- Injury restrictions and contraindications
- Previous scores, body mass, and comparison group if interpreting data

## Reference Loading

Read as needed:
- `references/test_selection_principles.md` for validity, reliability, and test choice.
- `references/test_categories.md` for what each test category measures.
- `references/test_administration_standards.md` for logistics and standardization.
- `references/scoring_and_interpretation.md` for score handling and athlete profiles.
- `references/monitoring_protocols.md` for recurring athlete monitoring.

## Templates

Use:
- `assets/templates/test_battery_template.md`
- `assets/templates/testing_session_plan_template.md`
- `assets/templates/athlete_profile_template.md`
- `assets/templates/test_report_template.md`

## Scripts

Use:
- `scripts/standardize_scores.py` for z-scores and T-scores.
- `scripts/rank_team_results.py` for ranked team outputs.
- `scripts/calculate_relative_strength.py` for strength relative to body mass.

## Core Workflow

1. Define the testing question:
   - What decision will the test inform?
2. Identify athlete and sport demands:
   - Match tests to key physical qualities and constraints.
3. Check test quality:
   - Prefer tests with reasonable validity, reliability, practicality, and safety for the setting.
4. Build the battery:
   - Include only tests that change decisions.
5. Order the tests:
   - Low-fatigue and technical measures first; fatiguing tests later.
6. Standardize administration:
   - Warm-up, instructions, trials, rest, equipment, surface, timing, and scoring.
7. Score and interpret:
   - Use absolute scores, relative scores, change over time, and comparison group when available.
8. Generate action:
   - Convert results into training priorities and monitoring recommendations.
9. State limits:
   - Explain uncertainty, missing norms, measurement error, and medical boundaries.

## Output Standards

For a testing plan include:
- Purpose
- Athlete group
- Test battery
- Order and rationale
- Equipment/personnel
- Standardization notes
- Scoring method
- Interpretation plan
- Safety/contraindication notes

For interpretation include:
- Raw scores
- Relative or standardized scores when appropriate
- Strengths and limitations
- Training implications
- Retest timing
- Measurement caveats

## Guardrails

- Do not present movement screens as definitive injury predictors.
- Do not compare athletes to norms unless the population is relevant.
- Avoid high-skill or maximal tests when technique is not competent.
- Use electronic timing when available for speed and agility.
- If pain, neurological symptoms, acute injury, or medical red flags appear, stop testing and refer.
