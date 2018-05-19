from data_structures import Edge
from data_structures import EdgeNode


class Graph:
    """A simple graph object"""
    input_dir = 'input_data'

    @classmethod
    def from_file(cls, filename, directed=False):
        with open('{}/{}.txt'.format(cls.input_dir, filename), 'r') as f:
            nvertices = int(f.readline())
            edges = []
            for line in f.readlines():
                x, y, weight = line.split()
                edges.append([int(x), int(y), int(weight)])
            return cls(nvertices, edges, directed=directed)

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

            return cls(len(vertices), edges, directed=True)

    def __init__(self, nvertices, edges, directed=False):
        self.nvertices = nvertices
        self.directed = directed
        self.degree = [0 for _ in range(len(self))]
        self.edges = [None for _ in range(len(self))]

        for edge in edges:
            self.insert_edge(*edge, directed=directed)

    def __len__(self):
        return self.nvertices

    def __repr__(self):
        edges = []
        for i in range(len(self)):
            for edge in self.edges[i]:
                edges.append(('({}, {}, weight={})'.format(i, edge.y, edge.weight)))
        return '{}([{}])'.format(self.__class__.__name__, ', '.join(edges))

    def insert_edge(self, x, y, weight=1, directed=False):
        p = EdgeNode(y, weight, next=self.edges[x])
        self.edges[x] = p
        self.degree[x] += 1

        if directed is False:
            self.insert_edge(y, x, weight=weight, directed=True)

    def iter_edges(self):
        for i, edge_node in enumerate(self.edges):
            while edge_node:
                yield Edge(x=i, y=edge_node.y, weight=edge_node.weight)
                edge_node = edge_node.next

