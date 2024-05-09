class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        s=0
        happiness.sort(reverse=True)
        for i in range(k):
            s+=max(happiness[i]-i,0)
        return s