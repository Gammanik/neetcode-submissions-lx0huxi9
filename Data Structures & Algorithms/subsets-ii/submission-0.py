class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def dfs(i, sub):
            print(i, sub)
            if i >= len(nums):
                res.append(sub)
                return

            dfs(i+1, sub + [nums[i]])

            new_i = i+1
            while new_i < len(nums) and nums[new_i] == nums[i]:
                new_i += 1 
            
            dfs(new_i, sub)
        
        dfs(0, [])
        return res 