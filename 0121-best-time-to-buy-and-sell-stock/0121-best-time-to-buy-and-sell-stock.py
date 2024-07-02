class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        mip=float('inf')
        maxp=0
        for price in prices:
            if price<mip:
                mip=price
            elif price - mip> maxp:
                maxp=price - mip
        return maxp