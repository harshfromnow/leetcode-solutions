from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        words = sentence.split()
        dict_set = set(dictionary)
        def find_root(word):
            for i in range(1, len(word) + 1):
                if word[:i] in dict_set:
                    return word[:i]
            return word
 
        replaced_words = [find_root(word) for word in words]
 
        return ' '.join(replaced_words)