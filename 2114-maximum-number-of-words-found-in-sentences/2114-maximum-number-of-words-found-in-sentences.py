class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=[]
        for k in sentences:
            l=k.split()
            c.append(len(l))
        return max(c)