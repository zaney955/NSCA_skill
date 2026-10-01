---
name: nsca-conditioning
description: Use this skill to design NSCA-informed plyometric, speed, change-of-direction, agility, aerobic endurance, and metabolic conditioning programs for athletes. Trigger when the user asks for explosive power drills, plyometric progressions, sprint training, COD or agility training, aerobic zones, MAS/heart-rate/RPE conditioning, interval programming, or integrating conditioning with strength training.
---

# NSCA Conditioning

Use this skill to design conditioning and field-based training that supports sport performance. It covers plyometric, speed, change-of-direction, agility, aerobic endurance, and metabolic training.

## Scope

Use for:
- Plyometric session and block design
- Speed acceleration and maximal-velocity development
- Change-of-direction and agility development
- Aerobic endurance and metabolic conditioning plans
- Conditioning zone selection
- Integration of conditioning with resistance training
- Progressions, regressions, and monitoring

Do not use for:
- Medical rehabilitation or return-to-play clearance
- Training through pain or unresolved injury
- Heat illness, rhabdomyolysis, cardiac, respiratory, or metabolic medical management
- Exhaustive copyrighted drill libraries
- Replacing qualified in-person coaching for high-risk drills

## Required Intake

Gather or infer:
- Athlete age, training status, sport, position/event, and season
- Primary conditioning goal
- Current workload, practice schedule, and competition schedule
- Injury restrictions, pain, or medical limits
- Available space, surfaces, equipment, and staff
- Current testing data: sprint times, jump metrics, MAS, HR zones, RPE, endurance tests
- Session duration and weekly frequency

If pain, heat illness symptoms, exertional collapse, suspected rhabdomyolysis, chest pain, or acute injury is present, stop training prescription and recommend immediate qualified evaluation.

## Reference Loading

Read as needed:
- `references/plyometric_training.md` for plyometric mode, intensity, volume, and progression.
- `references/speed_training.md` for acceleration, maximal velocity, and sprint mechanics.
- `references/cod_agility_training.md` for COD versus agility and drill selection.
- `references/aerobic_endurance_training.md` for endurance program design.
- `references/metabolic_training_zones.md` for zone, HR, RPE, MAS, and interval logic.

## Templates

Use:
- `assets/templates/plyometric_session_template.md`
- `assets/templates/speed_session_template.md`
- `assets/templates/agility_session_template.md`
- `assets/templates/aerobic_program_template.md`
- `assets/templates/conditioning_block_template.md`

## Scripts

Use:
- `scripts/plyometric_volume_checker.py` for foot-contact volume summaries.
- `scripts/zone_calculator.py` for simple heart-rate reserve or max-HR zones.
- `scripts/conditioning_block_builder.py` for dated weekly block scaffolds.

## Core Workflow

1. Classify the request:
   - plyometric, speed, COD/agility, aerobic, metabolic, or integrated block.
2. Screen for safety:
   - injury restrictions, pain, surface, weather, training status, equipment, supervision.
3. Identify sport demand:
   - force direction, movement mode, energy-system demand, competition density.
4. Select target quality:
   - Choose one primary emphasis per session or block.
5. Choose methods:
   - Match drill type, intensity, volume, frequency, rest, and progression to the athlete.
6. Place within week:
   - Protect high-quality speed, power, and plyometric work from excessive fatigue.
7. Build the plan:
   - Include warm-up, main work, rest, coaching focus, and progression/regression rules.
8. Add monitoring:
   - Track performance quality, RPE, soreness, jump/sprint markers, or HR/RPE response.
9. State boundaries:
   - Flag assumptions, contraindications, weather/heat concerns, and referral criteria.

## Output Standards

For sessions include:
- Goal
- Athlete context
- Warm-up
- Main drills or intervals
- Sets, reps, distances, contacts, intensity, rest
- Coaching notes
- Progression/regression
- Safety and monitoring

For blocks include:
- Weekly frequency
- Phase goal
- Progression by week
- Integration with strength and sport practice
- Deload or adjustment rules

## Guardrails

- Quality speed and plyometric work belongs early in sessions and away from excessive fatigue.
- For novices and youth, prioritize landing mechanics, coordination, and low intensity.
- For heavier, deconditioned, or injured athletes, reduce impact and progress conservatively.
- Do not prescribe high-volume high-intensity conditioning when recovery data suggest excessive fatigue.
- Outdoor conditioning must consider heat, cold, surface, hydration access, and emergency planning.
