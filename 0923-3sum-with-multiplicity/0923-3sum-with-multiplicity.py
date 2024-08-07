class Solution:
    def threeSumMulti(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(nums)
        keys = sorted(count)
        n = len(keys)
        c = 0
        
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, n - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else:
                    if i < j < k:
                        c += count[x] * count[y] * count[z]
                    elif i == j < k:
                        c += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k:
                        c += count[x] * count[y] * (count[y] - 1) // 2
                    else:  # i == j == k
                        c += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                    c %= MOD
                    j += 1
                    k -= 1
        return c