class Solution:
    def hammingWeight(self, n: int) -> int:
        i=bin(n)
        i=str(i)
        return i.count("1")