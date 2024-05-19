class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        for k in nums:
            if k not in d:
                d[k]=1
            else:
                d[k]+=1
        tup=sorted(d.items())
        sd=dict(tup)
        s=0
        cd={}
        for key in sd:
            sup=0
            s+=sd[key]
            sup+=s
            sup-=sd[key]
            cd[key]=sup
        print(cd)
        for k in nums:
            l.append(cd[k])
        return l