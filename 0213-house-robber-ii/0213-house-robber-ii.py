class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        def rob_linear(nums):
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]
            if n > 1:
                dp[1] = max(nums[0], nums[1])
            for k in range(2, n):
                dp[k] = max(dp[k-1], nums[k] + dp[k-2])
            return dp[-1]
        max1 = rob_linear(nums[:-1])
        max2 = rob_linear(nums[1:])     
        return max(max1, max2)