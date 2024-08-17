class Solution:
    def splitMessage(self, msg: str, lim: int) -> List[str]:
        def sz(n):
            return len(str(n))

        p = a = 1     

        while p * (sz(p) + 3) + a + len(msg) > p * lim:  
            if 3 + sz(p) * 2 >= lim : return []         
            p += 1                                       
            a += sz(p) 

        parts = []       

        for i in range(1,p+1):
            j = lim - (sz(p)+sz(i)+3)                       
            part, msg = msg[0:j], msg[j:]                  
            parts.append(f"{part}<{i}/{p}>")                 
        return parts
        