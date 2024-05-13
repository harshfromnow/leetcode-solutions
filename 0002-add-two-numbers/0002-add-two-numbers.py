# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        n2=0
        k=1
        j=1
        head=None
        if l1.val==0 and l2.val==0 and l1.next is None and l2.next is None:
            head=ListNode(0)
            return head
        while(l1!=None):
            n1+=l1.val*k
            k*=10
            l1=l1.next
        while(l2!=None):
            n2+=l2.val*j
            j*=10
            l2=l2.next
        n=n1+n2
        l=None
        while(n):
            digit=n%10
            n//=10
            if l is None:
                l=ListNode(digit)
                head=l
            else:
                l.next=ListNode(digit)
                l=l.next
        return head