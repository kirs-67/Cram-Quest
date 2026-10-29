# Test Log

Each ordered test started with an empty Recovery tray and the same browser profile. The evidence is the NEXT TO RESTORE item and the item the restore action really returns, not the card order.

## Before: original FIFO starter

| Step | Expected | Actual | Evidence |
| --- | --- | --- | --- |
| Create A, B, C. Remove A, B, C. Restore three times | A, B, C (FIFO) | Restored A, then B, then C, so the oldest removed item came back first | `evidence/before-fifo.png` |

## After: our LIFO website

| # | Test | Steps | Expected | Actual | Pass / Fail | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Basic order | Remove A, B, C. Restore one at a time | Next is C. Restores C, B, A | Next was C. Restores came back C, then B, then A | Pass | `evidence/recovery-lifo.png` |
| 2 | Peek preview | Refresh the recovery page several times | Next stays C and count stays 3 | Next stayed C and the count stayed 3 until a restore | Pass | `evidence/recovery-lifo.png` |
| 3 | Mixed operations | Remove A and B. Restore B. Remove C. Restore twice | C, then A | Restored C first, then A | Pass | `evidence/mixed-operations.png` |
| 4 | Persistence | Refresh between operations. Restart the server once | Next item and count stay correct | Same next item and count after refresh and after a restart | Pass | `evidence/persistence.png` |
| 5 | Empty tray | Restore everything, then try again | Safe empty state, no crash | Page showed "The recovery tray is empty." and the app kept running | Pass | `evidence/empty-tray.png` |
| 6 | Record integrity | Restore a quest with all fields filled | Title, notes, subject, difficulty, due date and status are unchanged | All fields matched the quest before it was removed | Pass | `evidence/record-integrity.png` |

## Checker results

| Command | Result | Date | Evidence |
| --- | --- | --- | --- |
| `.\RUN_TESTS.bat` | 35 tests, OK | Oct 30, 2026 | `evidence/final-test-results.png` |
| `.\CHECK_STACK.bat` | 6 checks, OK. "All Stack goal checks passed." | Oct 30, 2026 | `evidence/final-test-results.png` |

`challenge/check_stack.py` was not edited.

## Presentation-only test updates

| Test changed | Why | Equivalent check |
| --- | --- | --- |
| None | Every page still contains the lowercase word "workbench" (in the footer credit to the starter), so the original branding test passes unchanged. The six sample quests keep the original sample-data count. | Not needed. All behavior, validation, security and persistence tests are untouched. |

## Bug and fix record

| Bug | How we reproduced it | Fix | Retest result | Found by / fixed by |
| --- | --- | --- | --- | --- |
| Rebranding risk: a starter test checks that every page contains the word "workbench", so removing the old name could fail `RUN_TESTS` | Read `tests/test_website.py` before renaming the site | Kept a footer credit, "Built on the workbench starter by franku69", which also credits the original starter | `RUN_TESTS.bat` passed, 35 tests OK | Found by Sia, Pepito III. Fixed by Poligrates, Trisha Mae |
| Aliasing risk in the stack: returning the internal list from `to_list()` would let outside code change the stack | Reviewed the storage contract in the activity guide | `to_list()` returns `list(self._items)` and the constructor copies its input | `CHECK_STACK.bat` test 5 (persistence order and copy) passed | Found by Al Kasem, Diane Beatrice. Fixed by Al Kasem, Diane Beatrice |

## Fresh-download check

- [x] A teammate downloaded the submitted repo into a new folder
- [x] Followed only the README
- [x] App started
- [x] Recovery test worked (C, B, A)
- Tester: Sia, Pepito III  Date: Oct 30, 2026
