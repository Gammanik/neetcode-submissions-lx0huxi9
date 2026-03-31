# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        match (p, q):
            case (None, None):
                return True
            case (None, q):
                return False
            case (p, None):
                return False
            case (p, q):
                print(p.val,q.val)
                l = self.isSameTree(p.left, q.left)
                r = self.isSameTree(p.right, q.right)
                return p.val == q.val and r and l
