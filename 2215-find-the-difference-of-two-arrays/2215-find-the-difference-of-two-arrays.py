class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1=[]
        l2=[]
        for k in nums1:
            if k not in nums2 and k not in l1:
                l1.append(k)
        for k in nums2:
            if k not in nums1 and k not in l2:
                l2.append(k)
        return [l1,l2]