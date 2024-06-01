class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        m=[]
        l=[0]*n
        for k in nums:
            if not l[k-1]:
                l[k-1]=k
            else:
                m.append(k)
        return m
