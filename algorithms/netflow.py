from algorithms import bfs


def netflow(R, source, sink):
    """Determine the maximum flow from source to sink in the residual flow graph R.

    :param R: a residual flow graph
    :type R: data_structures.ResidualFlowGraph
    :param source: the source vertex from which the flow begins
    :type source: int
    :param sink: the sink vertex at which the flow terminates
    :type sink: int
    :return: an integer representing the total flow from source to sink
    :rtype: int
    """
    def netflow_bfs():
        """Conduct BFS on the residual graph, only choosing edges which have residual capacity.

        :return: a dict mapping vertices to their parent vertex in the search
        """
        return bfs(R, source, is_valid_edge=lambda e: e.residual > 0)

    def augment_path(start, end):
        """Recursively augment a path by increasing the flow from the source to the sink (and decreasing the residual
        capacity) while increasing the residual capacity flowing from the sink to the source.

        :param start: the start vertex for the path
        :type start: int
        :param end: the end vertex for the path
        :type end: int
        """
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
        """Recursively derive the min volume which can be pushed through a given path

        :param start: the start of the path
        :type: int
        :param end: the end of the path
        :type end: int
        :return: the residual volume that can be pushed along the given path
        :rtype: int
        """
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

