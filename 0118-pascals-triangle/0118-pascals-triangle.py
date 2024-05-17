class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]
        if numRows==1:
            return l
        elif numRows==2:
            l.append([1,1])
            return l
        else:
            l.append([1,1])
            for k in range(2,numRows):
                row=[1]
                prev=l[k-1]
                for i in range(1,len(prev)):
                    row.append(prev[i-1]+prev[i])
                row.append(1)
                l.append(row)
            return l

        