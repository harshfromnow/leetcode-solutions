class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        m=Counter(nums)
        l=[]
        for k in m:
            if m[k]==1:
                l.append(k)
        return l
