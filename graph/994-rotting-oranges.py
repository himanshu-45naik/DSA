# 994. Rotting Oranges

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()

        # multi-source BFS
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        time = 0
        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        while q:
            r, c, t = q.popleft()
            time = max(time, t)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, t + 1))

        # check for leftover fresh oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return time
