class Solution:
    def find(self, nums: List[int], index: int, current: List[int], result:List[int]):
        if index == len(nums):
            result.append(current)
            return 

        self.find(nums, index + 1, current + [nums[index]], result)
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        self.find(nums, index + 1, current, result)   

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        self.find(nums, 0, [], result)
        return result