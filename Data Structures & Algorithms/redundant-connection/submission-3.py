class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            ra, rb = find(a), find(b)

            if ra == rb:
                return False

            parent[ra] = rb
            return True
                
        for a, b in edges:
            if not union(a,b):
                return [a,b]