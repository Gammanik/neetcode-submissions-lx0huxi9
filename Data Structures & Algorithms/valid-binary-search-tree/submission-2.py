# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(curr, mn, mx):
            if not curr:
                return True
            
            if curr.val <= mn or curr.val >= mx:
                return False

            return check(curr.left, mn, min(curr.val, mx)) and check(curr.right, max(curr.val, mn), mx)

        return check(root.left, -1001, root.val) and check(root.right, root.val, 1001)
        