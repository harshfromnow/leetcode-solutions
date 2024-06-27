class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        tr=''
        for k in range(len(l)-1,0,-1):
            tr+=l[k]+' '
        tr+=l[0]
        return tr