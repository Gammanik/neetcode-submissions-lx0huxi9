"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(rt: 'Node'):
            if not rt:
                return

            for ch in rt.children:
                dfs(ch)

            res.append(rt.val)

        dfs(root)
        return res
            
        