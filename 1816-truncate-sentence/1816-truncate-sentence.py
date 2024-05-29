class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        c=0
        t=''
        for j in s:
            if j==' ':
                c+=1
            if c==k:
                return t
            t+=j
        return t