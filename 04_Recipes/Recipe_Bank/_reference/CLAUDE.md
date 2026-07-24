# Recipe Bank Standardization

## What This Project Is

This folder contains a large historical recipe archive (400+ files) from West Ashley
Culinary, organized under an old, retired course-unit numbering scheme (0 - Orientation,
1 - Culinary Fundamentals, ... 20 - Nutritional Cooking). The job is to turn it into
one clean, standardized recipe bank in `./Recipe_Bank/`, following the format and
conventions already established in `./Recipe_Bank/_reference/` (see below).

## Setup

Before starting, confirm these exist:
- `./Recipe_Bank/_reference/` - contains the Standard Recipe Format spec and the five
  already-completed recipe files (Breakfast.md, Lunch.md, Desserts.md, Beverages.md,
  Condiments_and_Sauces.md). These are the style and detail-level reference - match
  them, don't reinvent the format.
- The rest of this folder tree - the raw archive to process (docx, pdf, doc, and a
  few html/image files).

If `./Recipe_Bank/_reference/` doesn't exist yet, stop and ask rather than guessing
at the format.

## Standard Recipe Format

Every recipe entry needs: Name; Course/use case; Source and revision date; Yield and
portion size; Equipment; Ingredients with units; Procedure; Food safety controls;
Allergens; Quality indicators; Holding/cooling/storage/reheating; Scaling notes; Skill
focus.

## Scaling

Target batch size is roughly 16-30 portions, matching the program's own established
convention (Charleston Chewies at 24, Flaky Puff Crust Pizza at 16, Creamy Multi-Cheese
Mac at ~30). Recipes sized for 1-8 servings should be scaled up into this range, with
the scaling factor stated in the entry. Single-serving items (individual drink builds,
etc.) stay per-serving, same as the existing Beverages.md entries.

## Deduplication Rule

- **Same dish, minor variance only** (butter vs. shortening, a slightly different
  chill time, etc.) -> condense into ONE entry, noting the variation in Source/revision
  notes.
- **Same name, genuinely different technique or result** (e.g. a smoked version vs.
  a base version of the same dish) -> keep as SEPARATE entries, clearly labeled, same
  as the two mac-and-cheese and two rice-krispie-treat entries already in the bank.
- **Different cuisine or flavor direction using a similar method** -> keep separate.
  Similar technique does not mean same dish.
- When genuinely unsure which bucket something falls into, don't guess - add it to
  `./Recipe_Bank/_OPEN_QUESTIONS.md` with a one-line description of the ambiguity and
  move on. Do not block progress on one unclear item.

## Organization

Recategorize everything into current, sensible categories - reuse Breakfast, Lunch,
Desserts, Beverages, Condiments and Sauces where things fit, and create new category
files as needed (Breads.md, Poultry.md, Seafood.md, Soups_and_Stocks.md,
Baking_and_Pastry.md, International.md, etc.). Do NOT preserve the old numbered unit
folders (`0 - Orientation`, `17 - Advanced Baking & Pastry`, etc.) in the output
structure - that numbering is retired and doesn't map to the current curriculum. It's
fine to note in an entry's Source line which old folder something came from, for
traceability.

## What Not To Do

- Don't treat "ProStart" branding on a source file as a reason to exclude or
  deprioritize a recipe. ProStart's retirement is about a credential pathway, not a
  judgment on any specific recipe's quality or usability. A good recipe is a good
  recipe regardless of what folder it came from.
- Don't fabricate a yield, allergen list, or ingredient quantity that isn't in the
  source material - flag it as missing/needs confirmation in the entry itself
  instead, the same way a few recipes in the existing bank are flagged for missing
  yield.
- Keep source attribution for anything adapted from an outside site or cookbook.
- Genericize branded ingredients (a specific sausage or flour brand) to the generic
  product, unless the brand IS the actual menu item name.
- Don't delete or modify the original source files - this is a read-and-standardize
  job, not a cleanup of the raw archive. Leave the source folders exactly as they are.

## Workflow

Work through one category at a time, not all 400+ files at once. For each category:

1. Find all source files that plausibly belong in that category (search across all
   the old numbered folders, not just the one whose name matches - a good chicken
   recipe might be sitting in "12 - Poultry" or "11 - Cooking Methods" or "19 -
   International Cuisine").
2. Read each candidate file.
3. Group duplicates/near-duplicates per the rule above.
4. Write the standardized entries into the matching `./Recipe_Bank/<Category>.md`
   file (append to the existing file if it's one of the five already started,
   otherwise create a new one following the same format).
5. Log anything genuinely ambiguous to `./Recipe_Bank/_OPEN_QUESTIONS.md`.
6. Before moving to the next category, give a short summary: how many source files
   went in, how many final entries came out, and why (e.g. "14 cookie files ->
   5 entries: 3 were true duplicates of Overnight Chocolate Chip Cookies, 6 were minor
   variants of the same sugar cookie condensed into one entry with variation notes,
   5 were genuinely distinct recipes kept separate").

Suggested category order: Breads, Poultry, Seafood, Soups and Stocks, Baking and
Pastry (largest - break into sub-passes: cookies, cakes, pies, other), International,
everything else.
