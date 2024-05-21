class Solution:
    def find(self, nums: List[int], index: int, current: List[int]) -> List[List[int]]:
        if index == len(nums):
            return [current]
        without_current = self.find(nums, index + 1, current)
        with_current = self.find(nums, index + 1, current + [nums[index]])
        return without_current + with_current
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.find(nums, 0, [])