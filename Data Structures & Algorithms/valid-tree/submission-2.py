class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return len(edges) == 0
        if len(edges) != n-1:
            return False

        visited = set()


        mp = {}
        for e in edges:
            if not mp.get(e[0]):
                mp[e[0]] = set()
            mp[e[0]].add(e[1])

            if not mp.get(e[1]):
                mp[e[1]] = set()
            mp[e[1]].add(e[0])



        def dfs(prev, curr):
            if curr in visited:
                return False

            visited.add(curr)

            for nd in mp.get(curr, []):
                if nd != prev:
                    if not dfs(curr, nd):
                        return False
            return True

        
        if not dfs(-1, edges[0][0]):
            return False
        # print(mp)
        return len(visited) == n