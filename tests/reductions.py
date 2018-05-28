from unittest import TestCase


from algorithms.reductions import is_satisfiable
from algorithms.reductions import vertex_cover_to_sat


class ReductionsTestCase(TestCase):
    def test_is_satisfiable(self):
        self.assertTrue(is_satisfiable(((~1, 2), (1, ~2)), (1, 2))) # 1, 2
        self.assertFalse(is_satisfiable(((1, 2), (1, ~2), (~1,)), (1, 2)))
        self.assertTrue(is_satisfiable(((~1, 2), (1, ~2), (~1,)), (1, 2))) # ~1, 2
        self.assertTrue(is_satisfiable(((1, 2, 3), (1, ~2, ~3), (~1,)), (1, 2, 3))) # ~1, 2, ~3
        self.assertTrue(is_satisfiable(((1, 2, 3), (1, ~2, ~3), (~1,), (3,)), (1, 2, 3))) # ~1, ~2, 3
        self.assertFalse(is_satisfiable(((1, 2, 3), (1, ~2, ~3), (~1,), (~2,), (~3,)), (1, 2, 3)))

    def test_vertex_cover_to_sat(self):
        vertices = (1, 2, 3, 4)
        edges = ((1, 2), (1, 3), (1, 4), (2, 1), (2, 4), (3, 1), (3, 4), (4, 1), (4, 2), (4, 3))
        self.assertFalse(vertex_cover_to_sat(vertices, edges, 1))
        self.assertTrue(vertex_cover_to_sat(vertices, edges, 2))

