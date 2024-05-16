# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2==0:
            return []
        d={}
        def loop(n):
            if n in d:
                return d[n]
            l=[]
            if n==1:
                l.append(TreeNode(0))
            else:
                for i in range(1,n-1,2):
                    ltt=loop(i)
                    rtt=loop(n-i-1)
                    for lt in ltt:
                        for rt in rtt:
                            l.append(TreeNode(0,lt,rt))
            d[n]=l
            return l
        return loop(n)
           
