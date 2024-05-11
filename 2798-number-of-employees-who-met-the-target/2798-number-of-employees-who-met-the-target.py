class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count=0
        for k in hours:
            if k>=target:
                count+=1
        return count