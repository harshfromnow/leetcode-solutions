class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap={}
        l=[]
        for i in nums:
            if i not in numMap:
                numMap[i]=1
            else:
                numMap[i]+=1
        numMap = dict(sorted(numMap.items(), key=lambda x: x[1], reverse=True))
        l=[i for i in numMap]
        return l[:k]


