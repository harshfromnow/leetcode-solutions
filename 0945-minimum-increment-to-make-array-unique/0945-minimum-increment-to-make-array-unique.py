class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array
        c = 0  # Count of increments
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                c += increment
        return c
