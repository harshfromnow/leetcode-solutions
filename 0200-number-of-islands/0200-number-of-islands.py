class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == '0' or (r, c) in visit:
                return
            visit.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r, c) not in visit:
                    dfs(r, c)
                    count += 1

        return count
