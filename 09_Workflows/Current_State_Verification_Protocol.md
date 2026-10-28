# Current-State Verification and Change Capture Protocol
**Status:** WACOS operating workflow | **Adopted:** October 28, 2026 | **Scope:** Culinary 1, Culinary 2, Bistro, current-year implementation

## Why this exists
Pacing guides, prior DTGs, generated recipes, and archived discussions describe intentions at different points in time. They are not proof of what happened or what remains planned. Instructor-confirmed changes must override older plans without requiring the instructor to repeat them.

## Authoritative operational pointer
**Read first:** [Current Instructional State](../01_Curriculum/Current_Instructional_State_2026-27.md). Then read current dated decisions, governing SOPs, approved recipes and DTG standards as appropriate. The Core Manual still governs program policy and identity; this live state record governs *which lesson is current, what was completed, what was replaced, and what remains pending*. A recipe file does not establish that it was taught. A draft DTG does not establish that it is the current lesson.

## Mandatory preflight before answering "today", "next", "already done", or proposing a week
1. Read the live current-state file from the repository's default branch, not a cached Library copy.
2. Resolve course, cohort, date and instructional week. Check the most recent instructor-confirmed entry and the status of the candidate lesson.
3. Compare the completed-work register before recommending recipes. Never present a completed dish as a new lesson unless deliberately proposing a repeat with a different target.
4. If the state file conflicts with a newer instructor statement in the current conversation, the instructor statement wins immediately. Record the change before using older materials again.
5. If a required fact is absent, say it is unconfirmed. Do not promote an old proposal to "today's actual lesson." Ask only the missing question.
6. Distinguish **current cohort** from **future-year redesign**. Never treat a next-year plan as this year's adopted schedule.
7. Cite the active recipe version and use its actual quantities. If the current recipe is unclear, do not invent it.

## Capture workflow: say it once, record it once
When the instructor confirms a material change (pivot, cancellation, recipe substitution, completion, postponement, revised Bistro special, approved assessment change):
- Update the current-state file in the same working session when GitHub write access is available. Do not wait for a weekly catch-up.
- Record: date, course/cohort, previous plan, new plan, status (proposed / confirmed / completed / postponed / canceled), reason, recipe reference, next action, source (instructor confirmation), and any safety/approval dependencies.
- Change the older active entry to **superseded**, with a link or pointer to the new entry. Preserve history; do not erase it.
- Confirm the commit succeeded; only then say "WACOS updated." If a write fails, explicitly state it is not saved and provide the pending entry.
- If the decision changes enduring policy, also update the governing WACOS document through the established update workflow. Do not confuse a one-day pivot with a permanent curriculum redesign.

## Verification and maintenance
- At the end of a lab reflection, mark what actually happened, including incomplete work and observed gaps. A planned dish is not "completed" until confirmed.
- At the beginning of weekly planning, reconcile the live state with the pacing guide, events, recipe approvals and the completed-work register.
- Archive concluded terms separately; keep the live file short and visible.
- Keep student names, injury details, grades and other sensitive student records out of this repository. Record only de-identified instructional implications.
- GitHub updates are deliberate tool actions; ordinary chat memory alone does not automatically sync to WACOS. This protocol instructs the assistant to perform and verify the update whenever possible.

## Failure prevention test
A question such as "What is Culinary 1 doing Tuesday October 27?" must return the instructor-confirmed **beef and cheese sliders**, not the older dredged chicken or stir-fry proposals. A question about Culinary 2 November 9 must check completed dishes before recommending perloo, red rice or Hoppin' John.