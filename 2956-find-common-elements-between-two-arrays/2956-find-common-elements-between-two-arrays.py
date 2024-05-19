class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=0
        r=0
        for k in nums1:
            if k in nums2:
                l+=1
        for k in nums2:
            if k in nums1:
                r+=1
        return [l,r]