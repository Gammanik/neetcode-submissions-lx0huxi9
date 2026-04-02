class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = { i: set() for i in range(n) }
        for a, b in edges:
            mp[a].add(b)
        for a, b in edges:
            mp[b].add(a)
        print(mp)

        unvisited, visiting, visited = 0, 1, 2
        statuses = [ unvisited for _ in range(n) ]

        def dfs(node):
            if statuses[node] == visited:
                return False

            if statuses[node] == visiting:
                return False

            statuses[node] = visiting
            for child in mp[node]:
                dfs(child)
            statuses[node] = visited
            return True

        cnt = 0
        for node in mp:
            if dfs(node):
                cnt += 1

        return cnt
        