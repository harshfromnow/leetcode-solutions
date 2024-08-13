class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        s=[]
        if m*n!=r*c:
            return mat
        for k in mat:
            s+=k
        l=[[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                l[i][j]+=s.pop(0)
        return l