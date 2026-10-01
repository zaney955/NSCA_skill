---
name: nsca-nutrition-performance
description: Use this skill to provide conservative NSCA-informed sports nutrition education and planning frameworks for athlete performance, including macronutrient planning, pre-event, during-event, post-event fueling, hydration basics, supplement risk screening, and referral boundaries. Trigger when the user asks for performance nutrition plans, training-day fueling, competition nutrition, hydration strategy, protein/carbohydrate guidance, body-composition support within scope, or supplement caution checklists.
---

# NSCA Nutrition Performance

Use this skill for general sports nutrition education and planning frameworks that support performance. Keep advice conservative and within scope. This skill does not provide medical nutrition therapy, diagnose conditions, treat eating disorders, or determine supplement legality.

## Scope

Use for:
- Training-day and competition fueling frameworks
- Pre-event, during-event, and post-event nutrition structure
- General carbohydrate, protein, fat, hydration, and electrolyte planning
- Body-composition goal support within nonmedical boundaries
- Supplement risk screening questions
- Referral prompts to registered dietitians, physicians, or sport governing bodies

Do not use for:
- Eating disorder treatment or RED-S treatment
- Medical diets for disease
- Weight-cutting protocols
- Supplement prescriptions or safety guarantees
- Banned-substance clearance
- Advising minors on weight loss without qualified professional involvement
- Replacing a registered dietitian or physician

## Required Intake

Gather:
- Athlete age, sport, event duration, training phase, and schedule
- Goal: performance, recovery, body composition support, hydration, or competition fueling
- Training frequency and intensity
- Body mass if macro estimates are requested
- Dietary restrictions and preferences
- Medical conditions, GI issues, history of disordered eating, or RED-S risk
- Supplements under consideration
- Governing body if banned-substance risk is involved

If disordered eating, RED-S, rapid weight loss, medical disease, pregnancy, severe GI symptoms, or supplement legality questions are present, provide referral-oriented guidance instead of a prescriptive plan.

## Reference Loading

Read as needed:
- `references/nutrition_scope_boundaries.md` for safety and referral rules.
- `references/macronutrient_guidelines.md` for general macro planning.
- `references/pre_during_post_event_nutrition.md` for event fueling structure.
- `references/hydration_and_electrolytes.md` for hydration basics.
- `references/supplement_caution_framework.md` for supplement risk screening.

## Templates

Use:
- `assets/templates/performance_nutrition_brief_template.md`
- `assets/templates/event_nutrition_plan_template.md`
- `assets/templates/hydration_plan_template.md`
- `assets/templates/supplement_risk_checklist_template.md`

## Script

Use `scripts/macro_estimator.py` for broad gram-per-kilogram macro ranges. Treat outputs as starting estimates, not prescriptions.

## Core Workflow

1. Classify the request:
   - daily fueling, event fueling, recovery, hydration, body-composition support, or supplement screening.
2. Apply scope and risk screen:
   - Identify medical, eating disorder, RED-S, minor athlete, banned-substance, or rapid weight-loss concerns.
3. Gather sport context:
   - Training load, event duration, intensity, schedule, environment, and recovery window.
4. Select framework:
   - Macro range, event timing, hydration strategy, recovery routine, or supplement checklist.
5. Generate practical plan:
   - Use food-first, athlete-specific, preference-aware, and schedule-aware guidance.
6. Add monitoring:
   - Energy, performance, GI tolerance, hydration signs, recovery, body mass trends when appropriate.
7. State limitations:
   - Clarify when to consult a registered dietitian, physician, or governing-body compliance resource.

## Output Standards

For nutrition plans include:
- Goal and context
- Assumptions
- Fueling targets or ranges
- Timing structure
- Food examples when useful
- Hydration notes
- Monitoring and adjustment rules
- Referral or compliance flags

For supplement questions include:
- Evidence uncertainty
- Contamination and banned-substance risk
- Third-party testing questions
- Governing-body check reminder
- Medical professional referral when relevant

## Guardrails

- Prefer food-first strategies.
- Avoid extreme weight-loss or weight-cutting advice.
- Do not guarantee supplements are safe, effective, or permitted.
- Do not give fixed meal plans for medical conditions.
- For minors, body-composition change should involve guardians and qualified professionals.
- For RED-S, eating disorder signs, or persistent underfueling concern, refer to qualified medical and nutrition professionals.
