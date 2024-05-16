class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None  # Or raise an exception
        if root.val == 0:
            root.val = False
        elif root.val == 1:
            root.val = True

        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)

        if root.val == 2:
            root.val = left_val or right_val
        elif root.val == 3:
            root.val = left_val and right_val

        return root.val