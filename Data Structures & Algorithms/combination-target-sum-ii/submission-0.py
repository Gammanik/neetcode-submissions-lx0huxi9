class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)

        def dfs(i: int, res: List[int]):
            print(i, res)
            sm = sum(res)
            
            if sm == target:
                ans.append(res)

            if i == len(candidates):
                return
            
            if sm < target:
                dfs(i+1, res + [candidates[i]])
                dfs(i+1, res)

            return

        dfs(0, [])
        return [list(t) for t in {tuple(x) for x in ans}]