class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        t=[]
        pointer=0
        tring=''
        for k in range(n):
            tring+=s[k]
            if tring in wordDict:
                print(tring)
                t.append(tring)
                tring=''
                pointer=k
        if t and pointer==n-1:
            return True
        return False

            