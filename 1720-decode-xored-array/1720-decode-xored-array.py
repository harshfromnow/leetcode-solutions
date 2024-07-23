class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l=[first]
        for k in encoded:
            l.append(k^l[-1])
        return l