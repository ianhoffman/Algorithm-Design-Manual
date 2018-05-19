from algorithms import bfs


def netflow(R, source, sink):
    def netflow_bfs():
        return bfs(R, source, is_valid_edge=lambda e: e.residual > 0)

    def augment_path(start, end):
        if start == end:
            return

        parent = parents.get(end)

        edge = R.find_edge(parent, end)
        edge.flow += volume
        edge.residual -= volume

        edge = R.find_edge(end, parent)
        edge.residual += volume

        augment_path(start, parent)

    def path_volume(start, end):
        parent = parents.get(end)

        if parent is None:
            return 0

        edge = R.find_edge(parent, end)

        if start == parent:
            return edge.residual
        else:
            return min(path_volume(start, parent), edge.residual)

    parents = netflow_bfs()
    volume = path_volume(source, sink)
    while volume > 0:
        augment_path(source, sink)
        parents = netflow_bfs()
        volume = path_volume(source, sink)

    return sum(edge.residual for edge in R[sink])

