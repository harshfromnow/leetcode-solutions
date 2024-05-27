class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        c=0
        for k in range(len(nums)):
            if nums[k]>=c:
                c+=1
        if c<=nums[c-1]:
            return c
        return -1
    