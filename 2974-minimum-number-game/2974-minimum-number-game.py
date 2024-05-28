class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        arr=[]
        while nums:
            al=nums.pop()
            if nums:
                bob=nums.pop()
                arr.append(bob)
            arr.append(al)
        return arr
