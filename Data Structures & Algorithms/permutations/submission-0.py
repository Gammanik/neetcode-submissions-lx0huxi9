class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i, res):
            print(i, res)
            if i >= len(nums):
                ans.append(res)
                return

            if len(res) == 0 and i == 0:
                return dfs(1, [nums[0]])

            for j in range(len(res)+1):
                    dfs(i+1, res[:j] + [nums[i]] + res[j:])

        dfs(0, [])
        return ans