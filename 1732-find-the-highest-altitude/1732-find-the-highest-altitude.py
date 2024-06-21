class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=[0]*(len(gain)+1)
        alt[1]=gain[0]
        for k in range(1,len(gain)):
            alt[k+1]=gain[k]+alt[k]
        return max(alt)