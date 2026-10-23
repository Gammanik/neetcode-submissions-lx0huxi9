# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def dl(par: Optional[TreeNode], rt: Optional[TreeNode]):
            if not rt:
                return None

            if rt.val == key:
                if not par:
                    if not rt.right and not rt.left:
                        return TreeNode(-111)

                    if rt.right:
                        l = rt.left
                        rt = rt.right
                        newRt = TreeNode(rt.val, rt.left, rt.right)
                        rt = newRt
                        while rt.left:
                            rt = rt.left
                        
                        rt.left = l
                        return newRt
                    if rt.left:
                        r = rt.right
                        rt = rt.left
                        rt.right = r
                        return rt

                if par.val < rt.val: # right
                    par.right = rt.left
                    if par.right:
                        par.right.right = rt.right
                    else:
                        par.right = rt.right
                elif par.val > rt.val: # left
                    par.left = rt.right
                    if par.left:
                        par.left.left = rt.left
                    else:
                        par.left = rt.left

                if par.val == -999999:
                    return par.right

            if rt.val < key:
                dl(rt, rt.right)
            elif rt.val > key:
                dl(rt, rt.left)

        rt = dl(None, root)
        if rt and rt.val == -111:
            return None
        return rt if rt else root
        