class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i: int, curr: List[int]):
            if i > len(nums):
                return

            res.append(curr)
            
            for j in range(i, len(nums)):
                dfs(j+1, curr + [nums[j]])

        dfs(0, [])
        return res