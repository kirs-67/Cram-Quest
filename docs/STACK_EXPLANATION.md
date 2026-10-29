# Stack Explanation

## 1. Original FIFO behavior

The starter's `HistoryBuffer` used a dictionary and always returned the **oldest** removed record first. If we removed A, B, C, restoring gave A, B, C. That is First In, First Out (a queue).

## 2. Our representation

We use a Python `list` as a stack.

- **Top** = the last element of the list (`self._items[-1]`).
- **Bottom** = the first element.
- `push(item)` appends to the end. `pop()` removes from the end.

We chose a list because adding and removing at the end are both fast, and we never have to scan or sort the records to find the next one.

## 3. How each operation works

| Operation | What it does | Time |
| --- | --- | --- |
| `push(item)` | `append` the item at the top | O(1) amortized |
| `pop()` | Remove and return the top. Raises `IndexError` if empty | O(1) |
| `peek()` | Return the top without removing it. Raises `IndexError` if empty | O(1) |
| `is_empty()` | Check whether the list has no items | O(1) |
| `size()` | Return the length | O(1) |
| `to_list()` | Return a **new** copy, bottom to top | O(n) |

`to_list()` is O(n) because it copies every item. Saving to SQLite is a separate step that also costs O(n) for n stored IDs. That cost belongs to the database save, not to the in-memory stack.

## 4. Persistence order

If A, B, C were pushed, `to_list()` returns `[A, B, C]` (bottom to top). That is the order saved in the database. LIFO changes which item comes out next, not the saved order. When the server restarts, the list is loaded back with `HistoryBuffer(items)`, so C is still on top.

The constructor copies the incoming list (`list(items)`). Without the copy, changing the stack would also change the caller's list.

## 5. Real request trace

- Remove a quest: route in `backend/app.py` archives the record, then calls `push(id)`, then saves `to_list()`.
- Open the Revive Tray: route calls `peek()`. Nothing is removed, so the next item and count stay the same on refresh.
- Revive: route calls `pop()`, gets the ID, and returns the matching record to the board.

## 6. Why C returns first

C was pushed last, so it sits on top. `pop()` only touches the top, so C comes out before B, and B before A.

## 7. One bug we solved

Returning the stack's own list from `to_list()` would let other code change the stack by accident. For example, the route that saves history to SQLite could edit the same list the stack was using. We fixed it by returning a new list (`list(self._items)`) and by copying the input list in the constructor. `CHECK_STACK.bat` test 5 (persistence order and copy) confirms this.

## 8. Test evidence

Screenshots are in `docs/evidence/`: the A/B/C restore order (`recovery-lifo.png`), mixed operations, persistence after refresh and restart, the empty tray, record integrity, and the final results of `RUN_TESTS` (35 tests OK) and `CHECK_STACK` (6 checks OK). The full table is in `docs/TEST_LOG.md`.
