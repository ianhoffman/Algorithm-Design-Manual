from collections import deque


def bfs(G, start, is_valid_edge=lambda e: True):
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

