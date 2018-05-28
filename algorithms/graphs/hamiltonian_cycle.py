from typing import List

from typeclasses import Edges
from typeclasses import Vertex
from typeclasses import Vertices


def hamiltonian_cycle(V: Vertices, E: Edges) -> bool:
    """Does there exist in G a simple tour which visits each vertex without repetition?"""
    def find_simple_tour(path: List[Vertex], edges: Edges) -> bool:
        curr = path[-1]
        if len(path) == len(V):  # all vertices visited -- can we make it back to the origin?
            return any(edge[1] == path[0] and edge[0] == path[-1] for edge in edges)
        for edge in edges:
            # Consider each unvisited vertex reachable from the last visited vertex
            if edge[0] == curr and edge[1] not in path:
                vertex = edge[1]
                path.append(vertex)
                if find_simple_tour(path, {edge for edge in edges if edge[0] != curr}):
                    return True
                path.pop()
        return False

    # Check if a hamiltonian cycle is possible from any vertex
    return any(find_simple_tour([vertex], E) for vertex in V)

