import operator


class PriorityQueue(list):
    """A simple priority queue implementation."""
    def __init__(self, seq, cmp):
        super().__init__(seq)
        self.cmp = cmp
        for i in range((len(self) // 2) - 1, -1, -1):
            self.bubble_down(i)

    def extract(self):
        top = self[0]
        last_el = self.pop()
        if len(self):
            self[0] = last_el
            self.bubble_down(0)
        return top

    def heap_insert(self, x):
        self.append(x)
        self.bubble_up(len(self) - 1)

    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]

    def bubble_up(self, curr):
        parent = (curr - 1) // 2
        if parent >= 0 and self.cmp(self[curr], self[parent]):
            self.swap(curr, parent)
            self.bubble_up(parent)

    def bubble_down(self, curr):
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

