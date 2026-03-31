# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    d = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            r = dfs(node.left)
            l = dfs(node.right)
            self.d = max(self.d, l + r)
            return 1 + max(r, l)

        dfs(root)
        return self.d
        