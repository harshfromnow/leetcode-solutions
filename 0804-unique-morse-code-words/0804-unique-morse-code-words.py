class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        n=len(words)
        if n==1:
            return 1
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for k in range(len(words)):
            s=''
            for letter in words[k]:
                s+=l[ord(letter)-97]
            words[k]=s
        print(words)
        lst=list(set(words))
        return len(lst)