from collections import deque


def bfs(G, start, is_valid_edge=lambda e: True):
    """Conduct breadth-first search on the given graph

    :param G: a graph
    :type G: data_structures.BaseGraph
    :param start: the vertex from which the search begins
    :type start: int
    :param is_valid_edge: an additional function which determines whether to explore a given edge
    :type is_valid_edge: function
    :return: a mapping of vertices to their parent vertex in the search
    :rtype: dict
    """
    queue = deque([start])
    discovered = {start}
    parents = {}

    while queue:
        curr = queue.popleft()
        for edge in G.edges[curr]:
            if edge.y not in discovered and is_valid_edge(edge):
                queue.append(edge.y)
                discovered.add(edge.y)
                parents[edge.y] = curr

    return parents

