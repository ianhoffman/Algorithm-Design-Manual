import sys


def dijkstra(G, s, t):
    """Find the shortest path from vertex s to vertex t.

    :param G: a graph
    :type G: data_structures.graph.Graph
    :param s: a graph vertex
    :type s: int
    :param t: the target vertex
    :type t: int
    :return: an array of vertices representing the shortest path from s to t
    :rtype: list[int]
    """
    known = {s}
    dist = [sys.maxsize for _ in range(G.nvertices)]
    shortest_paths = [[s] for _ in range(G.nvertices)]
    for edge in G.edges[s]:
        dist[edge.y] = edge.weight
        shortest_paths[edge.y].append(edge.y)
    last = s
    while last != t:
        v_next = None
        min_dist = sys.maxsize
        for i in range(len(dist)):
            if i not in known and dist[i] < min_dist:
                min_dist = dist[i]
                v_next = i

        for edge in G.edges[v_next]:
            if edge.y != s and dist[edge.y] > min_dist + edge.weight:
                dist[edge.y] = min_dist + edge.weight
                shortest_paths[edge.y] = shortest_paths[v_next] + [edge.y]

        last = v_next
        known.add(v_next)

    return shortest_paths[t]

