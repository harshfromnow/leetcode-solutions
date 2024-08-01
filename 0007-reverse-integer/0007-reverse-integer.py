class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            s=-1
            t=abs(x)
        else:
            t=x
            s=1
        return s*int(str(t)[::-1])