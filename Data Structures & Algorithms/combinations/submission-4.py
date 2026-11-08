class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i: int):
            if i > n:
                if len(curr) == k:
                    res.append(curr[:])
                return

            curr.append(i)
            dfs(i+1)
            curr.pop()
            dfs(i+1)   

        dfs(1)
        return res