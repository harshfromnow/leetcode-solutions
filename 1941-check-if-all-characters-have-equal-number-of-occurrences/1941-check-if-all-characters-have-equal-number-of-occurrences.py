class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for k in s:
            if k not in d:
                d[k]=0
            else:
                d[k]+=1
        j=d[s[0]]
        for i in d.values():
            if i!=j:
                return False
        return True