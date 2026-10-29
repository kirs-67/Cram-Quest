"""BACKEND / STACK: backend/stack.py.

Cram Quest keeps removed quest IDs in a real LIFO stack. The recovery tray
(Revive Tray) calls this class directly, so this file controls the real website.

Representation: a Python list. The TOP of the stack is the LAST element
(self._items[-1]); the BOTTOM is the first element.

Storage contract (unchanged from the starter): to_list() returns values from
oldest/bottom to newest/top. If A, B, C were pushed, to_list() is [A, B, C]
and C is still the next item to come out. The database saves that list and
passes it back to the constructor on the next request.

Time complexity:
    push, pop, peek, is_empty, size -> O(1) (push is amortized O(1))
    to_list                         -> O(n), it copies the list
Saving the list to SQLite is a separate O(n) step done by the database layer.
"""


class HistoryBuffer:
    """LIFO stack of removed item IDs (the Revive Tray)."""

    def __init__(self, items=None):
        # Copy the caller's values so we never share their mutable list.
        # Input is bottom-to-top order, so the last value becomes the top.
        self._items = list(items) if items is not None else []

    def push(self, item):
        """Record one removed item's ID at the top."""
        self._items.append(item)

    def pop(self):
        """Remove and return the newest (top) ID."""
        if self.is_empty():
            raise IndexError("The recovery tray is empty.")
        return self._items.pop()

    def peek(self):
        """Read the top ID without removing it."""
        if self.is_empty():
            raise IndexError("The recovery tray is empty.")
        return self._items[-1]

    def is_empty(self):
        """True when there are no recovery records."""
        return len(self._items) == 0

    def size(self):
        """Number of recovery records."""
        return len(self._items)

    def to_list(self):
        """Return a NEW list in bottom-to-top order, ready to save in SQLite."""
        return list(self._items)


# Optional alias so the class can also be imported as Stack.
Stack = HistoryBuffer
