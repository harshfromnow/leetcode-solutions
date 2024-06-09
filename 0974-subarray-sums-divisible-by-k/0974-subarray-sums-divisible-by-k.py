class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        count = 0

        for num in nums:
            prefix_sum += num
            modulus = prefix_sum % k

            if modulus < 0:
                modulus += k

            if modulus in prefix_counts:
                count += prefix_counts[modulus]

            prefix_counts[modulus] += 1

        return count