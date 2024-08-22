class Solution:
    def jump(self, nums: List[int]) -> int:
        count=0
        end=0
        farthest=0
        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if farthest >= len(nums)-1:
                count+=1
                break
            if i==end:
                end=farthest
                count+=1
        return count