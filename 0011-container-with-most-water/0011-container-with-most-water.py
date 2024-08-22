class Solution:
    def maxArea(self, h: List[int]) -> int:
        left, right = 0, len(h) - 1
        max_area = 0
        
        while left < right:
            height = min(h[left], h[right])
            width = right - left
            area = height * width

            max_area = max(max_area, area)

            if h[left] < h[right]:
                left += 1
            else:
                right -= 1
        return max_area