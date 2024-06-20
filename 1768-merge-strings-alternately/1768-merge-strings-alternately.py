class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=''
        one=len(word1)
        two=len(word2)
        for k in range(one):
            s+=word1[k]
            if k<two:
                s+=word2[k]
        if two>one:
            s+=word2[one:]
        return s
        
        

        