class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        i=0
        while 0 in nums :
            if nums[i]==0:
                c+=1
                nums.pop(i)
            else:
                i+=1
        nums.extend([0]*c)
        