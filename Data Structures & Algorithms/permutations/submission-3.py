class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i: int):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for j in range(0,len(nums)):
                el = nums[j]
                if el not in curr:
                    curr.append(el)
                    dfs(i+1)
                    curr.pop()

        dfs(0)
        return res