# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBSTUtil(self, root, left, right) -> bool:
        if root is None:
            return True
        if root.val <= left or root.val >= right:
            return False
        return (self.isBSTUtil(root.left, left, root.val) and
                self.isBSTUtil(root.right, root.val, right))
    def isValidBST(self, root):
        return self.isBSTUtil(root, float('-inf'), float('inf'))