import sys


def prim(g, start):
    """A simple implementation of prim's algorithm for finding the minimum spanning tree of a graph, copied (for the
    most part) from Skiena's implementation in The Algorithm Design Manual.

    :param g: the graph
    :type g: data_structures.Graph
    :param start: the start vertex for the MST
    :type start: int
    :return: the total weight of the MST
    :rtype: int
    """
    intree = [False for _ in range(len(g))]
    distance = [sys.maxsize for _ in range(len(g))]

    distance[start] = 0
    v = start
    
    while intree[v] is False:
        intree[v] = True
        for edge in g.edges[v]:
            w = edge.y
            weight = edge.weight
            if distance[w] > weight and intree[w] is False:
                distance[w] = weight

        v = 1
        dist = sys.maxsize
        for i in range(len(g)):
            if intree[i] is False and dist > distance[i]:
                dist = distance[i]
                v = i

    return sum(distance)

