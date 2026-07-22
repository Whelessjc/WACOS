# Changelog

## 2026-07-22 - Add Instructor Workflow Documentation

### Decision

Created `09_Workflows/` as the instructor-only operating layer for weekly classroom practice, Bistro preparation and service, AI-supported work, repository maintenance, and external district systems. This layer documents current practice without creating curriculum or policy.

### Added

- Added the Teacher Cockpit operating model and source hierarchy.
- Added the Monday-Friday and weekend teacher workflow.
- Added concise daily, weekly, quarterly, and semester instructor checklists.
- Confirmed one documented deep clean per quarter.
- Added a dated ChatGPT EDU capability matrix that distinguishes available capabilities, blocked district connectors, and external systems.

### Governance and Navigation

- Added the instructor-supplied weekly agenda, checklist, and morning procedures to the Source Manifest as current-practice evidence without importing the raw Word files.
- Recorded the approved workflow-layer decision in the Decision Register.
- Added `09_Workflows/` to the root repository map.
- Preserved existing Core Manual, Bistro, assessment, safety, district, and cash-handling authority through links instead of duplicated policy.

## 2026-07-20 - Adopt 2026-2027 Academic Calendar Mapping

### Decision

Adopted the CCSD 2026-2027 Academic Calendar as the date authority for the current school year. Week 4 begins Bistro systems, mock service, and optional tightly controlled soft-opening work. Because Friday, September 4 is early release, the first normal public Bistro service is Friday, September 11 in Week 5, subject to readiness and safety.

### Calendar Integration

- Added `00_Core/2026-07-20_Calendar_Week_Mapping.md` with the approved week-numbering method, shortened-week adjustments, Semester 2 anchors, and May 17-27 post-guide buffer.
- Mapped Culinary 2 Weeks 19, 22, 29, 32, 33, 34, 35, and 36 to real dates.
- Corrected the Semester 2 assumption that Week 36 was the final student week; it is May 10-14, followed by two additional calendar blocks before the May 27 last student day.
- Set Week 33, April 19-23, as the preferred Explore Charleston tasting-menu execution window and Week 34 as an emergency compressed fallback.
- Embedded known closures, early releases, and shortened-week adjustments into the affected Culinary 1 and Culinary 2 daily plans.

### Consistency Corrections

- Replaced remaining current-facing `Kitchen + Classroom` references with `Classroom to Table`.
- Replaced FOH/BOH as a current Bistro team structure with Dining, Kitchen, Support, and Barista while retaining FOH/BOH as industry vocabulary only.
- Updated the Core Manual, Decision Register, source manifest, traceability, curriculum indexes, Bistro guidance, and administration references without overwriting newer WACOS content.

## 2026-07-20 - Add WACOS Return and Update Workflow

### Summary

Added a single refresher document for returning after time away and moving ideas into WACOS efficiently.

### Added or Updated

- Added `00_Core/WACOS_Update_Workflow.md` with Quick Edit, Program Decision, and Resource Intake lanes.
- Added copy-ready prompts for adding, changing, removing, approving, and publishing work.
- Defined when targeted validation is sufficient and when a full policy review is required.
- Added a return-status prompt and a four-document refresher list.
- Linked the workflow prominently from the root and Core README files.

## 2026-07-20 - Reconcile Claude Resource Intake

### Summary

Reviewed the supplied Claude-generated Markdown and Word resources, incorporated current source material, removed duplicate/superseded claims, and synchronized WACOS with the instructor decisions recorded July 19, 2026.

### Current Decisions Applied

- Grading: 20% Employability, 35% Labs, 45% Summative & Bistro.
- Credentials: ServSafe Food Handler for Culinary 1 and CKC for Culinary 2; ServSafe Manager retired from Culinary 2.
- Bistro launch: Week 4 target for 2026-2027, with instructor readiness/safety authority.
- Uniforms: Culinary 1 white jacket with logo; Culinary 2 black jacket with name and logo.
- Guest recovery: HEARD method.
- Bistro teams: Dining, Kitchen, Support, and Barista.

### Added or Updated

- Added three Culinary 1 foundational vehicles: dried pasta with basic tomato sauce, basic vinaigrette with simple salad, and basic pan sauce.
- Added whole-chicken breakdown to Culinary 2 Proteins, Heat, and Doneness, subject to supervision, sourcing, budget, and calendar confirmation.
- Reviewed the photographed cookbook overview against both course foundations; added cookware sizing/care and substitution judgment to Culinary 1 Unit 03.
- Confirmed and incorporated the four photo-review recommendations: tofu as the Culinary 1 plant-protein vehicle, same-day refrigerated quick pickling in Culinary 1 Flavor Systems, explicit poaching in Culinary 2 Proteins/Heat/Doneness, and gated broiler/grill fundamentals across Culinary 1 and 2.
- Added firm safety boundaries: no canning or fermentation in the quick-pickle application, and no student broiler/grill operation without the equipment-specific SOP, safety readiness, instruction/demo, supervision, and individual authorization.
- Recorded the instructor's final approval of the tofu, poaching, quick-pickle, and broiler/grill recommendations; remaining items are implementation-document tasks rather than open curriculum decisions.
- Culinary 2 Semester 1 corrections and Semester 2 Weekly Guide.
- Culinary 1 Units 4-5 service lesson updates and basic-tasks coverage map.
- Bistro Life of an Order, service standards, and team SOPs.
- WBL Readiness Bridge and Standard Recipe Format.
- Intake report and instructor decision note.

