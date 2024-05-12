class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = 2  
        for i in range(2, len(nums)):
            if nums[i] != nums[index - 2]:  
                nums[index] = nums[i]
                index += 1    
        return index