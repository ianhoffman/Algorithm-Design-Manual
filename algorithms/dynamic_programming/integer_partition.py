"""
Problem: Compute the number of ways of summing to an integer n.
Input: An integer n.
Returns: The number of ways to summing to that integer n.

"""
import numpy as np


def integer_partition(n):
    # First, construct a partition matrix. Row indices represent summands through n (starting at 0),
    # and column indices represent the number 0...n. Thus, an index i, j represents the number of
    # ways of summing to the number j using the summands 0...i only. The number of ways of summing
    # to n using the summands 0...n will be given by partition_matrix[n][n].
    partition_matrix = np.zeros((n + 1, n + 1), dtype=np.int)

    # There is one way to sum to 0 using the summands 0 through i. (Just use 0 and no other summand.)
    partition_matrix[:, 0] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i > j:
                # This summand cannot provide any additional ways of summing to j
                partition_matrix[i][j] = partition_matrix[i - 1][j]
            else:
                # Ways of summing to j without using the summand i
                ways_without_summand = partition_matrix[i - 1][j]

                # Ways of summing to j using the summand i. This equals the ways of summing to j - i,
                # because, by adding i to each of the ways of summing to (j - i), we determine a new
                # way of summing to j.
                ways_with_summand = partition_matrix[i][j - i]

                partition_matrix[i][j] = ways_without_summand + ways_with_summand

    return partition_matrix[n][n]


if __name__ == '__main__':
    assert integer_partition(4) == 5
    assert integer_partition(8) == 22
    assert integer_partition(30) == 5604

