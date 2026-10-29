# Contributions

Roles show who led an area. Everyone can contribute to any area. Evidence is linked to files, test-log entries and screenshots in `docs/evidence/`. Commit count alone is not a measure of contribution.

## Contribution log

| Member / role | Completed task | Files changed | Evidence / reviewer |
| --- | --- | --- | --- |
| Albarece, Stefe Kira (Team lead and integration) | Set up the team repo from the starter, merged the feature branches, fixed a merge conflict in the templates, and confirmed that `.venv/`, `instance/` and the SQLite file are not uploaded | `.gitignore` check, `README.md` (team and roles section), merged pull requests | Merge record and pull request history. Reviewed by Sia, Pepito III |
| Al Kasem, Diane Beatrice (Backend / stack developer) | Implemented `HistoryBuffer` as a list-based stack (top = end of list) and traced the remove and restore routes to `push()`, `peek()` and `pop()` | `backend/stack.py`, `docs/STACK_EXPLANATION.md` | Operation trace in `STACK_EXPLANATION.md`, `CHECK_STACK` results in `evidence/final-test-results.png`. Reviewed by Albarece, Stefe Kira |
| Poligrates, Trisha Mae (Frontend / UI developer) | Built the Cram Quest theme, redesigned the Revive Tray page with the "NEXT TO RESTORE" slot, and made the quest board work on narrow screens | `frontend/static/cram-quest.css`, `frontend/templates/base.html`, `index.html`, `recovery.html` | `evidence/before-home.png`, `evidence/after-home.png`, `evidence/recovery-lifo.png`. Reviewed by Seato, Antonette Hian |
| Seato, Antonette Hian (Data and feature developer) | Added the eight subjects, Easy / Medium / Boss difficulty labels, the Boss Battle badge and the subject filter; checked that revived quests keep all their details | `backend/app.py`, `database/db.py`, `frontend/templates/macros.html`, `item_form.html` | Data-flow notes below and the record-integrity test in `TEST_LOG.md`. Reviewed by Poligrates, Trisha Mae |
| Sia, Pepito III (QA and documentation lead) | Wrote the test cases, reproduced the rebranding test risk, tested a fresh download following only the README, and wrote the README | `docs/TEST_LOG.md`, `docs/CONTRIBUTIONS.md`, `README.md` | `TEST_LOG.md` entries and the fresh-download checklist. Reviewed by Al Kasem, Diane Beatrice |

## Data-flow notes (Seato)

Subjects are stored in the existing `category` column, so no schema change or migration was needed. The subject filter is applied in `backend/app.py` after the items are loaded. Difficulty keeps the stored values `low`, `medium` and `high`, and only the labels shown to the user changed. The Boss Battle badge is calculated when the page renders and is never stored, so a revived quest always shows the right badge for its due date.

## Pair programming record

| Date | Driver | Navigator | What each person did |
| --- | --- | --- | --- |
| Oct 28, 2026 | Al Kasem, Diane Beatrice | Sia, Pepito III | Diane wrote `HistoryBuffer` in `backend/stack.py`. Pepito read each method against the activity guide and ran `CHECK_STACK.bat` with her. |
| Oct 29, 2026 | Poligrates, Trisha Mae | Seato, Antonette Hian | Trisha built the Revive Tray layout and theme. Antonette checked that the subject chips, difficulty labels and Boss Battle badge appeared in the right places. |
| Oct 30, 2026 | Albarece, Stefe Kira | Al Kasem, Diane Beatrice | Stefe merged the branches. Diane re-ran the stack checker on the merged code and traced a restore request through `app.py`. |

## Each member can explain

- Their own contribution
- FIFO versus LIFO
- Why C returns first, and why peek does not remove an item
- That the stack lives in `backend/stack.py`, and that the restore route in `backend/app.py` calls `pop()`
- The difference between frontend, backend and database

## Individual notes

### Albarece, Stefe Kira
I set up the team repository, reviewed pull requests, merged the branches and checked that only source files were uploaded (no `.venv/`, `instance/` or database file).

### Al Kasem, Diane Beatrice
I implemented the stack in `backend/stack.py`. The top is the end of the list, so `push` and `pop` are both O(1). I traced how the real restore route uses `pop()`.

### Poligrates, Trisha Mae
I designed the Cram Quest look in `cram-quest.css` and the Revive Tray page, and checked the layout at a narrow screen width.

### Seato, Antonette Hian
I added the subjects, difficulty labels, Boss Battle badge and subject filter, and checked that revived quests keep their title, notes, subject, difficulty, due date and status.

### Sia, Pepito III
I wrote the test cases and the README, kept the test log, and tested a fresh download using only the README steps.
