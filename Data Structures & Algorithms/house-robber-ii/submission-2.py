class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob1(nums):
            cache = [-1 for _ in range(len(nums))]

            def dfs(i):
                if i >= len(nums):
                    return 0

                if cache[i] == -1:
                    cache[i] = max(nums[i]+dfs(i+2), dfs(i+1))

                return cache[i]

            return dfs(0)

        if len(nums) == 1:
            return nums[0]

        return max(rob1(nums[:len(nums)-1]), rob1(nums[1:]))