import unittest

from algorithms.combinatorial_search_and_heuristics.backtrack import backtrack_permutations
from algorithms.combinatorial_search_and_heuristics.backtrack import backtrack_subsets


class BackTrackTestCase(unittest.TestCase):
    def test_backtrack_permutations(self):
        self.assertListEqual(
            backtrack_permutations(3),
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1]
            ]
        )

    def test_backtrack_subsets(self):
        self.assertListEqual(
            backtrack_subsets(3),
            [
                [1, 2, 3],
                [1, 2],
                [1, 3],
                [1],
                [2, 3],
                [2],
                [3],
                []
            ]
        )

        self.assertListEqual(
            backtrack_subsets(2),
            [
                [1, 2],
                [1],
                [2],
                []
            ]
        )

        self.assertListEqual(
            backtrack_subsets(4),
            [
                [1, 2, 3, 4],
                [1, 2, 3],
                [1, 2, 4],
                [1, 2],
                [1, 3, 4],
                [1, 3],
                [1, 4],
                [1],
                [2, 3, 4],
                [2, 3],
                [2, 4],
                [2],
                [3, 4],
                [3],
                [4],
                []
            ]
        )
