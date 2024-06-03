class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        j=0
        for k in range(len(s)):
            if s[k]==t[j]:
                j+=1
        x=t[j:]
        return len(x)