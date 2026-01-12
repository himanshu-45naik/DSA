class Solution:
    def __init__(self, n, m):
        self.n = n                  # maximum node label
        self.m = m                  # number of edges
        self.adj = [[] for _ in range(n + 1)]  # index 0 unused

    def dfs_traversal(self, start_node):
        # build adjacency list
        for _ in range(self.m):
            u = int(input("Vertex 1: "))
            v = int(input("Vertex 2: "))

            if 1 <= u <= self.n and 1 <= v <= self.n:
                self.adj[u].append(v)
                self.adj[v].append(u)
            else:
                print(f"Invalid vertex index: {u}, {v}")

        visited = [0] * (self.n + 1)
        res = []

        def dfs(node):
            visited[node] = 1
            res.append(node)

            for neighbor in self.adj[node]:
                if visited[neighbor] == 0:
                    dfs(neighbor)

        dfs(start_node)
        return res

if __name__ == "__main__":
    n = int(input("Number of vertices: "))
    m = int(input("Number of edges: "))
    start_node = int(input("Start Node: "))

    s = Solution(n, m)
    print(s.dfs_traversal(start_node))