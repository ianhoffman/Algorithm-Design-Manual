import itertools

from typing import Tuple

from .sat_to_3sat import *


def is_satisfiable(clauses: Tuple[Tuple[int, ...], ...], variables: Tuple[int, ...]) -> bool:
    """Whether or not a set of variables V can satisfy a set of clauses C."""
    if not clauses:
        return True
    elif not variables:
        return False
    else:
        current_variable = variables[0]
        new_variables = variables[1:]
        if is_satisfiable(tuple(c for c in clauses if current_variable not in c), new_variables):
            return True
        negated_variable = ~current_variable
        return is_satisfiable(tuple(c for c in clauses if negated_variable not in c), new_variables)


def vertex_cover_to_sat(vertices: Tuple[int, ...], edges: Tuple[Tuple[int, int], ...], k: int) -> bool:
    """Determine whether a graph has a vertex cover of size K by making repeated calls to is_satisfiable."""
    return any(is_satisfiable(edges, vertex_subset) for vertex_subset in itertools.combinations(vertices, k))

