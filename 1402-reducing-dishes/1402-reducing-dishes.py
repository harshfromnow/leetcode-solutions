class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        s,res=0,0
        for dish in satisfaction:
            s+=dish
            if s<0:
                break
            res+=s
        return res