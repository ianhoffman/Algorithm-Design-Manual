from abc import ABC
from abc import abstractmethod
from collections import defaultdict
from itertools import chain


class BaseEdge:
    """A base class for edges."""
    def __init__(self, x, y):
        """Initialize the edge.

        :param x: the vertex at which the edge originates.
        :type x: int
        :param y: the vertex at which the edge terminates.
        :type y: int
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(
                f'{k}={v}'
                for k, v in vars(self).items()
                if not k.startswith('_')
            )
        )


class Edge(BaseEdge):
    """A generic edge implementation."""
    def __init__(self, x, y, weight):
        """Initialize the edge.

        :param x: the vertex at which the edge originates.
        :type x: int
        :param y: the vertex at which the edge terminates.
        :type y: int
        :param weight: weight of the edge
        :type weight: int
        """
        super().__init__(x, y)
        self.weight = weight


class NetFlowEdge(BaseEdge):
    """An edge in a NetFlow graph."""
    def __init__(self, x, y, capacity, flow, residual):
        """Initialize the edges

        :param x: the vertex from which the edge is pointing away
        :type x: int
        :param y: the vertex to which the edge points
        :type y: int
        :param capacity: the capacity of the edge
        :type capacity: int
        :param flow: the flow through the edge
        :type flow: int
        :param residual: the residual capacity remaining in the edge
        :type residual: int
        """
        super().__init__(x, y)
        self.capacity = capacity
        self.flow = flow
        self.residual = residual


class BaseGraph(ABC):
    input_dir = 'input_data'

    @classmethod
    def from_file(cls, filename, directed=False):
        """Initialize a graph from a file.

        :param filename: name of the file in which each line represents a from vertex, to vertex, and weight
        :type filename: str
        :param directed: whether or not the graph should be directed
        :type: directed: bool
        :return: a newly-initialized graph instance
        :rtype: BaseGraph
        """
        with open('{}/{}.txt'.format(cls.input_dir, filename), 'r') as f:
            edges = []
            for line in f.readlines():
                x, y, weight = line.split()
                edges.append([int(x), int(y), int(weight)])
            return cls(edges, directed=directed)

    @classmethod
    def from_file_weighted_vertices(cls, filename):
        """Initialize a graph in which vertices, not edges, have weights, from a file.

        :param filename: name of the file containing the graph info
        :type filename: str
        :return: a newly-initialized graph instance
        :rtype: BaseGraph
        """
        with open('{}/{}.txt'.format(cls.input_dir, filename), 'r') as f:
            vertices = {}
            line = f.readline()
            while line.strip():
                if line.strip():
                    vertex, weight = line.split()
                    vertices[int(vertex)] = int(weight)
                line = f.readline()

            edges = []
            line = f.readline()
            while line.strip():
                x, y = line.split()
                edges.append([int(x), int(y), vertices[int(y)]])
                edges.append([int(y), int(x), vertices[int(x)]])
                line = f.readline()

            return cls(edges, directed=True)

    def __init__(self, edges, directed=False):
        """Initialize the graph

        :param edges: a list of (start_vertex, end_vertex, weight) edges
        :type edges: list[tuple(int, int, int)]
        :param directed: whether or not the graph is directed
        :type directed: bool
        """
        self.directed = directed
        self.edges = defaultdict(list)
        for edge in edges:
            self.insert_edge(*edge, directed=directed)

    def __iter__(self):
        yield from self.edges

    def __getitem__(self, vertex):
        return self.edges[vertex]

    def __len__(self):
        return len(self.edges)

    def __repr__(self):
        return f'{self.__class__.__name__}(edges={dict(self.edges)}, directed={self.directed})'

    def __setitem__(self, key, value):
        self.edges[key] = value

    def delete_edge(self, x, y, directed=None):
        """Delete an edge between x and y. If the graph is not directed, also delete the edge between y and x.

        :param x: start vertex
        :type x: int
        :param y: end vertex
        :type y: int
        :param directed: whether or not the graph is directed
        :type directed: bool
        """
        if directed is None:
            directed = self.directed
        self[x] = list(filter(lambda e: e.y != y, self[x]))
        if not directed:
            self.delete_edge(y, x, directed=True)

    def find_edge(self, x, y):
        """Find an edge going from x to y, if one exists.

        :param x: origin of the edge
        :type x: int
        :param y: terminus of the edge
        :type y: int
        :return: an edge object
        :rtype: BaseEdge
        """
        return next((edge for edge in self[x] if edge.y == y), None)

    @abstractmethod
    def insert_edge(self, *args, **kwargs):
        """Insert an edge into the graph. Depends on the kind of graph (filled in by subclasses)."""

    def iter_edges(self):
        """Alternative iterator that yields all edges.

        :return: an iterator which yields all edges in the graph.
        :rtype: Iterator
        """
        yield from chain.from_iterable(self.edges.values())


class Graph(BaseGraph):
    def insert_edge(self, x, y, weight=1, directed=False):
        """Insert an edge from x to y into the graph. If the graph is undirected, also insert an edge from y to x.

        :param x: start vertex
        :type x: int
        :param y: end vertex
        :type y: int
        :param weight: weight of the edge
        :type weight: int
        :param directed: whether or not the graph is directed
        :type directed: bool
        """
        p = Edge(x, y, weight)
        self.edges[x].append(p)

        if directed is False:
            self.insert_edge(p.y, x, weight=p.weight, directed=True)


class ResidualFlowGraph(BaseGraph):
    def insert_edge(self, x, y, capacity, directed=False, residual=None):
        """Insert an edge from x to y into a residual graph.
        If the graph is undirected, also insert an edge from y to x.

        :param x: origin vertex
        :type x: int
        :param y: terminus vertex
        :type y: int
        :param capacity: capacity of edge
        :type capacity: int
        :param directed: whether the graph is directed
        :type directed: bool
        :param residual: residual capacity of edge
        :type residual: int
        """
        if residual is None:
            residual = capacity

        p = NetFlowEdge(x, y, capacity, 0, residual)
        self.edges[x].append(p)

        if directed is False:
            self.insert_edge(p.y, x, p.capacity, directed=True, residual=0)

