# Migration Report

## Purpose
Describe how WACOS Version 2.1 was reconstructed, what was used, what remains unresolved, and what should improve in Version 3.0.

## Migration Method
1. Preserved WACOS Version 2.0 unchanged.
2. Reviewed Version 2.0 for duplicate content, conflicts, organization, terminology, links, and missing documentation.
3. Removed operating-repo evidence clutter and export duplication.
4. Centralized unresolved decisions in [DECISION_REGISTER.md](DECISION_REGISTER.md).
5. Added [GLOSSARY.md](GLOSSARY.md), [QA_REVIEW.md](QA_REVIEW.md), and [RELEASE_REPORT_2_1.md](RELEASE_REPORT_2_1.md).
6. Regenerated the manual exports and ZIP package.

## Consistency Review
| Review Area | Result |
|---|---|
| Grading systems | Conflict found. Multiple compatible evidence types exist, but final weights require review. |
| Curriculum versions | Culinary 1 and Culinary 2 philosophy is stable; exact pacing varies across drafts. Newest 2026 direction preserved. |
| Duplicate recipes | Duplicate/conceptual recipe material likely exists. Master recipe deduplication deferred. |
| Duplicate SOPs | SOP concepts overlap across safety, closing, dish, Bistro, and fundamentals threads. Consolidated into systems; final SOP cards still needed. |
| Internal links | Core Markdown links were generated and checked by script. |
| Terminology | Standardized around West Ashley Culinary, Kitchen + Classroom, Bistro, Culinary 1, Culinary 2, Hospitality Work-Based Learning, Food Handler, CKC. |

## Assumptions Made
- The exported ChatGPT data is authoritative unless contradicted by newer source material.
- Version 1.0 is architecture only.
- Culinary 1 is one semester.
- Culinary 2 is full year.
- Thursday prep and Friday service is the stable Bistro rhythm for Culinary 2.
- Food Handler is a Culinary 1 credential target.
- CKC is the preferred Culinary 2 credential target based on newest pacing material.

## Missing Information
See [TODO.md](TODO.md).

## Recommended Version 3.0 Improvements
- Build exact lesson calendars from the school calendar.
- Create master recipe bank with allergen and yield data.
- Create printable Bistro role cards, station cards, and live grading sheets.
- Add formal CKC alignment.
- Add equipment-specific SOPs and safety sign-offs.
- Build a cleaned ChatGPT Edu upload bundle.
