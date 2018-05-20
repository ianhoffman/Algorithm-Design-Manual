

def backtrack(
    target,
    *,
    is_a_solution,
    process_solution,
    construct_candidates
):
    def _backtrack(a=None):
        if a is None:
            a = []
        if is_a_solution(a, target):
            process_solution(a)
        else:
            candidates = construct_candidates(a)
            for candidate in candidates:
                a.append(candidate)
                _backtrack(a)
                a.pop()
    _backtrack()


def backtrack_subsets(target):
    solutions = []

    def construct_candidates(*args):
        return [True, False]

    def is_a_solution(a, n):
        return len(a) == n

    def process_solution(a):
        solutions.append([i + 1 for i, v in enumerate(a) if v])

    backtrack(
        target,
        is_a_solution=is_a_solution,
        process_solution=process_solution,
        construct_candidates=construct_candidates
    )

    return solutions


def backtrack_permutations(target):
    solutions = []

    def construct_candidates(a):
        return [i for i in range(target) if i not in a]

    def is_a_solution(a, n):
        return len(a) == n

    def process_solution(a):
        solutions.append([i + 1 for i in a])

    backtrack(
        target,
        is_a_solution=is_a_solution,
        process_solution=process_solution,
        construct_candidates=construct_candidates
    )

    return solutions

