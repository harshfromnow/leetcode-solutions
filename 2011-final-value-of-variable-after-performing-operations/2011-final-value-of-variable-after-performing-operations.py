class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X=0
        for k in operations:
            if k[0]=='-' or k[2]=='-':
                X-=1
            elif k[0]=='+' or k[2]=='+':
                X+=1
        return X