class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        l = 1
        r = int(1e9)

        def isPossible(m: int) -> bool:
            for machine in composition:
                requiredMoney = 0
                for j in range(n):
                    requiredUnits = max(0, machine[j] * m - stock[j])
                    requiredMoney += requiredUnits * cost[j]
                if requiredMoney <= budget:
                    return True
            return False

        while l < r:
            m = (l + r) // 2
            if isPossible(m):
                l = m + 1
            else:
                r = m
        return l - 1
