class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def two_sum_recursive(left, right):
            if left >= right:
                return []
            sum_val = numbers[left] + numbers[right]
            if sum_val == target:
                return [left + 1, right + 1]
            elif sum_val < target:
                return two_sum_recursive(left + 1, right)
            else:
                return two_sum_recursive(left, right - 1)
        return two_sum_recursive(0, len(numbers) - 1)