class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        c=0
        for k in range(len(words)):
            if words[k][::-1] in words[k+1:]:
                c+=1
        return c