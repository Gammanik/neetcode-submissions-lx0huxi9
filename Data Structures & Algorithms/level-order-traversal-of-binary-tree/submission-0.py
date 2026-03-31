# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        
        def lvl(root: Optional[TreeNode], l: int):
            if not root:
                return

            if not d.get(l):
                d[l] = []

            d[l].append(root.val)

            lvl(root.left, l + 1)
            lvl(root.right, l + 1)

        lvl(root, 0)
        res = []
        for key in sorted(d):
            res.append(d[key])

        return res
        