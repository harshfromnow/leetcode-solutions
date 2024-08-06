class Solution:
    def minimumPushes(self, word: str) -> int:
        m=Counter(word)
        d=dict(sorted(m.items(), key=lambda item:item[1], reverse=True))
        print(m)
        c=0
        mul=1
        op=0
        for k in d:
            if c!=0 and c%8==0:
                mul=c//8+1
            op+=d[k]*mul
            c+=1
        return op