def floyd(adjacency_matrix):
    """Non-vectorized implementation of Floyd's algorithm for finding all shortest paths between vertices in a graph.

    :param adjacency_matrix: a 2-dimensional matrix in which the distance between vertices i, j is represented by
        adjacency_matrix[i][j]. If the distance has not yet been calculated, it's equal to sys.maxsize.
    :type adjacency_matrix: list[list[int]]
    :return: the adjacency matrix with all distances derived (except the distances between (v, v)).
    :rtype: list[list[int]]
    """
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

