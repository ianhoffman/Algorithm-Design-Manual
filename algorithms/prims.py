"""A simple implementation of Prim's algorithm."""
import sys

def prim(g, start):
    # minimum_spanning_tree = []
    intree = [False for _ in range(g.nvertices)]
    distance = [sys.maxsize for _ in range(g.nvertices)]
    parent = [-1 for _ in range(g.nvertices)]
    
    distance[start] = 0
    v = start
    
    while intree[v] is False:
        # minimum_spanning_tree.append(v)
        intree[v] = True
        p = g.edges[v]
        while p is not None:
            w = p.y
            weight = p.weight
            if distance[w] > weight and intree[w] is False:
                distance[w] = weight
                parent[w] = v
            p = p.next

        v = 1
        dist = sys.maxsize
        for i in range(g.nvertices):
            if intree[i] is False and dist > distance[i]:
                dist = distance[i]
                v = i

    return parent

