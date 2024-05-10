class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=''
        for k in range(len(address)):
            if address[k]=='.':
                s+="[.]"
            else:
                s+=address[k]
        return s
        