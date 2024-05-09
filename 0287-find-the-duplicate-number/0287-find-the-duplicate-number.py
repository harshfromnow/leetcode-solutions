class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for k in range(len(nums)):
            if nums[k+1]==nums[k]:
                return nums[k]