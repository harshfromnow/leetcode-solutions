class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        l=[]
        t=len(digits)
        j=0
        for k in range(t-1,-1,-1):
            n+=digits[k]*(10**j)
            j+=1
        n+=1
        n=str(n)
        for k in n:
            l.append(int(k))
        return l
        