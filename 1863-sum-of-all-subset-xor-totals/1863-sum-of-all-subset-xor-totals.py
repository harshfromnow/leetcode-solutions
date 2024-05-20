class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.loop(nums, 0, 0)

    def loop(self, nums: List[int], index: int, currentXor: int) -> int:
        if index == len(nums):
            return currentXor
        
        include = self.loop(nums, index + 1, currentXor ^ nums[index])
        exclude = self.loop(nums, index + 1, currentXor)
        
        return include + exclude