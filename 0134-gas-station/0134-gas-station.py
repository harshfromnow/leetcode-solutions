class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        totsur=0
        sur=0
        start=0

        for i in range(n):
            totsur+=gas[i]-cost[i]
            sur+=gas[i]-cost[i]
            if sur<0:
                sur=0
                start=i+1
        return -1 if (totsur < 0) else start
