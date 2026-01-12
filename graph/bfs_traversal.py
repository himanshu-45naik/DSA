class Solution:
    def __init__(self, n, m):
        self.n = n                  # maximum node label
        self.m = m                  # number of edges

        # adjacency list: index 0 unused
        self.adj = [[] for _ in range(n + 1)]

    def bfs_traversal(self, start_node):
        # build adjacency list
        for _ in range(self.m):
            u = int(input("Vertex 1: "))
            v = int(input("Vertex 2: "))

            if 1 <= u <= self.n and 1 <= v <= self.n:
                self.adj[u].append(v)
                self.adj[v].append(u)   # undirected graph
            else:
                print(f"Invalid vertex index: {u}, {v}")

        visited = [0] * (self.n + 1)
        queue = [start_node]
        bfs = []

        visited[start_node] = 1

        while queue:
            node = queue.pop(0)
            bfs.append(node)

            for neighbor in self.adj[node]:
                if visited[neighbor] == 0:
                    visited[neighbor] = 1
                    queue.append(neighbor)

        return bfs


if __name__ == "__main__":
    n = int(input("Number of vertices: "))
    m = int(input("Number of edges: "))
    start_node = int(input("Start Node: "))

    s = Solution(n, m)
    print(s.bfs_traversal(start_node))