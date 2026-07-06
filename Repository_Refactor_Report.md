# Repository Refactor Report

Date: 2026-07-06

## 1. Summary of Work Completed

Reorganized the WACOS workspace into a clean documentation structure for the West Ashley High School Culinary Arts Program.

The refactor created the requested folder system, moved governing documents into `00_Core/`, distributed current WACOS v2.1 documents into functional folders, copied external Culinary 2 curriculum materials from OneDrive into current working locations, and moved historical/raw source materials into `99_Archive/`.

No document meaning was intentionally changed.

## 2. Final Folder Structure

```text
WACOS/
|-- README.md
|-- CHANGELOG.md
|-- Repository_Refactor_Report.md
|-- 00_Core/
|-- 01_Curriculum/
|   |-- Culinary_1/
|   |-- Culinary_2/
|   |-- Hospitality_WBL/
|-- 02_Bistro/
|   |-- Operations/
|   |-- Menus/
|   |-- Production/
|   |-- Station_Guides/
|   |-- SOPs/
|-- 03_Assessment/
|-- 04_Recipes/
|-- 05_AI/
|-- 06_Templates/
|-- 07_Administration/
|-- 08_Equipment_and_Safety/
|-- 99_Archive/
```

Each major folder now includes a `README.md` explaining what belongs there, what does not belong there, how the folder relates to the Core Manual, and any special cautions.

## 3. Files Moved and Where They Were Moved

### Root Governing Documents to `00_Core/`

| File | New Location |
|---|---|
| `West_Ashley_Culinary_Core_Manual.md` | `00_Core/West_Ashley_Culinary_Core_Manual.md` |
| `Core_Manual_Traceability.md` | `00_Core/Core_Manual_Traceability.md` |
| `WACOS_Alignment_Checklist.md` | `00_Core/WACOS_Alignment_Checklist.md` |
| `WACOS_Playbook.md` | `00_Core/WACOS_Playbook.md` |
| `WACOS_Style_Guide.md` | `00_Core/WACOS_Style_Guide.md` |
| `WACOS_AI_Reference.md` | `00_Core/WACOS_AI_Reference.md` |
| `WACOS_Custom_Instructions_Draft.md` | `00_Core/WACOS_Custom_Instructions_Draft.md` |
| `WACOS_Companion_Docs_Completion_Report.md` | `00_Core/WACOS_Companion_Docs_Completion_Report.md` |

### Current WACOS v2.1 Documents

| Source File | New Location |
|---|---|
| `01_Program_Philosophy.md` | `00_Core/01_Program_Philosophy.md` |
| `02_Program_Standards.md` | `00_Core/02_Program_Standards.md` |
| `08_Daily_and_Weekly_Systems.md` | `00_Core/08_Daily_and_Weekly_Systems.md` |
| `GLOSSARY.md` | `00_Core/GLOSSARY.md` |
| `SOURCE_MANIFEST.md` | `00_Core/SOURCE_MANIFEST.md` |
| `DECISION_REGISTER.md` | `00_Core/DECISION_REGISTER.md` |
| `TODO.md` | `00_Core/TODO.md` |
| `03_Culinary_1_Curriculum.md` | `01_Curriculum/Culinary_1/03_Culinary_1_Curriculum.md` |
| `04_Culinary_2_Curriculum.md` | `01_Curriculum/Culinary_2/04_Culinary_2_Curriculum.md` |
| `05_Bistro_Operations.md` | `02_Bistro/Operations/05_Bistro_Operations.md` |
| `07_Leadership_and_Student_Roles.md` | `02_Bistro/Station_Guides/07_Leadership_and_Student_Roles.md` |
| `06_Assessment_System.md` | `03_Assessment/06_Assessment_System.md` |
| `09_Recipes_and_Production.md` | `04_Recipes/09_Recipes_and_Production.md` |
| `11_AI_Workflows.md` | `05_AI/11_AI_Workflows.md` |
| `12_Prompt_Library.md` | `05_AI/12_Prompt_Library.md` |
| `13_Templates_Checklists.md` | `06_Templates/13_Templates_Checklists.md` |
| `14_Program_Administration.md` | `07_Administration/14_Program_Administration.md` |
| `15_Teacher_Assistant_Onboarding.md` | `07_Administration/15_Teacher_Assistant_Onboarding.md` |
| `16_Future_Development.md` | `07_Administration/16_Future_Development.md` |
| `10_Equipment_Facility_Safety.md` | `08_Equipment_and_Safety/10_Equipment_Facility_Safety.md` |

### External Culinary 2 Curriculum Copies

The external `Culinary-2-Curriculum` folder was outside the WACOS workspace, so files were copied rather than removed from OneDrive.

