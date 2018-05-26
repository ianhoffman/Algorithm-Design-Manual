"""
Problem: Compute the cost changing string X into a string Y.
Input: Strings X and Y and a set of changes with associated costs.
Returns: The cost of changing the string X into a string Y, where the cost may be the number of changes required
    (if all transformations have a weight of 1).
"""
import numpy as np


def edit_distance(X, Y):
    X = ' ' + X
    Y = ' ' + Y

    m = len(X)
    n = len(Y)

    d = np.zeros((m, n), dtype=int)

    for i in range(m):
        d[i, 0] = i

    for j in range(n):
        d[0, j] = j

    for j in range(1, n):
        for i in range(1, m):
            if X[i] == Y[j]:
                d[i, j] = d[i - 1, j - 1]
            else:
                d[i, j] = min(
                    d[i - 1, j] + 1,  # delete
                    d[i, j -1] + 1,  # insert
                    d[i - 1, j - 1] + 1  # substitute
                )

    return d[m - 1, n - 1]

