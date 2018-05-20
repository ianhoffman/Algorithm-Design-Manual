import sys


def prim(g, start):
    """A simple implementation of prim's algorithm for finding the minimum spanning tree of a graph.

    :param g: the graph
    :type g: data_structures.Graph
    :param start: the start vertex for the MST
    :type start: int
    :return: the total weight of the MST
    :rtype: int
    """
    in_tree = set()
    distance = {start: 0}
    v = start
    
    while v not in in_tree:
        in_tree.add(v)
        for edge in g.edges[v]:
            y = edge.y
            weight = edge.weight
            if distance.get(y, sys.maxsize) > weight and y not in in_tree:
                distance[y] = weight

        dist = sys.maxsize
        for i in g:
            if i not in in_tree and dist > distance.get(i, sys.maxsize):
                dist = distance[i]
                v = i

    return sum(distance.values())

