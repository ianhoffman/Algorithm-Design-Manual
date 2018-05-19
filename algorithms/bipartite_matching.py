from algorithms.netflow import netflow


def bipartite_match(G):
    """

    :param G:
    :type G: data_structures.Graph
    :return:
    """
    vertices = sorted(list(G.edges.keys()))
    num_vertices = len(G)
    half = int(num_vertices / 2)
    for vertex in vertices[:half]:
        G.insert_edge(-1, vertex, 1)
    for vertex in vertices[half:]:
        G.insert_edge(num_vertices, vertex, 1)

    R = G.to_residual_flow_graph()

    return netflow(R, -1, num_vertices)

