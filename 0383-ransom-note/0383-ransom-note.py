class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m=Counter(magazine)
        for k in ransomNote:
            if k in m and m[k]>0:
                m[k]-=1
            else:
                return False
        return True

        