class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #sl[0]=0
        t=len(nums)
        sl=[0]*t
        sr=[0]*t
        suml=0
        for i in range(t):
            sumr=0
            if i-1>-1:
                suml+=nums[i-1]
            for j in range(i+1,t):
                sumr+=nums[j]
            sr[i]=sumr
            sl[i]=suml
        print(sl)
        for i in range(t):
            if sl[i]==sr[i]:
                return i
        return -1