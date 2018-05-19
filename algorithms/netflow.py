from functools import partial

from algorithms import bfs


netflow_bfs = partial(bfs, is_valid_edge=lambda e: e.residual > 0)


def netflow(R, source, sink):
    parents = netflow_bfs(R, source)
    volume = path_volume(R, source, sink, parents)
    while volume > 0:
        augment_path(R, source, sink, parents, volume)
        parents = netflow_bfs(R, source)
        volume = path_volume(R, source, sink, parents)
    return sum(edge.residual for edge in R[sink])


def augment_path(R, start, end, parents, volume):
    if start == end:
        return

    parent = parents.get(end)

    edge = R.find_edge(parent, end)
    edge.flow += volume
    edge.residual -= volume

    edge = R.find_edge(end, parent)
    edge.residual += volume

    augment_path(R, start, parent, parents, volume)


def path_volume(R, start, end, parents):
    parent = parents.get(end)

    if parent is None:
        return 0

    edge = R.find_edge(parent, end)

    if start == parent:
        return edge.residual
    else:
        return min(path_volume(R, start, parent, parents), edge.residual)

