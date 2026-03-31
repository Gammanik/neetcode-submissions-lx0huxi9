# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        r = self.maxDepth(root.left)
        l = self.maxDepth(root.right)

        return 1 + max(r, l)

        # def ln(num: int, root: Optional[TreeNode]) -> int:
        #     if not root:
        #         return num - 1

        #     ml = ln(num + 1, root.left)
        #     mr = ln(num + 1, root.right)

        #     return max(ml, mr)


        # return ln(1, root)



        