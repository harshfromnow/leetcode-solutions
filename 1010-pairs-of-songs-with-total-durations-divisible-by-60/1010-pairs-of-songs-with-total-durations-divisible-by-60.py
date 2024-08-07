class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c=0
        n=len(time)
        for k in range(n):
            for j in range(k+1,n):
                if (time[k] + time[j])%60==0:
                    c+=1
        return c