class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for k in range(len(nums)):
            ans.append(nums[nums[k]])
        return ans