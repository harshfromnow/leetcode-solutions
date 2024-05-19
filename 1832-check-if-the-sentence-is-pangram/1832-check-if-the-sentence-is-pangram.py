class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count=Counter(sentence)
        if 'qwertyuiopasdfghjklzxcvbnm' in sentence:
            return True
        c=0
        print(count)
        for k in count:
            c+=1
            if count[k]<1:
                return False
        if c>=26:
            return True
