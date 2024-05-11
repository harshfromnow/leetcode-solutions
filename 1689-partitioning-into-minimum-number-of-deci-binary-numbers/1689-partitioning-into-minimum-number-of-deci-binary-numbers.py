class Solution:
    def minPartitions(self, n: str) -> int:
        max='0'
        for k in n:
            if k>max:
                max=k
        return int(max)

        