class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t=['']*len(s)
        i=0
        for k in indices:
            t[k]=s[i]
            i+=1
        s=''
        for k in t:
            s+=k
        return s