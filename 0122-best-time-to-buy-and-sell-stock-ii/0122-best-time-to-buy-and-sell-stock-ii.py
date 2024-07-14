class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        for k in range(len(prices)-1):
            if prices[k+1]>prices[k]:
                maxp+=prices[k+1]-prices[k]
        return maxp