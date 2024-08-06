class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        max_length = 1
        current_length = 1
        for k in range(len(nums)-1):
            if nums[k]==nums[k+1]-1:
                current_length+=1
                max_length=max(max_length,current_length)
            else:
                current_length=1
        return max_length