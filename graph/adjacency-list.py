from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        if 0 <= u < self.n and 0 <= v < self.n:
            self.adj[u].append(v)
            self.adj[v].append(u)
        else:
            raise ValueError("Invalid vertex index")

    def adjacency_list(self):
        return self.adj


if __name__ == "__main__":
    n = int(input("Number of vertices: "))
    e = int(input("Number of edges: "))

    g = Graph(n)

    for _ in range(e):
        u = int(input("Vertex 1: "))
        v = int(input("Vertex 2: "))
        g.add_edge(u, v)

    print(dict(g.adj))
