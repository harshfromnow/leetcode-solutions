class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def countWhileMerging(prefix_sums, start, end):
            if end - start <= 1:
                return 0
            mid = (start + end) // 2
            count = countWhileMerging(prefix_sums, start, mid) + countWhileMerging(prefix_sums, mid, end)
            
            j = k = mid
            for left in prefix_sums[start:mid]:
                while k < end and prefix_sums[k] - left < lower:
                    k += 1
                while j < end and prefix_sums[j] - left <= upper:
                    j += 1
                count += j - k
            
            # Merge step
            prefix_sums[start:end] = sorted(prefix_sums[start:end])
            return count
        
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        
        return countWhileMerging(prefix_sums, 0, len(prefix_sums))