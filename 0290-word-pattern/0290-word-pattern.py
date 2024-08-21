class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=s.split()
        if len(pattern)!=len(l):
            return False
        m={}
        for k in range(len(pattern)):
            if pattern[k] not in m:
                m[pattern[k]]=[k]
            else:
                m[pattern[k]].append(k)
        print(m)
        ma={}
        for k in range(len(l)):
            if l[k] not in ma:
                ma[l[k]]=[k]
            else:
                ma[l[k]].append(k) 
        t=ma.values()
        check=m.values()
        for j in t:
            if j not in check:
                return False
        return True