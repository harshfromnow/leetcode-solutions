class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        even=0
        odd=0
        dp=[0]*n
        dp[0]=nums[0]
        if n<=2:
            return max(nums)
        dp[1]=nums[1]
        for k in range(2,n):
            if k>2:
                dp[k]+=nums[k]+max(dp[k-2],dp[k-3])
            else:
                dp[k]+=nums[k]+dp[k-2]
        return max(dp[n-1],dp[n-2])