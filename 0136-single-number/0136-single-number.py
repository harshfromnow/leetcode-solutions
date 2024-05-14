class Solution:
    def singleNumber(self, nums):
        count={}
        for k in range(len(nums)):
            if nums[k] not in count:
                count[nums[k]]=1
            else:
                count[nums[k]]+=1
        for k in count:
            if count[k]==1:
                return k