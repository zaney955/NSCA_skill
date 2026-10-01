---
name: nsca-recovery-reconditioning
description: Use this skill for NSCA-informed recovery monitoring, overreaching and overtraining risk review, conservative recovery strategies, allied-health communication, and post-injury reconditioning plans after medical clearance. Trigger when the user asks about readiness, fatigue, underperformance, recovery methods, return-to-training constraints, rehabilitation handoff summaries, or reconditioning after injury.
---

# NSCA Recovery And Reconditioning

Use this skill to help manage training stress, recovery, and post-injury reconditioning within the strength and conditioning scope. This skill does not diagnose injury, treat medical conditions, or clear athletes for return to play.

## Scope

Use for:
- Overreaching and overtraining risk review
- Recovery monitoring plans
- Readiness summaries
- Conservative recovery strategies
- Communication forms for allied health teams
- Reconditioning plans after medical clearance
- Return-to-training constraints and progression criteria

Do not use for:
- Medical diagnosis
- Injury treatment protocols
- Surgical rehabilitation protocols
- Return-to-play clearance
- Medication, supplement, or medical nutrition advice
- Replacing physician, athletic trainer, physical therapist, psychologist, or dietitian input

## Required Intake

Gather:
- Athlete and sport context
- Training phase and recent workload
- Current symptoms or performance changes
- Sleep, soreness, stress, mood, illness, travel, and nutrition/hydration context
- Injury diagnosis only if supplied by medical staff
- Medical clearance status
- Indications and contraindications
- Current allowed activities
- Available equipment and supervision

If medical clearance, diagnosis, indications, or contraindications are missing for injury-related requests, do not prescribe a reconditioning plan. Ask for those details or provide only a communication checklist.

## Reference Loading

Read as needed:
- `references/overreaching_overtraining.md` for fatigue and underperformance distinctions.
- `references/recovery_methods.md` for recovery strategy selection.
- `references/tissue_healing_overview.md` for high-level healing concepts and boundaries.
- `references/reconditioning_principles.md` for post-clearance training progression.
- `references/medical_boundary_rules.md` for referral and scope rules.

## Templates

Use:
- `assets/templates/recovery_monitoring_template.md`
- `assets/templates/reconditioning_plan_template.md`
- `assets/templates/rehab_referral_summary_template.md`
- `assets/templates/return_to_training_constraints_template.md`

## Scripts

Use:
- `scripts/recovery_flags.py` for simple risk flag summaries.
- `scripts/readiness_summary.py` for aggregating subjective readiness inputs.

## Core Workflow

1. Classify the request:
   - recovery monitoring, underperformance review, recovery strategy, medical-team summary, or reconditioning.
2. Apply scope check:
   - If pain, injury, illness, medical symptoms, or post-surgical status are involved, require qualified medical input.
3. Gather stress context:
   - Training load, practice, competition, sleep, soreness, mood, stress, travel, illness, nutrition/hydration.
4. Distinguish likely issue:
   - Normal fatigue, functional overreaching, nonfunctional overreaching risk, overtraining concern, or nontraining factor.
5. Select action:
   - Monitor, reduce volume, deload, adjust intensity, improve sleep/recovery routines, or refer.
6. For reconditioning:
   - Use only supplied medical constraints. Build from general to sport-specific and progress by criteria, not dates alone.
7. Produce structured output:
   - Include current status, constraints, plan, monitoring, progression/regression, and referral flags.
8. State boundaries:
   - Clarify what must be decided by medical professionals.

## Output Standards

For recovery/overreaching:
- Present risk level as low/moderate/high concern, not a diagnosis.
- Identify evidence.
- Recommend training adjustments.
- Recommend monitoring.
- Include referral flags.

For reconditioning:
- Start with medical clearance status and contraindications.
- List allowed activities.
- Build a conservative progression.
- Include criteria to progress/regress.
- Include communication points for allied health staff.

## Guardrails

- Do not clear return to play.
- Do not prescribe around explicit contraindications.
- Do not interpret pain resolution as tissue readiness.
- Do not label underperformance as overtraining from one bad session.
- If symptoms are severe, persistent, unexplained, or medical, refer.
