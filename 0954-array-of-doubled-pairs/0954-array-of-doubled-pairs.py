class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        
        # Sort by absolute value to handle both positive and negative numbers correctly
        for num in sorted(arr, key=abs):
            if count[num] == 0:
                continue  # If the current num is already paired, skip it
            
            if count[2 * num] == 0:
                return False  # Can't find a pair for num
            
            # Pair the current num with 2 * num
            count[num] -= 1
            count[2 * num] -= 1
        
        return True