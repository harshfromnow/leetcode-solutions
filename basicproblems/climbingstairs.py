class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        arr=[0]*(n+1)
        arr[1]=1
        arr[2]=2
        for i in range(3,n+1):
            arr[i]=arr[i-1]+arr[i-2]
        return arr[n]
#climbing 3rd stair= no. of steps for 2nd + 1st
