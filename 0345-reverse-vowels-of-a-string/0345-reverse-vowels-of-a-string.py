class Solution:
    def reverseVowels(self, s: str) -> str:
        t=''
        for k in s:
            if k in 'aeiouAEIOU':
                t+=k
        t=t[::-1]
        j=0
        l=''
        for k in range(len(s)):
            if s[k] in 'aeiouAEIOU':
                l+=t[j]
                j+=1
            else:
                l+=s[k]
        return l
        