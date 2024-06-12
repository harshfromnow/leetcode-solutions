class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for k in operations:
            if k.isalpha():
                if k=="C":
                    record.pop()
                elif k=="D":
                    s=record[-1]*2
                    record.append(s)
            elif k=='+':
                s=record[-1]+record[-2]
                record.append(s)
            else:
                record.append(int(k))
        return sum(record)