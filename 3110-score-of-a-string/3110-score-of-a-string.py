class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        for k in range(len(s)-1):
            sum+=abs(ord(s[k])-ord(s[k+1]))
        return sum
        