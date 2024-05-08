class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d={}
        l=[0]*len(score)
        for k in range(len(score)):
            d[score[k]]=k
        ld=sorted(d.keys(),reverse=True)
        sdict = {i: d[i] for i in ld}
        j=1
        for k in sdict:
            if j==1:
                l[sdict[k]]="Gold Medal"
                j+=1
            elif j==2:
                l[sdict[k]]="Silver Medal"
                j+=1
            elif j==3:
                l[sdict[k]]="Bronze Medal"
                j+=1
            else:
                l[sdict[k]]=str(j)
                j+=1
        return l
