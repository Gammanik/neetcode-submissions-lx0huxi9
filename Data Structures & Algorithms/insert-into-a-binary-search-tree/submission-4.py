# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insert(rt: Optional[TreeNode]):
            if not rt:
                root = TreeNode(val)
                return

            if val > rt.val:
                if not rt.right:
                    rt.right = TreeNode(val)
                    return

                insert(rt.right)
            elif val < rt.val:
                if not rt.left:
                    rt.left = TreeNode(val)
                    return

                insert(rt.left)
        
        insert(root)
        return root if root else TreeNode(val)