class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        row = len(grid)
        col = len(grid[0])
        visit = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0 or (r, c) in visit:
                return 0
            visit.add((r, c))
            area = 1  
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)
            return area
        max_area = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, dfs(r, c))
        return max_area