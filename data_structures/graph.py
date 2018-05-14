def build_weighted_vertex_graph(filename):
    """Constructs a graph such that each vertex, as opposed to each edge, is assigned a weight."""
    with open('data_structures/{}.txt'.format(filename), 'r') as f:
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

        return Graph(len(vertices), edges, directed=True)


class EdgeNode:
    def __init__(self):
        self.y = 0
        self.weight = 0
        self.next = None

    def __iter__(self):
        curr = self
        while curr is not None:
            yield curr
            curr = curr.next

    def __repr__(self):
        return ', '.join(str(node.y) for node in self)


class Graph:
    """A simple graph object"""

    def __init__(self, nvertices, edges, directed=False):
        self.degree = [0 for _ in range(nvertices)]
        self.nvertices = nvertices
        self.directed = directed
        self.edges = [None for _ in range(nvertices)]

        for edge in edges:
            self.insert_edge(*edge, directed=directed)

    def __repr__(self):
        edges = []
        for i in range(self.nvertices):
            for edge in self.edges[i]:
                edges.append(('({}, {}, weight={})'.format(i, edge.y, edge.weight)))
        return '{}([{}])'.format(self.__class__.__name__, ', '.join(edges))

    @classmethod
    def from_file(cls, filename, directed=False):
        with open('data_structures/{}.txt'.format(filename), 'r') as f:
            nvertices = int(f.readline())
            edges = []
            for line in f.readlines():
                x, y, weight = line.split()
                edges.append([int(x), int(y), int(weight)])
            return cls(nvertices, edges, directed=directed)

    def insert_edge(self, x, y, weight=1, directed=False):
        p = EdgeNode()
        p.y = y
        p.weight = weight
        p.next = self.edges[x]
        self.edges[x] = p
        self.degree[x] += 1

        if directed is False:
            self.insert_edge(y, x, weight=weight, directed=True)

    def print_graph(self):
        for i in range(self.nvertices):
            p = self.edges[i]
            edges = []
            while p is not None:
                edges.append(str(p.y))
                p = p.next
            print('{}: {}'.format(i, ' '.join(edges)))

