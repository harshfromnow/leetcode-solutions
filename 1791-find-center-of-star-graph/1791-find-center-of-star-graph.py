class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        m=edges[0][0]
        n=edges[0][1]
        for k in edges:
            if m in k:
                continue
            else:
                return n
        return m
