from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min=0
        l=[]
        final=[]
        for row in points:
            sum=row[0]**2 + row[1]**2
            dist=sqrt(sum)
            l.append([dist,row])
        l.sort()
        print(l)
        for i in range(k):
            final.append(l[i][1])
        return final