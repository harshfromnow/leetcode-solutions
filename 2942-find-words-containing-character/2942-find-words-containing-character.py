class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=[]
        for k in range(len(words)):
            if x in words[k]:
                l.append(k)
        return l