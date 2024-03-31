class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=""
        l=[]
        if s=="":
            return 0
        for k in s:
            if k in sub:
                l.append(len(sub))
                for i in range(len(sub)):
                    if k==sub[i]:
                        sub=sub[i+1:]
                        break 
            sub+=k
        l.append(len(sub))
        return max(l)