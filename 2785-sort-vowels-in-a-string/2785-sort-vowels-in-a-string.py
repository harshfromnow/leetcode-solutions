class Solution:
    def sortVowels(self, s: str) -> str:
        l=[]
        sr=''
        for k in s:
            if k in 'aeiouAEIOU':
                l.append(k)
        l.sort(reverse=True)
        for k in range(len(s)):
            if s[k] in 'aeiouAEIOU':
                sr+=l.pop()
            else:
                sr+=s[k]
        return sr
        