class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        c=0
        for k in range(len(nums)):
            if nums[k]+diff in nums[k:]:
                if nums[k]+diff+diff in nums[k+1:]:
                    c+=1
        return c