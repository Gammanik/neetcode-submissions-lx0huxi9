class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i: int):
            if i > n+1:
                return

            # print(curr)
            if len(curr) == k:
                res.append(curr.copy())

            for j in range(i,n+1):
                curr.append(j)
                dfs(j+1)
                curr.pop()

        dfs(1)
        return res