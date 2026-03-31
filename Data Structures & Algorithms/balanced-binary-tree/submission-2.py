# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    isBal = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            r = maxDepth(root.left)
            l = maxDepth(root.right)

            if abs(r - l) > 1:
                self.isBal = False

            return 1 + max(r, l)

        maxDepth(root)
        
        return self.isBal