class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set('qwertyuiop')
        s2 = set('asdfghjkl')
        s3 = set('zxcvbnm')
        
        rows = [s1, s2, s3]
        result = []

        for word in words:
            lower_word = word.lower()
            for row in rows:
                if lower_word[0] in row:
                    if all(char in row for char in lower_word):
                        result.append(word)
                    break
        
        return result