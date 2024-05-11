class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        row=-1
        cols=len(matrix[0])
        for k in range(rows):
            if matrix[k][0]<= target <= matrix[k][cols-1]:
                row=k
        if row==-1:
            return False
        #binary search2
        l=0
        r=cols-1
        while l<=r:
            m=(l+r)//2
            if target<matrix[row][m]:
                r=m-1
            elif target>matrix[row][m]:
                l=m+1
            else:
                return True
        return False
        