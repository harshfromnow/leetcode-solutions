class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}
        
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
        return dfs(0,n)