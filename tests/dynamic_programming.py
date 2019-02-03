import unittest

from algorithms.dynamic_programming import edit_distance
from algorithms.dynamic_programming import integer_partition
from algorithms.dynamic_programming import minimum_weight_partition


class DynamicProgrammingTestCase(unittest.TestCase):
    def test_edit_distance(self):
        X = 'ABC'
        Y = 'DEF'
        self.assertEqual(edit_distance(X, Y), 3)

        X = 'ABC'
        Y = 'DBC'
        self.assertEqual(edit_distance(X, Y), 1)

        X = 'AABC'
        Y = 'ABC'
        self.assertEqual(edit_distance(X, Y), 1)

        X = 'AAABC'
        Y = 'ABC'
        self.assertEqual(edit_distance(X, Y), 2)

        X = 'Thou shalt not'
        Y = 'You should not'
        self.assertEqual(edit_distance(X, Y), 5)

        X = 'Kitten'
        Y = 'Sitting'
        self.assertEqual(edit_distance(X, Y), 3)

        X = 'Saturday'
        Y = 'Sunday'
        self.assertEqual(edit_distance(X, Y), 3)

    def test_integer_partition(self):
        self.assertEqual(integer_partition(0), 1)
        self.assertEqual(integer_partition(4), 5)
        self.assertEqual(integer_partition(8), 22)
        self.assertEqual(integer_partition(30), 5604)

    def test_minimum_weight_partition(self):
        A = [9, 1, 7, 3, 4, 10, 8, 1, 1, 8]
        self.assertEqual(minimum_weight_partition(A, 0), 52)
        self.assertEqual(minimum_weight_partition(A, 1), 28)
        self.assertEqual(minimum_weight_partition(A, 2), 18)
        self.assertEqual(minimum_weight_partition(A, 3), 17)
        self.assertEqual(minimum_weight_partition(A, 4), 14)
        self.assertEqual(minimum_weight_partition(A, 5), 10)  # Ten is smallest possible
