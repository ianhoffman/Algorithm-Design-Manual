import random
import unittest

from data_structures import MinHeap


class HeapTestCase(unittest.TestCase):
    def test_priority_queue(self):
        for i in range(5):
            l = list(range(20))
            random.shuffle(l)
            pq = MinHeap(l)
            result = []
            while len(pq):
                result.append(pq.extract())
            self.assertListEqual(result, list(range(20)))

