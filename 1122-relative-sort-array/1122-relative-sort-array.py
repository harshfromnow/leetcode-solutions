class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        r=[]
        for k in arr2:
            while k in arr1:
                l.append(k)
                arr1.remove(k)
        if arr1:
            arr1.sort()
            l=l+arr1
        return l