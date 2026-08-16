# Finished-Artifact Publishing Workflow

## Purpose

Use this workflow to turn current WACOS source material into a durable, instructor-reviewed artifact that can be opened directly in Google Drive next semester or school year. GitHub governs the system; Google Drive makes accepted materials usable.

## Material States

| State | Location | Meaning |
|---|---|---|
| Source of truth | WACOS on GitHub | Governing decisions, curriculum architecture, SOPs, source records, and revision history. |
| Working draft | ChatGPT, an approved authoring tool, or a temporary workspace | Unreviewed planning, drafting, alternatives, and generated files. |
| Published artifact | District-approved Google Drive | Instructor-reviewed material accepted for direct teaching or operational use. |

## Lifecycle

1. Identify the classroom or operating need and the governing WACOS source.
2. Create or revise the artifact in ChatGPT or another approved authoring tool.
3. Keep the artifact in draft status until instructor review is complete.
4. Review content, safety, student-facing language, formatting, links, print rendering, accessibility, and classroom fit as applicable.
5. Publish the accepted DOCX, PDF, XLSX, PPTX, or Google-native copy to its durable Drive destination.
6. Add or update one concise entry in the [Published Artifact Index](Published_Artifact_Index.md).
7. Reuse the accepted Drive artifact directly. Do not regenerate it merely because a new term or school year begins.
8. Revise or retire it when needed. Preserve prior-year copies only when they remain useful.
9. If artifact work changes a governing rule, use the [WACOS Update Workflow](../00_Core/WACOS_Update_Workflow.md) before treating the change as current practice.

## Drive Organization

```text
West Ashley Culinary/
|-- 00 Start Here/
|-- Culinary 1/
|   `-- [school year]/Week NN/
|-- Culinary 2/
|   `-- [school year]/Week NN/
|-- Bistro/
|   |-- Current Service Materials/
|   |-- Forms and Checklists/
|   `-- Menus and Production/
|-- Shared Resources/
|   |-- Assessments and Blank Rubrics/
|   |-- Recipes/
|   `-- Instructor Tools/
|-- Program Administration/
|   `-- Reusable Blank Materials/
`-- Prior Years/[school year]/
```

Course/week folders are the primary daily entry point. Keep one canonical copy of a shared resource and use Drive shortcuts where several weeks or areas need it.

## Artifact Naming

Use **Course or Operation -> Week or Unit -> Plain-language artifact name**. Examples: `Culinary 1 - Week 1 Teaching Guide`, `Culinary 2 - Week 1 Recipes`, and `Bistro - Week 5 Prep List`. These human-facing names do not require stable GitHub source filenames to be renamed unless a source name is actively misleading.

## Indexing Rule

Index accepted packets, bundles, reusable forms, slide decks, spreadsheets, recipes, and other materials whose durable location or review state would otherwise be unclear. Do not create a separate row for every minor component when a packet-level entry is sufficient. Routine printing, sharing, shortcut creation, and formatting-only edits do not require a Git commit.

## Boundaries

- Do not add generated delivery binaries or Google exports to GitHub unless a specific preservation or release reason is documented.
- A published artifact does not independently establish policy.
- Google permissions, ownership, sharing, native revision history, and file retention remain external-system responsibilities.
- Keep student records, completed assessments, grades, credentials, restricted financial records, personnel information, and district-restricted data in their approved protected systems, not in WACOS or the general usable-materials library.
