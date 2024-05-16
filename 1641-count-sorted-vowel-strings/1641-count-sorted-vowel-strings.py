class Solution:
    def countVowelStrings(self, n: int) -> int:
        d=[[i for i in range(5,0,-1)] for _ in range(n)]
        for i in range(1,n):
            for j in range(3,-1,-1):
                d[i][j]=d[i-1][j]+d[i][j+1]
        return d[n-1][0]