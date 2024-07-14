class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        k=0
        while k<len(prices)-1:
            if prices[k+1]>prices[k]:
                maxp+=prices[k+1]-prices[k]
                if k!=len(prices):
                    k+=1
            k+=1
        return maxp