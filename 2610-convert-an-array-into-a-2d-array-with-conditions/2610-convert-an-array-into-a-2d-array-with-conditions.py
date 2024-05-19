class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        l=[[]]
        for k in range(len(nums)):
            j=0
            if nums[k] not in l[j]:
                l[j].append(nums[k])
            else:
                while nums[k] in l[j]:
                    j+=1
                    if j >= len(l):
                        l.append([])
                l[j].append(nums[k])
        return l  