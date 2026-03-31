# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        s1 = self.find(p, root, [])
        s2 = self.find(q, root, [])

        print([x.val for x in s1], [x.val for x in s2])
        for i in s1:
            for j in s2:
                if i.val == j.val:
                    return i

        return []

    def find(self, f: TreeNode, root: TreeNode, way: List[TreeNode]) -> List[TreeNode]:
        if root.val == f.val:
            return [root] + way

        if root.val > f.val:
            return self.find(f, root.left, [root] + way)
        if root.val < f.val:
            return self.find(f, root.right, [root] + way)    


