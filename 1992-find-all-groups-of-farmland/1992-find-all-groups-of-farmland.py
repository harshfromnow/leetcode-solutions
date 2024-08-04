class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        if not land:
            return []
        m=len(land)
        n=len(land[0])
        visit=set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or land[r][c] == 0 or (r, c) in visit:
                return (-1, -1)

            visit.add((r, c))
            max_r, max_c = r, c

            # Traverse all four possible directions
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                sub_max_r, sub_max_c = dfs(nr, nc)
                if sub_max_r is not None and sub_max_c is not None:
                    max_r = max(max_r, sub_max_r)
                    max_c = max(max_c, sub_max_c)

            return max_r, max_c

        result = []
        for r in range(m):
            for c in range(n):
                if land[r][c] == 1 and (r, c) not in visit:
                    min_r, min_c = r, c
                    max_r, max_c = dfs(r, c)
                    if max_r != -1 and max_c != -1:
                        result.append([min_r, min_c, max_r, max_c])

        return result