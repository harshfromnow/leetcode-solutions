class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        t=len(nums)
        if max(nums)==nums[0]:
            return 0
        if t==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        for k in range(t-2):
            if nums[k+1]>nums[k] and nums[k+2]<nums[k+1]:
                return k+1
        return t-1