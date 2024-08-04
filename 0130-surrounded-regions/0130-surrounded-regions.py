from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r=len(board)
        c=len(board[0])
        def dfs(i,j):

            #return condition
            if (i<0 or i>=r or 
                j<0 or j>=c or 
                board[i][j]!="O"):
                return
            
            #core dfs : mark as 'T' and spredding based on the CONNECT rule
            board[i][j]="T"
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                dfs(i+dx,j+dy)

        #do dfs to every node on boundery
        for i in range(r):
            dfs(i,0)
            dfs(i,c-1)
        for j in range(1,c-1):
            dfs(0,j)
            dfs(r-1,j)

        for i in range(r):
            for j in range(c):
                if board[i][j]=="T":
                    board[i][j]="O"
                else:
                    board[i][j]="X"
        '''
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

        '''