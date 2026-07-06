# QA Review

## Scope
Comprehensive quality assurance review of WACOS Version 2.0 before release of Version 2.1.

## Findings And Corrections
| Area | Finding | Correction In 2.1 |
|---|---|---|
| Duplicate content | Complete manual and export files were stored inside the operating repo and separately in outputs. | Removed generated exports from the operating repo; exports now live in `WACOS_v2_1_Exports`. |
| Evidence clutter | Large topic evidence packets were stored inside the operating repo. | Moved raw evidence and topic packets to the research archive only. |
| Source manifest length | High-signal conversation index made the manifest too long for daily use. | Simplified manifest and kept detailed reports in the archive. |
| Conflict repetition | Grade weights, Bistro launch timing, credentials, and naming conflicts appeared in multiple docs. | Centralized unresolved issues in [DECISION_REGISTER.md](DECISION_REGISTER.md). |
| Terminology | Culinary 2 was described with several overlapping labels. | Standardized to "full-year depth and operations course" and "fundamentals under pressure." |
| Missing control docs | No glossary or formal decision register existed. | Added [GLOSSARY.md](GLOSSARY.md) and [DECISION_REGISTER.md](DECISION_REGISTER.md). |
| Broken links | Version 2.0 link check passed, but new docs needed validation. | Regenerated link check for 2.1. |
| Organization | Operating manual and archive functions were blurred. | 2.1 separates operating repo, archive, and exports. |

## Remaining Risks
- Gradebook policy still needs instructor confirmation.
- Exact Culinary 1 and Culinary 2 calendars still require calendar alignment.
- Recipe and SOP deduplication require artifact-level review.
- Equipment, emergency, budget, and vendor details are not yet complete.
