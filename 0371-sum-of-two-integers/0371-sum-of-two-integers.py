class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # Mask to get 32 bits integer
        MASK = 0xFFFFFFFF
        
        while b != 0:
            # ^ gets different bits and & gets double 1s, << moves carry
            c = (a & b) << 1
            a = (a ^ b) & MASK
            b = c & MASK
        
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ MASK)
