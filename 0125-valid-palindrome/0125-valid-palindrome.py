class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for i in range(len(s)):
            if s[i]==" " or  s[i]=="," or s[i]==":" or s[i]==".":
                continue
            elif "A" <= s[i] <="Z":
                arr.append(chr(ord(s[i])+32))
            elif "a" <= s[i] <= "z":
                arr.append(s[i])
            elif "0" <= s[i] <= "9":
                arr.append(s[i])
        print(arr)
        if arr==arr[::-1]:
            return True
        else:
            return False