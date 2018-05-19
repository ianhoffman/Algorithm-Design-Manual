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
    dist = [sys.maxsize for _ in range(len(G))]
    parents = [None for _ in range(len(G))]
    for edge in G.edges[s]:
        dist[edge.y] = edge.weight
        parents[edge.y] = s
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
                parents[edge.y] = v_next

        last = v_next
        known.add(v_next)

    # Walk parents backwards to find shortest path
    results = [t]
    curr_parent = parents[t]
    while curr_parent != s:
        results.append(curr_parent)
        curr_parent = parents[curr_parent]
    results.append(s)
    return list(reversed(results))

