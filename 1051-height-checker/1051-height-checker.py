class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=heights.copy()
        expected.sort()
        c=0
        for k in range(len(heights)):
            if heights[k]!=expected[k]:
                c+=1
        return c