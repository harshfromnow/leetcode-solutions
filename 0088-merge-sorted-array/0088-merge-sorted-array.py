class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for k in range(len(nums1)):
            if nums1[k]==0 and nums2:
                nums1[k]=nums2.pop()
        return nums1.sort()       