class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        arr = []
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        sorted_items = sorted(d.items(), key=lambda x: (x[1], -x[0]))
        for num, freq in sorted_items:
            arr.extend([num] * freq)
        return arr