
class Graph:
    def __init__(self):
        self.n = int(input("Number of vertices: "))
        self.m = int(input("Number of edges: "))
        self.matrix = [[0 for _ in range(self.n)] for _ in range(self.n)]

    def add_edges(self):
        for _ in range(self.m):
            u = int(input("Element u: "))
            v = int(input("Element v: "))

            if 0 <= u < self.n and 0 <= v < self.n:
                self.matrix[u][v] = 1
                self.matrix[v][u] = 1
            else:
                print("Invalid vertex index")

        return self.matrix


if __name__ == "__main__":
    g = Graph()
    print(g.add_edges())

