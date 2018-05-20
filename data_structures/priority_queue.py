import operator


class PriorityQueue(list):
    """A simple priority queue implementation."""

    def __init__(self, seq, cmp):
        """Initialize the PriorityQueue.

        :param seq: the initial sequence used to construct the PQ.
        :type seq: Iterable[Any]
        :param cmp: function used to determine priority.
        :type cmp: function
        """
        super().__init__(seq)
        self.cmp = cmp
        for i in range((len(self) // 2) - 1, -1, -1):
            self.bubble_down(i)

    def extract(self):
        """Get the highest-priority element in the queue.

        :return: the highest-priority element in the queue.
        :rtype: Any
        """
        top = self[0]
        last_el = self.pop()
        if len(self):
            self[0] = last_el
            self.bubble_down(0)
        return top

    def heap_insert(self, x):
        """Insert an element into the queue (at correct priority).

        :param x: the element to insert.
        :type x: Any
        """
        self.append(x)
        self.bubble_up(len(self) - 1)

    def swap(self, i, j):
        """Convenience method to swap to elements in the queue.

        :param i: the index of the first element to swap.
        :type i: int
        :param j: the index of the second element to swap.
        :type j: int
        """
        self[i], self[j] = self[j], self[i]

    def bubble_up(self, curr):
        """Bubble an element at index curr up to its correct place in the heap recursively.

        :param curr: the index of the element to bubble up
        :type curr: int
        """
        parent = (curr - 1) // 2
        if parent >= 0 and self.cmp(self[curr], self[parent]):
            self.swap(curr, parent)
            self.bubble_up(parent)

    def bubble_down(self, curr):
        """Bubble an element at a given index down to its correct place.

        :param curr: the index of the element to bubble down
        :type curr: int
        """
        child = curr * 2 + 1
        if child < len(self):
            rchild = child + 1
            if len(self) > rchild and self.cmp(self[rchild], self[child]):
                child = rchild
            if self.cmp(self[child], self[curr]):
                self.swap(curr, child)
                self.bubble_down(child)


class MinHeap(PriorityQueue):
    def __init__(self, seq):
        super().__init__(seq, cmp=operator.lt)


class MaxHeap(PriorityQueue):
    def __init__(self, seq):
        super().__init__(seq, cmp=operator.gt)

