class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {}
        resolved = set()

        for p in prerequisites:
            if not m.get(p[1]):
                m[p[1]] = set()
            
            m[p[1]].add(p[0])


        print(m)
        isFailed = False

        def dfs(nd, path):
            nonlocal resolved, isFailed
            if not m.get(nd):
                resolved.add(nd)
                return

            print(nd, path)
            for preq in m.get(nd):
                print('~', nd, preq, path, preq in path, isFailed)
                if preq in path:
                    isFailed = True
                    return

                if preq not in resolved:
                    dfs(preq, path | {nd})
                    # m[nd].remove(preq)

            resolved.add(nd)

        for nd in m:
            dfs(nd, set())

        return not isFailed