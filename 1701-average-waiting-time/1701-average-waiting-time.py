class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        no=len(customers)
        wt=[]
        prev=[0]*no
        ft=customers[0][0]
        for k in range(no):
            if customers[k][0]>ft:
                ft=customers[k][0]
            ft+=customers[k][1]
            wt.append(ft-customers[k][0])
        return sum(wt)/no