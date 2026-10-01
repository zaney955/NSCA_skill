---
name: nsca-program-design
description: Use this skill to design NSCA-informed resistance training programs, needs analyses, training blocks, microcycles, mesocycles, annual plans, and load progressions for athletes. Trigger when the user asks for strength training program design, resistance training variables, periodization, 1RM-based loading, offseason/preseason/in-season planning, or sport-specific strength and power programming.
---

# NSCA Program Design

Use this skill to turn athlete context into a practical strength and conditioning plan. The skill is for training design, not medical diagnosis, physical therapy, legal advice, or nutrition prescription.

## Scope

Use for:
- Sport and athlete needs analysis
- Resistance training session, microcycle, mesocycle, and annual plan design
- Training goal selection: strength, power, hypertrophy, muscular endurance, maintenance
- Exercise selection, order, frequency, load, repetitions, volume, and rest periods
- Periodization models and seasonal planning
- 1RM, estimated 1RM, relative load, and volume-load calculations

Do not use for:
- Return-to-play after injury without medical clearance
- Treating pain, diagnosing injury, or overriding contraindications
- Dietary, supplement, or banned-substance advice
- Copying textbook tables or protocols verbatim

## Required Intake

Gather or infer the minimum viable context:
- Athlete: age, sex if relevant, training age, training status, injury restrictions, available days
- Sport: sport, position/event, season, competition density
- Goal: primary training outcome for the block
- Constraints: equipment, time per session, concurrent sport practice, testing data
- Current strength data: 1RM, estimated 1RM, RM loads, RPE/RIR, or recent training loads

If key details are missing, make conservative assumptions and label them. Ask only when the missing detail changes safety or the core plan.

## Reference Loading

Read only the files needed:
- `references/training_principles.md` for global programming principles.
- `references/needs_analysis.md` for sport and athlete analysis.
- `references/resistance_training_variables.md` for frequency, order, load, volume, and rest.
- `references/loading_and_progression.md` for 1RM, RM, RPE, load increases, and volume-load logic.
- `references/periodization_models.md` for annual, macrocycle, mesocycle, and microcycle planning.
- `references/population_considerations.md` for youth, older adults, sex-related, or training-status adjustments.

## Templates

Use templates when producing structured deliverables:
- `assets/templates/needs_analysis_template.md`
- `assets/templates/resistance_program_template.md`
- `assets/templates/mesocycle_template.md`
- `assets/templates/microcycle_template.md`
- `assets/templates/annual_plan_template.md`

## Scripts

Use scripts for deterministic calculations:
- `scripts/estimate_1rm.py` estimates 1RM from load and reps.
- `scripts/calculate_training_load.py` calculates target loads and volume-load.
- `scripts/generate_periodization_calendar.py` creates a dated cycle scaffold.

Run scripts rather than recalculating large tables by hand when exact arithmetic matters.

## Core Workflow

1. Classify the request:
   - needs analysis, single session, microcycle, mesocycle, annual plan, loading calculation, or review.
2. Establish scope and safety:
   - Note injuries, medical restrictions, age-related limits, equipment, and current training status.
3. Analyze sport demands:
   - Movement patterns, primary force qualities, energy-system contribution, common injury risks, position/event demands.
4. Analyze athlete:
   - Training history, skill level, testing data, strengths, limitations, and current season.
5. Select the primary block goal:
   - Prefer one main emphasis per block. Maintain other qualities with smaller doses when needed.
6. Choose training variables:
   - Exercises, frequency, order, load/reps, volume, rest, progression, deload/recovery.
7. Build the plan:
   - Match detail to request. Include session tables for short plans and cycle logic for longer plans.
8. Explain decisions:
   - Briefly connect choices to sport demands, training status, and season.
9. Include monitoring:
   - Suggest simple readiness/performance checks and adjustment rules.
10. State assumptions and boundaries:
   - Be explicit about missing data, medical clearance, and when to involve qualified professionals.

## Output Standards

Keep outputs coach-usable:
- Start with the plan, then rationale.
- Use tables for programs.
- Include warm-up categories, main lifts, accessories, sets/reps/load, rest, and progression.
- Avoid overprecision when data are missing.
- Prefer conservative first-week loading for novice, in-season, or high-practice-load athletes.
- When load is prescribed from 1RM, provide both percentage and calculated load if data exist.

## Built-In Guardrails

- For youth athletes, prioritize technique, motor skill, progressive exposure, and supervision.
- For in-season athletes, reduce volume and protect performance quality.
- For advanced athletes, use more variation and individualized loading.
- For pain, acute injury, post-surgical status, or unresolved symptoms, stop program prescription and request medical clearance.
- For legal, medical, or nutrition questions, refer to the appropriate professional and keep advice educational.
