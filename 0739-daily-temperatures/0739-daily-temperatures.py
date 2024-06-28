class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=[]
        for k in range(len(temperatures)-1):
            j=k+1
            c=1
            while (temperatures[j]<=temperatures[k] and j<len(temperatures)-1):
                c+=1
                j+=1
            if temperatures[k] == max(temperatures[k:]):
                l.append(0)
            else:
                l.append(c)
        l.append(0)
        return l