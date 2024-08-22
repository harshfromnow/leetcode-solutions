class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre={0:1}
        currsum=0
        res=0
        for n in nums:
            currsum+=n
            diff=currsum-k
            res+=pre.get(diff,0)
            pre[currsum]=1+pre.get(currsum,0)
        return res
