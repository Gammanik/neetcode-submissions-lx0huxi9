class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        
        def dfs(i: int):
            if i > len(nums):
                return

            res.append(curr.copy()) 
            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j+1)
                curr.pop()

        dfs(0)
        return res