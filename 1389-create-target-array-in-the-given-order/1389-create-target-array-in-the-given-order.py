class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n=len(nums)
        target=[-1]*n
        c=0
        for k in index:
            if target[k]==-1:
                target[k]=nums[c]
            else:
                target[k+1:]=target[k:]
                target[k]=nums[c]
            c+=1
        return target[:n]