class Solution:
    def generateGray(self, n: int):
        if n<=0:
            return ["0"]
        if n==1:
            return ["0","1"]
        rec = self.generateGray(n - 1)
        l=[]
        for i in range(len(rec)):
            s=rec[i]
            l.append("0"+s)
        for i in range(len(rec)-1,-1,-1):
            s=rec[i]
            l.append("1"+s)
        return l

    def grayCode(self, n: int) -> List[int]:
        arr=self.generateGray(n)
        for k in range(len(arr)):
            arr[k]=int(arr[k],2)
        return arr