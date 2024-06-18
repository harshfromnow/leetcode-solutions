class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        flag=1
        for word in words:
            for j in word:
                if j not in allowed:
                    flag=0
            if flag==1:
                c+=1
            flag=1
        return c