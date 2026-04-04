class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        rank = [0] * n
        parent = [i for i in range(n)]

        def find(x):
            # print(x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            ra, rb = find(a), find(b)

            if ra == rb:
                return False

            if rank[ra] < rank[rb]:
                parent[ra] = rb
            if rank[ra] > rank[rb]:
                parent[rb] = ra
            if rank[ra] == rank[rb]:
                parent[rb] = ra
                rank[ra] += 1

            return True
                
            

        for a, b in edges:
            if not union(a,b):
                return [a,b]