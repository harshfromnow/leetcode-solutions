# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, root: Optional[TreeNode], l=[]):
        if root is None:
            return l
        l.append(root.val)
        self.preorder(root.left, l)
        self.preorder(root.right, l)
        return l

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            return root
        left_result = self.searchBST(root.left, val)
        if left_result:
            return left_result
        return self.searchBST(root.right, val)
