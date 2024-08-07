class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        map={}
        n=len(time)
        count=0
        res=[]
        for i in range(n):
            comp = (60-(time[i]%60))%60
            if comp in map:
                count+=map[comp]
            if time[i]%60 in map:
                map[time[i]%60]+=1
            else:
                map[time[i]%60]=1
        return count