### Held Out

- Generated DOCX planning/delivery copies remain excluded from GitHub.
- Recipe-project instructions were not imported because the referenced archive and completed bank files were not supplied.
- POS/payment and master recipe-bank completion remain open rather than being inferred.

## 2026-07-06 - Add Curriculum Index and Culinary 2 Package Shell

### Summary

Added a curriculum index and organized Culinary 2 into a course package structure that can be expanded to match the classroom-ready depth of the imported Culinary 1 curriculum.

### Added

- `01_Curriculum/Curriculum_Index.md` as the current map for Culinary 1, Culinary 2, and Hospitality Work-Based Learning.
- `01_Curriculum/Culinary_2/Culinary-2-Curriculum/` as the Culinary 2 build-out package.
- Culinary 2 course map, unit overview folders, and a unit packet template.

### Updated

- `01_Curriculum/README.md` now points to the curriculum index and clarifies that GitHub is the curriculum home of record.
- `01_Curriculum/Culinary_2/README.md` now points to the organized Culinary 2 package and corrected assessment and recipe document locations.

### Confirmation

This change did not rewrite Culinary 2 policy. It organized the existing Culinary 2 framework into a teaching-package structure and identified where fuller daily lesson materials should be built next.

## 2026-07-06 - Add Culinary 1 Curriculum Markdown

### Summary

Imported the Desktop `Culinary-1-Curriculum` Markdown materials into the organized WACOS repository under `01_Curriculum/Culinary_1/Culinary-1-Curriculum/`.

### Included

- Canonical Culinary 1 curriculum Markdown source tree.
- Top-level Culinary 1 Markdown notes.
- Final-delivery Markdown materials under `FINAL-DELIVERY-Markdown/`.

### Excluded From GitHub

- ZIP packages.
- DOCX exports.
- PDF exports.
- PPTX slide decks.

These generated/binary delivery files remain local and are excluded by `.gitignore` unless intentionally published later as release assets.

### Confirmation

This import copied existing curriculum materials into the WACOS structure. It did not intentionally rewrite program policy.

## 2026-07-06 - Repository Structure Refactor

### Summary

Reorganized the WACOS workspace into a clean documentation structure centered on the Core Manual and current operating documents.

No document meaning was intentionally changed. Files were moved or copied for organization only.

### Major Folders Created

- `00_Core/`
- `01_Curriculum/`
- `01_Curriculum/Culinary_1/`
- `01_Curriculum/Culinary_2/`
- `01_Curriculum/Hospitality_WBL/`
- `02_Bistro/`
- `02_Bistro/Operations/`
- `02_Bistro/Menus/`
- `02_Bistro/Production/`
- `02_Bistro/Station_Guides/`
- `02_Bistro/SOPs/`
- `03_Assessment/`
- `04_Recipes/`
- `05_AI/`
- `06_Templates/`
- `07_Administration/`
- `08_Equipment_and_Safety/`
- `99_Archive/`

### Files Moved or Copied

- Governing documents moved into `00_Core/`.
- Current WACOS v2.1 curriculum documents moved into `01_Curriculum/`.
- Current WACOS v2.1 Bistro documents moved into `02_Bistro/`.
- Current WACOS v2.1 assessment documents moved into `03_Assessment/`.
- Current WACOS v2.1 recipe and production documents moved into `04_Recipes/`.
- Current WACOS v2.1 AI documents moved into `05_AI/`.
- Current WACOS v2.1 template documents moved into `06_Templates/`.
- Current WACOS v2.1 administration documents moved into `07_Administration/`.
- Current WACOS v2.1 equipment and safety documents moved into `08_Equipment_and_Safety/`.
- External Culinary 2 curriculum materials were copied from OneDrive into functional WACOS folders.
- Raw research archive and historical control reports moved into `99_Archive/`.

### Unresolved Classification Issues

- The OneDrive `Culinary-1-Curriculum` folder appeared empty during this refactor.
- `Hospitality_WBL/` was created but no current WBL source files were found.
- Exact current Bistro POS, payment, reservation, and cash-handling documents were not found.
- Equipment-specific SOPs, shutoff maps, and emergency maps still need instructor confirmation.
- External Culinary 2 Google Docs upload DOCX exports and build scripts were archived as generated/support material.
- `Network - Shortcut.lnk` from the external Culinary 2 folder was not copied into WACOS.

### Confirmation

This refactor reorganized files and added navigation documents. It did not intentionally rewrite program policy or change document meaning.
