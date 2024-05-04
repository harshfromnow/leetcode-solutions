class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=list(s)
        d=list(t)
        if len(s)!= len(t):
            return False
        for k in l:
            if k in d:
                d.remove(k)
        if d:
            return False
        return True    