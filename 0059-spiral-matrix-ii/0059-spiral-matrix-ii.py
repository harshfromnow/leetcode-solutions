class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom, left, right = 0, n-1, 0, n-1
        l=[i for i in range(1,n*n+1)]
        print(l)
        mat=[[0]*n for _ in range(n)]
        while l:
            for i in range(left, right+1):
                mat[left][i]=l.pop(0)
            top+=1
            for j in range(top,bottom+1):
                mat[j][right]=l.pop(0)
            right-=1
            if top<=bottom:
                for i in range(right, left-1,-1):
                    mat[bottom][i]=l.pop(0)
                bottom-=1
            if left<=right:
                for i in range(bottom, top -1, -1):
                    mat[i][left]=l.pop(0)
                left+=1
        return mat