class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxnum = max(candies)
        l = [candy + extraCandies >= maxnum for candy in candies]
        return l
