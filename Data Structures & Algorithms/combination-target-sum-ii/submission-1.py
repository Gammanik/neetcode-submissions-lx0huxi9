class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)

        def dfs(i: int, res: List[int]):
            print(i, res)
            sm = sum(res)
            
            if sm == target:
                ans.append(res)

            if sm > target or i == len(candidates):
                return
            
            if sm < target:
                newI = i+1
                while newI < len(candidates) and candidates[i] == candidates[newI]:
                    newI += 1
    
                dfs(i+1, res + [candidates[i]])
                dfs(newI, res)


        dfs(0, [])
        return ans