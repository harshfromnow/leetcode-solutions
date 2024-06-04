class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=set()
        l=0
        for k in s:
            if k in c:
                c.remove(k)
                l+=2
            else:
                c.add(k)
        if c:
            l+=1
        return l