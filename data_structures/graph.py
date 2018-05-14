"""A simple graph object"""
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


class Graph:
    def __init__(self, directed):
        self.edges = None
        self.degree = None
        self.nvertices = 0
        self.nedges = 0
        self.directed = directed

    def read_graph(self, directed, filename):
        with open('data_structures/{}.txt'.format(filename), 'r') as f:
            nvertices, nedges = f.readline().split()

            self.nvertices = int(nvertices)
            self.nedges = int(nedges)
            self.edges = [None for _ in range(self.nedges)]
            self.degree = [0 for _ in range(self.nvertices)]

            for _ in range(self.nedges):
                x, y, weight = f.readline().split()
                self.insert_edge(int(x), int(y), int(weight), directed)

    def insert_edge(self, x, y, weight=1, directed=False):
        p = EdgeNode()
        p.y = y
        p.weight = weight
        p.next = self.edges[x]
        self.edges[x] = p
        self.degree[x] += 1

        if directed is False:
            self.insert_edge(y, x, weight=weight, directed=True)
        else:
            self.nedges += 1

    def print_graph(self):
        for i in range(self.nvertices):
            p = self.edges[i]
            edges = []
            while p is not None:
                edges.append(str(p.y))
                p = p.next
            print('{}: {}'.format(i, ' '.join(edges)))

