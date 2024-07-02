class Solution:
    def change(self, row, col, matrix):
            for i in range(len(matrix[0])):
                matrix[row][i]=0
            for i in range(len(matrix)):
                matrix[i][col]=0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=[]
        row=len(matrix)
        col=len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    l.append([i,j])
        for t in l:
            self.change(t[0],t[1],matrix)
