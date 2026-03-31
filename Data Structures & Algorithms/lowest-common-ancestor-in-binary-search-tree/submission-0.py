# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # p = 
        s1 = self.find(p, root, [])
        s2 = self.find(q, root, [])

        print([x.val for x in s1], [x.val for x in s2])
        for i in list(reversed(s1)):
            for j in list(reversed(s2)):
                if i.val == j.val:
                    return i

        return []

    def find(self, f: TreeNode, root: TreeNode, way: List[TreeNode]) -> List[TreeNode]:
        # print('f:', f.val, root.val, [x.val for x in way])

        if root.val == f.val:
            return way + [root]

        if root.val > f.val:
            return self.find(f, root.left, way + [root])
        if root.val < f.val:
            return self.find(f, root.right, way + [root])    


