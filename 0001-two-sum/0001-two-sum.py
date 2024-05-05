class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for k in range(len(nums)):
            t=target-nums[k]
            for j in range(k+1,len(nums)):
                if t==nums[j]:
                    return [k,j]
        