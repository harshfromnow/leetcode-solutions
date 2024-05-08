class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ts = sum(nums)
        ls= 0

        for i in range(len(nums)):
            if ls== ts - ls - nums[i]:
                return i
            ls += nums[i]
        return -1