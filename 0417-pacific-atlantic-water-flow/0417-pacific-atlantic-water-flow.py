class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set() 
        def dfs(r, c, reachable_set):
            reachable_set.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and (nr, nc) not in reachable_set and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable_set)

        for i in range(m):
            dfs(i, 0, pacific_reachable)
            dfs(i, n - 1, atlantic_reachable)
        for j in range(n):
            dfs(0, j, pacific_reachable)
            dfs(m - 1, j, atlantic_reachable)
        result = list(pacific_reachable & atlantic_reachable)
        return [list(cell) for cell in result]