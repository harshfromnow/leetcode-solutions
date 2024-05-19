class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        res = []
        for k in range(m):
            beg = l[k]
            end = r[k]
            sub = nums[beg:end + 1]  
            sub.sort()
            diff = sub[1] - sub[0]  
            flag = True
            for j in range(1, len(sub)):
                if sub[j] - sub[j - 1] != diff:  
                    res.append(False)
                    flag = False
                    break
            if flag:
                res.append(True)
        return res