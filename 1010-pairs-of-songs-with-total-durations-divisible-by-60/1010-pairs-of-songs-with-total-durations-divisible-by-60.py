class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c=0
        n=len(time)
        remc={}
        for t in time:
            rem=t%60
            com=(60-rem)%60
            if com in remc:
                c+=remc[com]
            if rem in remc:
                remc[rem]+=1
            else:
                remc[rem]=1
        return c