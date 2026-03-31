class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, sub):
            # print(i, sub)
            if i >= len(nums):
                res.append(sub)
                return

            dfs(i+1, sub)
            dfs(i+1, sub + [nums[i]])
        
        dfs(0, [])
        return res