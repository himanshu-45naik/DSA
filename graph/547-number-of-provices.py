# 547. Number Of Provinces

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        provinces = 0

        def dfs(node):
            visited[node] = 1
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and visited[neighbor] == 0:
                    dfs(neighbor)

        for i in range(n):
            if visited[i] == 0:
                provinces += 1
                dfs(i)

        return provinces

if __name__ == "__main__":
    
    s = Solution()

    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(f"For graph {isConnected}: {s.findCircleNum(isConnected)}")

    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(f"For graph {isConnected}: {s.findCircleNum(isConnected)}")
