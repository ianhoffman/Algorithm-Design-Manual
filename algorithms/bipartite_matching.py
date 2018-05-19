def bipartite_match(G):
    """

    :param G:
    :type G: data_structures.Graph
    :return:
    """
    half = len(G) / 2
    for edge_list in G.edges.values()[:half]:
        print(edge_list)

    for edge_list in G.edges.values()[half:]:
        print(edge_list)

    R = G.to_residual_flow_graph()

