from algorithms.graphs.netflow import netflow


def bipartite_match(R):
    """Return the match number of bipartite matching available in a given graph.

    Assumes the first n / 2 vertices correspond to the first "half" of the graph while the second n / 2 vertices
    are the second "half" which we should attempt to match with the first half.

    :param R: a graph
    :type R: data_structures.ResidualFlowGraph
    :return: the number of matching available
    :rtype: int
    """
    vertices = sorted(list(R.edges.keys()))
    num_vertices = len(R)
    half = int(num_vertices / 2)
    for vertex in vertices[:half]:
        R.insert_edge(-1, vertex, 1)
    for vertex in vertices[half:]:
        R.insert_edge(vertex, num_vertices, 1)

    return netflow(R, -1, num_vertices)

