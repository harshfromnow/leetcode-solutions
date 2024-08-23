class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res=0
        countOne=0
        for k in s:
            if k=='1':
                countOne+=1
            else:
                res=min(res+1,countOne)
        return res