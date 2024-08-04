from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        o="O"

        def dfs(x, y):
            board[x][y] = '#' #mark it
            for x2, y2 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0 <= x2 < m and 0 <= y2 < n and board[x2][y2] == o:
                    dfs(x2, y2)
        #borders
        for i in range(m):
            if board[i][0] == o: dfs(i,0)
            if board[i][n-1] == o: dfs(i,n-1)
        for j in range(n):
            if board[0][j] == o: dfs(0,j)
            if board[m-1][j] == o: dfs(m-1,j)

        #flip remaining regions
        for x in range(m):
            for y in range(n):
                if board[x][y] == o:
                    board[x][y] = 'X' # change to 'X'
                elif board[x][y] == '#':
                    board[x][y] = o # change back to 'O'

        