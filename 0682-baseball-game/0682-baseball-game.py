class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for k in operations:
            if k.isalpha():
                if k=="C":
                    record.pop()
                elif k=="D":
                    record.append(record[-1]*2)
            elif k=='+':
                record.append(record[-1]+record[-2])
            else:
                record.append(int(k))
        return sum(record)