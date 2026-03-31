"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(nd):
            if nd in visited:
                return visited[nd]

            print(nd.val, len(nd.neighbors))

            nd_copy = Node(nd.val)
            visited[nd] = nd_copy

            for n in nd.neighbors:
                nd_copy.neighbors.append(dfs(n))

            return nd_copy
            
        return dfs(node) if node else None