class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        for k in stones:
            if k in jewels:
                c+=1
        return c