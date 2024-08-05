class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        index=len(nums)-1
        currsum=0
        self.memo={}
        return self.dp(nums, target, index, currsum)
    def dp(self, nums, target, index, currsum):
        if (index, currsum) in self.memo:
            return self.memo[(index, currsum)]
        if index < 0 and currsum == target:
            return 1
        if index < 0:
            return 0 
        positive = self.dp(nums, target, index-1, currsum + nums[index])
        negative = self.dp(nums, target, index-1, currsum + -nums[index])
        self.memo[(index, currsum)] = positive + negative
        return positive + negative