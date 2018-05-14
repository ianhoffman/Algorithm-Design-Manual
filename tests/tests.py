import random
import unittest

from algorithms import dijkstra
from algorithms import prim

from data_structures import build_weighted_vertex_graph
from data_structures import Graph
from data_structures import MinHeap


class AlgorithmsTestCase(unittest.TestCase):
    def test_dijkstra(self):
        g = Graph.from_file('graph_weighted')
        result = dijkstra(g, 0, 7)
        self.assertListEqual(result, [0, 1, 7])
        result = dijkstra(g, 0, 4)
        self.assertListEqual(result, [0, 1, 7, 4])

    def test_prims(self):
        g = Graph.from_file('graph_weighted')
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


class GraphTestCase(unittest.TestCase):
    def test_weighted_vertices(self):
        g = build_weighted_vertex_graph('graph_weighted_vertices')
        self.assertListEqual(dijkstra(g, 0, 7), [0, 1, 7])
        self.assertListEqual(dijkstra(g, 0, 6), [0, 1, 7, 6])
        self.assertListEqual(dijkstra(g, 0, 2), [0, 3, 2])
        self.assertListEqual(dijkstra(g, 4, 5), [4, 1, 0, 3, 5])
        self.assertListEqual(dijkstra(g, 4, 2), [4, 7, 6, 2])
        self.assertListEqual(dijkstra(g, 4, 7), [4, 7])


if __name__ == '__main__':
   unittest.main()

