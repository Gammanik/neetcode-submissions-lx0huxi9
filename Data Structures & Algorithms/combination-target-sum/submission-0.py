class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i: int, res: List[int]):
            print(i, res)
            sm = sum(res)

            if i == len(nums):
                return
            
            if sm == target:
                ans.append(res)
            if sm < target:
                dfs(i, res + [nums[i]])
                dfs(i+1, res)



            return

        dfs(0, [])
        return ans