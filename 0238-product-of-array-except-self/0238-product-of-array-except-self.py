class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        post=[]
        pre.append(nums[0])
        for k in range(1,len(nums)):
            pre.append(pre[k-1]*nums[k])
        p=1
        i=-1
        c=0
        for k in range(len(nums)):
            if nums[k]!=0:
                p*=nums[k]
                post.append(pre[-1]//nums[k])
            else:
                c+=1
                post.append(0)
                i=k
        if c>1:
            p=0
        if i!=-1:
            post[i]=p
        return post