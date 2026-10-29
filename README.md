# Cram Quest: Revive Tray

A study-quest board where the last quest you drop is the first one you can bring back.

> Our website helps **students** manage **study quests** so they can **revive the last quest they dropped** during a stressful exam week.

Built for the Data Structures & Algorithms Website Remix + LIFO Stack Challenge.
Original starter: [franku69/Website-Stack-Data-Structure](https://github.com/franku69/Website-Stack-Data-Structure).

## Who it is for

College students juggling several subjects. When exams pile up, people delete tasks in a panic and regret the most recent one first. The Revive Tray fixes that: it always offers the quest you removed last.

## What a quest is

One study task (example: "Normalize a table to 3NF"). Each quest has a title, notes, a subject, a difficulty (shown as Easy, Medium, Boss), a due date, and a status.
Removing a quest sends it to the **Graveyard** (the recovery tray). Reviving it returns that same record with all details intact.

All sample data is fictional.

## Setup (Windows, Python 3.10+)

1. Download or clone this repo into a new folder.
2. Open the folder in VS Code (File > Open Folder) and open a PowerShell terminal.
3. Run `.\SETUP_WINDOWS.bat` and wait for SETUP COMPLETE.
4. Run `.\START_WEBSITE.bat`, then open http://127.0.0.1:5000
5. Port busy? Run `.\START_WEBSITE.bat --port 5001`.

## Run the tests

In a second terminal, one at a time:

```
.\RUN_TESTS.bat
.\CHECK_STACK.bat
```

## Try the LIFO demo

1. Create quests A, B, and C.
2. Remove them in order A, B, C using "Move to recovery tray".
3. Open the Revive Tray. The next quest is **C**.
4. Click "Restore next item" three times. You get C, then B, then A.

## Where the LIFO code lives

`backend/stack.py`, class `HistoryBuffer`. The routes in `backend/app.py` call `push()` when a quest is removed and `pop()` when one is revived. Full explanation: [docs/STACK_EXPLANATION.md](docs/STACK_EXPLANATION.md).

## What we changed

| Change | Why it helps the user | Files | Owner |
| --- | --- | --- | --- |
| New name, dungeon theme, pixel headings | Makes the board feel like a game, which is more fun to open | `frontend/static/cram-quest.css`, `base.html` | Frontend |
| Subjects (DSA, Discrete Structures, Stats, EnviSci, PathFit, Rizal, HCI, FDS) replace generic categories | Matches how students organize work | `backend/app.py`, `database/db.py`, `item_form.html` | Data |
| Difficulty labels (Easy / Medium / Boss) | Shows effort at a glance | `index.html`, `macros.html`, `cram-quest.css` | Data + Frontend |
| Boss Battle badge for quests due in 3 days | Surfaces urgent work | `index.html`, `backend/app.py` | Data |
| Subject filter | Focus on one subject at a time | `index.html`, `backend/app.py` | Data |
| XP bar (done vs total) | Visible progress | `index.html`, `cram-quest.css` | Frontend |
| Revive Tray page redesign | Makes the next quest obvious | `recovery.html`, `cram-quest.css` | Frontend |


## Team and roles

| Member | Role | Main contribution |
| --- | --- | --- |
| Albarece, Stefe Kira | Team lead and integration | Team repo, merged branches, checked that only source files were uploaded |
| Al Kasem, Diane Beatrice | Backend / stack developer | List-based `HistoryBuffer` in `backend/stack.py` and the restore-route trace |
| Poligrates, Trisha Mae | Frontend / UI developer | Cram Quest theme, Revive Tray layout, narrow-screen view |
| Seato, Antonette Hian | Data and feature developer | Subjects, difficulty labels, Boss Battle badge, subject filter |
| Sia, Pepito III | QA and documentation lead | Test cases, test log, README, fresh-download test |

Details and evidence are in [docs/CONTRIBUTIONS.md](docs/CONTRIBUTIONS.md).

## Known limitations

- Runs locally only. GitHub Pages cannot run the Flask backend.
- Only item recovery is a stack. Undoing every edit is not supported.
- Boss Battle badges and the subject filter are calculated when a page loads. They are not saved in the database.
- The theme loads fonts from Google Fonts, so plain fallback fonts appear when offline.

## Credits

Starter code by franku69 (instructor). Fonts: Pixelify Sans and Nunito from Google Fonts.
