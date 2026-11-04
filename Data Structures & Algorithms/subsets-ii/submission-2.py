class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        nums = sorted(nums)

        def dfs(i):
            if i >= len(nums):
                res.append(curr[:])
                return

            curr.append(nums[i])
            dfs(i+1)
            curr.pop()

            new_i = i+1
            while new_i < len(nums) and nums[new_i] == nums[i]:
                new_i += 1 
            
            dfs(new_i)
        
        dfs(0)
        return res 