class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = [0] * k
        m = {}

        for it in logs:
            m.setdefault(it[0], set()).add(it[1])

        for value in m.values():
            uam[len(value) - 1] += 1

        return uam