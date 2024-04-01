class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1=int(a,2)
        num2=int(b,2)
        sumn=num1+num2
        out=bin(sumn)
        return out[2:]