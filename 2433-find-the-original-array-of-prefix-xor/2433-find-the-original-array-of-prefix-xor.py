class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        l=[]
        l.append(pref[0])
        for k in range(len(pref)-1):
            l.append(pref[k]^pref[k+1])
        return l
