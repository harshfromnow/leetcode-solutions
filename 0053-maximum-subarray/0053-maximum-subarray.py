class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSum=float('-inf')
        currentSum=0
        for num in nums:
            currentSum+= num
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum=0
        return maxSum