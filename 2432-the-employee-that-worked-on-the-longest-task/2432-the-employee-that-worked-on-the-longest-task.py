class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        l=[]
        prev=0
        for k in range(len(logs)):
            if k>0:
                prev=logs[k-1][1]
            l.append([logs[k][0],logs[k][1]-prev])
        maxn=0
        for k in range(len(l)):
            if l[k][1]>maxn:
                maxn=l[k][1]
        p=[]
        for k in range(len(l)):
            if l[k][1]==maxn:
                p.append(l[k][0])
        return min(p)