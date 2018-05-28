import itertools

from typing import cast
from typing import Set
from typing import Tuple

from typeclasses import Edges
from typeclasses import Vertices


def is_satisfiable(clauses: Set[Tuple[int, ...]], variables: Tuple[int, ...]) -> bool:
    """Whether or not a set of variables V can satisfy a set of clauses C."""
    if not clauses:
        return True
    elif not variables:
        return False
    return is_satisfiable({c for c in clauses if variables[0] not in c}, variables[1:]) or \
           is_satisfiable({c for c in clauses if ~variables[0] not in c}, variables[1:])


def set_cover(X: Set[int], F: Tuple[Set[int], ...], k: int) -> bool:
    """Determine if a set X has a set cover of size k composed from the sets in the family F."""
    return any(set(itertools.chain.from_iterable(covering)) == X for covering in itertools.combinations(F, k))


def vertex_cover_to_sat(vertices: Vertices, edges: Edges, k: int) -> bool:
    """Determine whether a graph has a vertex cover of size K by making repeated calls to is_satisfiable."""
    clauses = cast(Set[Tuple[int, ...]], edges)
    return any(is_satisfiable(clauses, vertex_subset) for vertex_subset in itertools.combinations(vertices, k))


def vertex_cover_to_set_cover(vertices: Vertices, edges: Edges, k: int) -> bool:
    F = [
        {
            int(''.join(map(str, sorted(edge))))
            for edge in edges
            if edge[0] == vertex
        } for vertex in vertices
    ]

    return set_cover(set(itertools.chain.from_iterable(F)), tuple(F), k)

