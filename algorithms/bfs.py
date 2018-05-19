from collections import deque


def bfs(G, start):
    queue = deque([start])
    discovered = {start}
    parents = {}
    while queue:
        curr = queue.popleft()
        edge = G.edges[curr]
        while edge:
            if edge.y not in discovered:
                queue.append(edge.y)
                discovered.add(edge.y)
                parents[edge.y] = curr
            edge = edge.next
    return parents

