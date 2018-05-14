import random
import unittest

from algorithms.prims import prim

from data_structures import Graph
from data_structures import MinHeap


class AlgorithmsTestCase(unittest.TestCase):
    def test_prims_algorithm(self):
        directed = False
        g = Graph(directed)
        g.read_graph(directed)
        minimum_spanning_tree = prim(g, 0)
        self.assertEqual(len(minimum_spanning_tree), g.nvertices)


class DataStructuresTestCase(unittest.TestCase):
    def test_priority_queue(self):
        for i in range(5):
            l = list(range(20))
            random.shuffle(l)
            pq = MinHeap(l)
            result = []
            while len(pq):
                result.append(pq.extract())
            self.assertListEqual(result, list(range(20)))


if __name__ == '__main__':
   unittest.main()

