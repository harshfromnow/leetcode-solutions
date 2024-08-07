class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        n = len(cuts)
        dp = [[0]*n for _ in range(n)]
        for l in range(2, n):
            for i in range(n - l):
                j = i + l
                dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i+1, j)) + cuts[j] - cuts[i]
        return dp[0][n-1]
        '''dp = {}
        
        def dfs(l, r):
            if r - l == 1:  # If the length of the segment is 1
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            res = float('inf')
            for c in cuts:
                if l < c < r:
                    res = min(res, (r - l) + dfs(l, c) + dfs(c, r))
            
            if res == float('inf'):
                dp[(l, r)] = res = 0
            else:
                dp[(l, r)] = res
            return res
        return dfs(0,n)'''