| Source Material | WACOS Location |
|---|---|
| Core Culinary 2 curriculum `.md` files | `01_Curriculum/Culinary_2/` |
| Culinary Arts Management 2 Curriculum Binder `.docx` | `01_Curriculum/Culinary_2/` |
| Weekly agendas and yearly notes | `01_Curriculum/Culinary_2/` |
| Line check cards and assessment/rubric file | `03_Assessment/` |
| Assessment snapshots | `03_Assessment/Culinary_2_Assessment_Snapshots/` |
| Recipe use guidance and recipe bank README | `04_Recipes/` |
| Bistro menu README materials | `02_Bistro/Menus/` |
| Google Docs upload DOCX exports | `99_Archive/Culinary_2_Google_Docs_Upload_DOCX/` |
| External source copy | `99_Archive/External_Culinary_2_Curriculum_Source_Copy/` |
| Build scripts | `99_Archive/External_Culinary_2_Build_Scripts/` |

## 4. Files Renamed

No current policy documents were renamed for meaning.

Some copied external files were renamed only when moved into functional folders to clarify course/source context:

- `06_Line_Check_Cards.md` copied as `03_Assessment/Culinary_2_Line_Check_Cards.md`.
- `07_Assessment_and_Rubrics.md` copied as `03_Assessment/Culinary_2_Assessment_and_Rubrics.md`.
- `08_Recipe_Use_Guidelines.md` copied as `04_Recipes/Culinary_2_Recipe_Use_Guidelines.md`.

The v2.1 changelog was archived as `99_Archive/WACOS_v2_1_Control_Reports/CHANGELOG_v2_1.md` to avoid conflict with the new root `CHANGELOG.md`.

## 5. Files Placed in Archive and Why

| Archive Location | Reason |
|---|---|
| `99_Archive/WestAshleyCulinary_Research_Archive_v2_1/` | Raw source evidence, baseline history, reports, and source packets; historical/contextual |
| `99_Archive/WACOS_v2_1_Control_Reports/` | v2.1 release, migration, QA, link-check, index, and summary reports; useful history but not daily operating docs |
| `99_Archive/External_Culinary_2_Curriculum_Source_Copy/` | Full copied external source bundle preserved for traceability |
| `99_Archive/Culinary_2_Google_Docs_Upload_DOCX/` | Generated export copies for upload/use elsewhere; not primary working Markdown |
| `99_Archive/External_Culinary_2_Build_Scripts/` | Build scripts that support generated artifacts; not current instructional documents |

## 6. Duplicates or Conflicts Found

- The raw research archive contains baseline v1 documents and many source packets that overlap with current WACOS documents. These were kept in `99_Archive/`.
- The external Culinary 2 folder contained Markdown working files and generated DOCX upload copies. Markdown working files were copied into current folders; generated DOCX exports were archived.
- Older ProStart-centered language exists in the archive and older source materials. It was not placed into current policy folders as current direction.
- Older grading structures exist in historical material. Current folders should use 30% Employability, 30% Labs, and 40% Summative when grade weights are included.
- The preserved WACOS v2.1 `DECISION_REGISTER.md` and `03_Assessment/06_Assessment_System.md` still contain older language treating grade weights as unresolved. The Core Manual now governs; the decision register received a refactor note, and the assessment document should be updated in a future content-maintenance pass.

## 7. Unclear Files Needing Instructor Review

- `Culinary-1-Curriculum` in OneDrive appeared empty during this refactor.
- `01_Curriculum/Hospitality_WBL/` has no current source files yet.
- Current Bistro POS, payment, reservation, customer, and cash-handling documents were not found.
- Current facility maps, emergency maps, shutoff locations, and equipment-specific SOPs were not found.
- Master recipe bank authority remains unresolved.
- The external `Network - Shortcut.lnk` file was skipped and not copied into WACOS.
- `03_Assessment/06_Assessment_System.md` needs instructor review to update its pre-Core Manual grade-weight note without changing assessment philosophy.

## 8. Recommended Next Steps

1. Add current Culinary 1 source files if they exist outside the empty OneDrive folder.
2. Create or import Hospitality Work-Based Learning documents.
3. Build a Bistro Operations Playbook with current POS/payment/customer flow rules after instructor/admin confirmation.
4. Build the equipment and safety SOP index, including missing shutoff maps and emergency procedures.
5. Review `04_Recipes/` and identify the authoritative master recipe bank.
6. Update internal links in moved documents if they will be used as clickable navigation documents.
7. Use `00_Core/WACOS_Alignment_Checklist.md` before approving new documents as current.

## 9. Follow-Up Import: Culinary 1 Desktop Curriculum

Date: 2026-07-06

After the initial refactor, a separate `Culinary-1-Curriculum` folder was identified on the Desktop. Its Markdown source materials were copied into:

`01_Curriculum/Culinary_1/Culinary-1-Curriculum/`

Included:

- Canonical Culinary 1 curriculum Markdown source tree.
- Top-level Culinary 1 Markdown notes.
- Final-delivery Markdown materials in `FINAL-DELIVERY-Markdown/`.

Excluded from GitHub:

- ZIP files.
- DOCX files.
- PDF files.
- PPTX files.

These generated delivery/export files remain local and are excluded by `.gitignore`.
