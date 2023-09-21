def palindrome(x)
  if x<0:
    return False
  temp=0
  num=x
  while x:
    temp=temp*10+x%10
    x//= 10  
  return num == temp

x=int(input())
