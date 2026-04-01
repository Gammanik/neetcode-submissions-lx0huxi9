class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m = { i: set() for i in range(numCourses) }
        resolved = set()
        res = []

        for a, b in prerequisites:
            m[a].add(b)
        print(m)

        def dfs(nd, path: set):
            if nd in path:
                return False

            if nd in resolved:
                return True

            preq = m.get(nd)
            if not preq:
                resolved.add(nd)
                res.append(nd)

            for p in preq:
                if not dfs(p, path | {nd}):
                    return False

            resolved.add(nd)
            res.append(nd)
            return True


        for p in m:
            if not dfs(p, set()):
                return []

        return res