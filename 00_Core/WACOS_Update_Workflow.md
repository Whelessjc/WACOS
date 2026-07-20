# WACOS Return and Update Workflow

Last updated: July 20, 2026

## Purpose

Use this page whenever returning to WACOS after time away or whenever an idea needs to be added, changed, or removed. It is the short operating workflow for moving from an idea to an accurate GitHub update without repeating a full repository review.

## The 60-Second Refresher

1. Start a Codex task in the local `WACOS` workspace.
2. Say which lane the request belongs to: **Quick Edit**, **Program Decision**, or **Resource Intake**.
3. State the desired result in plain language. Attach only the sources needed for that change.
4. Say whether Codex may publish after validation or must pause for approval.
5. Codex updates the affected documents, checks consistency, records the change, and reports the Git commit.

The instructor decides program direction. Codex handles file placement, cross-document consistency, decision records, changelog entries, validation, and GitHub publishing.

## Choose the Smallest Workflow That Fits

### Lane 1: Quick Edit

Use for a typo, clarification, small lesson adjustment, recipe vehicle, renamed item, or change that does not alter program policy.

Copy and use:

> Quick update: ADD / CHANGE / REMOVE [exact idea] in [course, unit, Bistro area, or document]. The intended result is [one sentence]. Publish after validation.

Codex should:

- Inspect only the affected document and its direct governing references.
- Make the smallest complete change.
- Run targeted checks rather than a full resource audit.
- Update the changelog only when the change is meaningful enough to need a future record.
- Commit and push immediately when “Publish after validation” is included.

### Lane 2: Program Decision

Use when the idea changes grading, credentials, course scope, required foundations, Bistro structure, safety boundaries, team names, calendars, or another rule that several documents must follow.

Copy and use:

> Program decision: CHANGE [current practice] TO [new practice]. This applies to [courses/years/teams]. First show me the one-paragraph decision summary and affected-document list. After I say “approved,” update everything and publish.

Codex should:

1. Check the Core Manual, Decision Register, current course maps, and directly affected operating documents.
2. Present one concise decision statement and the expected file scope.
3. Wait for one instructor approval.
4. Apply the decision everywhere it governs without asking for repeated approval.
5. Update the Decision Register, source/traceability records when relevant, and changelog.
6. Validate, commit, and push.

### Lane 3: Resource Intake

Use when importing several documents, AI-generated materials, photographs, ZIP files, prior-year resources, or a new curriculum package.

Bundle related sources together and provide one intake note containing:

- What the materials are.
- Which course, semester, unit, or operation they belong to.
- Which source is newest or most authoritative.
- What you believe should change.
- Whether the originals are evidence only or should become current WACOS content.

Copy and use:

> Resource intake: Review these files for [topic]. Identify what is new, redundant, conflicting, or out of place. Use [named file] as the newest authority. Give me one recommendation summary. After I approve it, integrate the approved items and publish.

Codex should use two passes:

1. **Review pass:** return only the net-new content, conflicts, duplicates, recommended placement, and decisions needed.
2. **Integration pass:** after one approval, update the repository, exclude unnecessary delivery files, validate, commit, and push.

Do not mix unrelated resource groups in one intake. A single topic folder or upload set is faster and easier to verify than many loosely related files.

## Add, Change, and Remove Rules

### Add

State what the idea is, where it belongs, and whether it is required or optional. Codex should add it to the narrowest appropriate location and then update governing summaries only when necessary.

### Change

State the old practice and the replacement. Avoid wording such as “update this” without naming the desired result. Codex should search for the old practice in current documents and replace only the places where it is acting as current guidance.

### Remove

State whether the item is:

- **Retired:** no longer current but worth preserving historically.
- **Replaced:** superseded by a named new practice.
- **Deleted:** incorrect, duplicated, or inappropriate to retain.

The default is to remove retired material from current guidance and preserve necessary history in the Decision Register or `99_Archive/`. Permanent deletion should be explicit.

Copy and use:

> Remove [item] from current WACOS guidance. Treat it as RETIRED / REPLACED BY [new item] / DELETE. Search current documents for dependent references, update the decision trail, and publish after validation.

## Approval Shortcuts

Use one of these phrases to control stopping points:

- **“Publish after validation.”** Codex may edit, validate, commit, and push without another approval request.
- **“Show me the recommendation first.”** Codex reviews and pauses before editing.
- **“Update locally but do not publish.”** Codex edits and validates but leaves the work uncommitted or unpushed.
- **“Approved—finish and publish.”** Codex completes all already-described work without reopening settled decisions.

## What Codex Must Check Before Publishing

For every published update:

- The request is reflected in the correct current document.
- Directly affected course maps, unit plans, SOPs, or assessment documents agree.
- Policy changes are recorded in the Decision Register.
- Meaningful changes are recorded in the changelog.
- No temporary files, source ZIPs, photographs, generated delivery copies, credentials, or unrelated changes are included.
- Internal links and formatting checks pass.
- The local branch and GitHub are synchronized after the push.

A full-repository policy scan is reserved for Program Decisions and Resource Intake. Quick Edits receive targeted validation unless the change reveals a broader conflict.

## What the Completion Message Should Contain

Every published update should end with:

- What changed.
- Where it changed.
- Any remaining instructor or implementation task.
- Branch and commit ID.
- Confirmation that GitHub is synchronized.

## Returning After Time Away

Open a Codex task in the WACOS workspace and paste:

> WACOS return check: sync with GitHub, read the Update Workflow, Decision Register, TODO, and latest changelog entry, then give me a short status summary with current decisions, unfinished work, and the best next action. Do not change anything yet.

The four documents to open manually when needed are:

1. `00_Core/WACOS_Update_Workflow.md` — how to make changes.
2. `00_Core/DECISION_REGISTER.md` — what has been decided and what remains open.
3. `00_Core/TODO.md` — unfinished implementation work.
4. `CHANGELOG.md` — what changed most recently.

## Default Recommendation

For most new ideas, use **Quick Edit** and include **“Publish after validation.”** Use Program Decision only when the idea changes a governing rule. Use Resource Intake only when outside files must be reconciled. This keeps ordinary updates small, fast, and easy to reverse.
