class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[-1]*len(nums1)
        for num in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[num]==nums2[j]:
                    for i in range(j+1,len(nums2)):
                        if nums2[i]>nums1[num]:
                            l[num]=nums2[i]
                            break
        return l
                