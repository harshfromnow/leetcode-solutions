class Solution:
    def longestPalindrome(self, s: str) -> int:
        m={}
        for k in s:
            if k not in m:
                m[k]=1
            else:
                m[k]+=1
        c=0
        l=0
        for k in m:
            if c==0 and m[k]==1:
                l+=1
                c=1
            if m[k]%2==0:
                l+=m[k]
        return l