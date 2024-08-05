class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        c=0
        row=len(grid)
        col=len(grid[0])
        rowmax=[]
        colmax=[]
        for k in grid:
            rowmax.append(max(k))
        print(rowmax)
        l=[]
        for i in range(row):
            t=[]
            for j in range(col):
                t.append(grid[j][i])
            l.append(t)
        for k in l:
            colmax.append(max(k))
        print(colmax)
        for i in range(row):
            for j in range(col):
                c+=min(rowmax[i],colmax[j])-grid[i][j]
        return c
