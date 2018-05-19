import sys
import unittest

from algorithms import bfs
from algorithms import bipartite_match
from algorithms import dijkstra
from algorithms import floyd
from algorithms import kruskal
from algorithms import netflow
from algorithms import prim

from data_structures import Graph
from data_structures import ResidualFlowGraph


class GraphTestCase(unittest.TestCase):
    def test_bfs(self):
        g = Graph.from_file('graph_bfs')
        result = bfs(g, 0)
        self.assertDictEqual(
            result,
            {
                1: 0,
                2: 1,
                4: 0,
                3: 4,
                5: 0
            }
        )

    def test_bipartite_match(self):
        R = ResidualFlowGraph.from_file('graph_netflow_bipartite')
        result = bipartite_match(R)
        self.assertEqual(result, 6)

        R = ResidualFlowGraph.from_file('graph_netflow_bipartite')
        R.delete_edge(0, 6)
        result = bipartite_match(R)
        self.assertEqual(result, 5)

        R = ResidualFlowGraph.from_file('graph_netflow_bipartite')
        R.delete_edge(0, 6)
        R.delete_edge(5, 11)
        result = bipartite_match(R)
        self.assertEqual(result, 4)

    def test_dijkstra(self):
        g = Graph.from_file('graph_shortest_path')
        result = dijkstra(g, 0, 7)
        self.assertListEqual(result, [0, 1, 7])
        result = dijkstra(g, 0, 4)
        self.assertListEqual(result, [0, 1, 7, 4])

    def test_floyd(self):
        MAX = sys.maxsize
        self.assertListEqual(
            floyd(
                [
                    [MAX,   5,      7,      12,     MAX,    MAX,    MAX],
                    [5,     MAX,    9,      MAX,    7,      MAX,    MAX],
                    [7,     9,      MAX,    4,      4,      3,      MAX],
                    [12,    MAX,    4,      MAX,    MAX,    7,      MAX],
                    [MAX,   7,      4,      MAX,    MAX,    2,      5  ],
                    [MAX,   MAX,    3,      7,      2,      MAX,    2  ],
                    [MAX,   MAX,    MAX,    MAX,    5,      2,      MAX],
                ]
            ),
            [
                [None,  5,      7,      11,     11,     10,     12  ],
                [5,     None,   9,      13,     7,      9,      11  ],
                [7,     9,      None,   4,      4,      3,      5   ],
                [11,    13,     4,      None,   8,      7,      9   ],
                [11,    7,      4,      8,      None,   2,      4   ],
                [10,    9,      3,      7,      2,      None,   2   ],
                [12,    11,     5,      9,      4,      2,      None],
            ]
        )

    def test_kruskal(self):
        mst_total_weight = 23
        g = Graph.from_file('graph_MST')
        result = kruskal(g)
        self.assertEqual(result, mst_total_weight)

    def test_netflow(self):
        r = ResidualFlowGraph.from_file('graph_netflow')
        self.assertEqual(7, netflow(r, 0, 6))

    def test_prims(self):
        mst_total_weight = 23
        g = Graph.from_file('graph_MST')
        result = prim(g, 0)
        self.assertEqual(result, mst_total_weight)

    def test_weighted_vertices(self):
        g = Graph.from_file_weighted_vertices('graph_weighted_vertices')
        self.assertListEqual(dijkstra(g, 0, 7), [0, 1, 7])
        self.assertListEqual(dijkstra(g, 0, 6), [0, 1, 7, 6])
        self.assertListEqual(dijkstra(g, 0, 2), [0, 3, 2])
        self.assertListEqual(dijkstra(g, 4, 5), [4, 1, 0, 3, 5])
        self.assertListEqual(dijkstra(g, 4, 2), [4, 7, 6, 2])
        self.assertListEqual(dijkstra(g, 4, 7), [4, 7])

