class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es=0
        ds=0
        for k in nums:
            es+=k
            while k:
                ds+=k%10
                k=k//10
        return es-ds