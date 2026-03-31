# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, mx):
            nonlocal res
            if not root:
                return

            new_mx = max(mx, root.val)
            if root.val >= mx:
                res = res + 1

            dfs(root.left, new_mx)
            dfs(root.right, new_mx)

        dfs(root, -101)
        return res

        