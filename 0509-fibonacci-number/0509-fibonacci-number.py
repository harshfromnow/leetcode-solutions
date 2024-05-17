class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            prev=0
            curr=1
            sum=0
            for k in range(1,n):
                sum=prev+curr
                prev=curr
                curr=sum
            return sum