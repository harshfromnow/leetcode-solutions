class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for k in range(0,n+1):
            s=str(bin(k))
            s.count('1')
            l.append(s.count('1'))
        return l