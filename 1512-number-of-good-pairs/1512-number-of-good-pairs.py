class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        for k in range(len(nums)):
            for j in range(k+1,len(nums)):
                if nums[k]==nums[j]:
                    c+=1
        return c