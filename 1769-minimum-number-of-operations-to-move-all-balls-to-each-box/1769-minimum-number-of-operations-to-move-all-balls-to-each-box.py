class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l=[]
        for n in range(len(boxes)):
            s=0
            for k in range(len(boxes)):
                if k!=n and boxes[k]=='1':
                    s+=abs(k-n)
            l.append(s)
        return l