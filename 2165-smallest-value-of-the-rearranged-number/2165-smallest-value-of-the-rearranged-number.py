class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        res=''
        zero=''
        for i in str(num):
            if i!='-':
                if i=='0':
                    zero+=i
                else:
                    res+=i
        res=''.join(sorted(res))
        if num<0:
            return -1* int(res[::-1]+zero)
        return int(res[0]+zero+res[1:])