class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        m=Counter(nums)
        s=0
        for k in m:
            if m[k]==1:
                s+=k
        return s