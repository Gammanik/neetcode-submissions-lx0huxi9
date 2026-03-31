# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(rt):
            if not rt:
                return []

            return dfs(rt.left) + [rt.val] + dfs(rt.right)


        res = dfs(root)
        print(res)
        return res[k-1]