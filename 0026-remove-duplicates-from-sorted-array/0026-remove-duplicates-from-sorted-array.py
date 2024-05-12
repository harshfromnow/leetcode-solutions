class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=[]
        for k in range(len(nums)):
            if nums[k] not in l:
                l.append(nums[k])
            else:
                nums[k]=9999
        nums.sort()
        return len(l)