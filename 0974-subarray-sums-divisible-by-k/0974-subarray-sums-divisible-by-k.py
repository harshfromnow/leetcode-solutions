class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currsum = 0
        prefixsum = {0: 1}  # Start with 0:1 because a sum of 0 is considered divisible by k
        count = 0

        for num in nums:
            currsum += num  # Calculate cumulative sum
            remainder = currsum % k  # Calculate the remainder
            
            if remainder < 0:  # Adjust for negative remainder
                remainder += k
            
            # If the remainder has been seen before, add the count of its occurrences to result
            count += prefixsum.get(remainder, 0)
            
            # Increment the count of this remainder in the map
            prefixsum[remainder] = prefixsum.get(remainder, 0) + 1
            
        return count