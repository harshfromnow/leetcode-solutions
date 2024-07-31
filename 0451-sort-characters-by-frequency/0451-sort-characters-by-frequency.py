class Solution:
    def frequencySort(self, s: str) -> str:
        m=Counter(s)
        l=''
        print(m)
        d=dict(sorted(m.items(), key=lambda item: item[1]))
        for k in d:
            print(k,d[k])
            l+=k*d[k]
        return l[::-1]
