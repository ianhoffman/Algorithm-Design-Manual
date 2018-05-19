def floyd(adjacency_matrix):
    """Non-optimized implementation of floyd's algorithm for finding all-pairs shorts paths in O(n ^ 3) time."""
    for k in range(len(adjacency_matrix)):
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix)):
                if i == j:
                    continue
                weight_through_k = adjacency_matrix[i][k] + adjacency_matrix[k][j]
                if weight_through_k < adjacency_matrix[i][j]:
                    adjacency_matrix[i][j] = weight_through_k

    for i in range(len(adjacency_matrix)):
        adjacency_matrix[i][i] = None  # Blank-out (v, v) paths

    return adjacency_matrix

