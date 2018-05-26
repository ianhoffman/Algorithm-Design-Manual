"""
Problem: Partition an array of integers, A, into at most K sub-arrays such that the ordering of A is preserved and
            the maximum sum of each sub-array is minimized.
Input: An array A and an integer k.

"""
import sys


def minimum_weight_partition(A, k):
    """Simple recursive (non-optimized) implementation."""
    if k == 0:
        return sum(A)
    else:
        min_sum = sys.maxsize
        for i in range(1, len(A)):  # An array of N elements can be partitioned N - 2 ways.
            left = A[:i]
            right = A[i:]
            min_sum = min(min_sum, max(sum(left), minimum_weight_partition(right, k - 1)))
        return min_sum

