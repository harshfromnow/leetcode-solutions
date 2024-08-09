class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(x, y, px, py):
            if (x, y) in visited:
                return True
            visited.add((x, y))
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[x][y]:
                    if (nx, ny) != (px, py):
                        if dfs(nx, ny, x, y):
                            return True
            return False

        m, n = len(grid), len(grid[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if dfs(i, j, -1, -1):
                        return True
        return False
