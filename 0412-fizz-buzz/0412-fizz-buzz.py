class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l=[]
        for k in range(1,n+1):
            if (k%3==0):
                if (k%5==0):
                    l.append("FizzBuzz")
                else:
                    l.append("Fizz")
            elif (k%5==0):
                l.append("Buzz")
            else:
                l.append(str(k))
        return l
