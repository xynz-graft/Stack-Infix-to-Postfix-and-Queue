"""ITECC04 Laboratory 4, Part D: the circular queue and the deque."""


class CircularQueue:

    def __init__(self, capacity):
        """Step 1. A list of `capacity` Nones, a front index, and a count."""
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self._items = [None] * capacity
        self._front = 0
        self._count = 0

    def enqueue(self, item):
        """Step 2. Add at the rear. Raise OverflowError when full."""
        if self.is_full():
            raise OverflowError("queue is full")
        rear = (self._front + self._count) % len(self._items)
        self._items[rear] = item
        self._count += 1

    def dequeue(self):
        """Step 3. Remove and return the front item. IndexError when empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % len(self._items)
        self._count -= 1
        return item

    def peek(self):
        """Step 4. Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[self._front]

    def is_empty(self):
        """Step 5. True when the count is 0."""
        return self._count == 0

    def is_full(self):
        """Step 6. True when the count has reached the capacity."""
        return self._count == len(self._items)

    def size(self):
        """Step 7. Return the count."""
        return self._count

    def slots(self):
        """Written for you. Returns a copy of the raw list."""
        return list(self._items)


class Deque:
    """A queue you may add to and remove from at both ends."""

    def __init__(self):
        """Step 8. Create the empty list."""
        self._items = []

    def add_front(self, item):
        """Step 9. Insert at position 0."""
        self._items.insert(0, item)

    def add_rear(self, item):
        """Step 10. Append at the end."""
        self._items.append(item)

    def remove_front(self):
        """Step 11. Remove and return index 0. IndexError when empty."""
        if self.is_empty():
            raise IndexError("remove_front from empty deque")
        return self._items.pop(0)

    def remove_rear(self):
        """Step 12. Remove and return the last item. IndexError when empty."""
        if self.is_empty():
            raise IndexError("remove_rear from empty deque")
        return self._items.pop()

    def is_empty(self):
        """Step 13. True when there is nothing in the deque."""
        return len(self._items) == 0

    def size(self):
        """Step 14. Return how many items are held."""
        return len(self._items)


def is_palindrome(text):
    """Step 15. True when text reads the same both ways."""
    d = Deque()
    for ch in text:
        if ch.isalpha():
            d.add_rear(ch.lower())

    while d.size() > 1:
        if d.remove_front() != d.remove_rear():
            return False
    return True