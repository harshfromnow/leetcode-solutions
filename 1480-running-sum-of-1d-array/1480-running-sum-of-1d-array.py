class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        l=[]
        for k in nums:
            sum+=k
            l.append(sum)
        return l