from abc import ABC
from abc import abstractmethod
from collections import defaultdict
from itertools import chain


class BaseEdge:
    def __init__(self, x, y):
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
    def __init__(self, x, y, weight):
        super().__init__(x, y)
        self.weight = weight


class NetFlowEdge(BaseEdge):
    def __init__(self, x, y, capacity, flow, residual):
        super().__init__(x, y)
        self.capacity = capacity
        self.flow = flow
        self.residual = residual


class BaseGraph(ABC):
    input_dir = 'input_data'

    @classmethod
    def from_file(cls, filename, directed=False):
        with open('{}/{}.txt'.format(cls.input_dir, filename), 'r') as f:
            edges = []
            for line in f.readlines():
                x, y, weight = line.split()
                edges.append([int(x), int(y), int(weight)])
            return cls(edges, directed=directed)

    @classmethod
    def from_file_weighted_vertices(cls, filename):
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
        if directed is None:
            directed = self.directed
        self[x] = list(filter(lambda e: e.y != y, self[x]))
        if not directed:
            self.delete_edge(y, x, directed=True)

    def find_edge(self, x, y):
        return next((edge for edge in self[x] if edge.y == y), None)

    @abstractmethod
    def insert_edge(self, *args, **kwargs):
        pass

    def iter_edges(self):
        yield from chain.from_iterable(self.edges.values())


class Graph(BaseGraph):
    def insert_edge(self, x, y, weight=1, directed=False):
        p = Edge(x, y, weight)
        self.edges[x].append(p)

        if directed is False:
            self.insert_edge(p.y, x, weight=p.weight, directed=True)


class ResidualFlowGraph(BaseGraph):
    def insert_edge(self, x, y, capacity, directed=False, residual=None):
        if residual is None:
            residual = capacity

        p = NetFlowEdge(x, y, capacity, 0, residual)
        self.edges[x].append(p)

        if directed is False:
            self.insert_edge(p.y, x, p.capacity, directed=True, residual=0)

