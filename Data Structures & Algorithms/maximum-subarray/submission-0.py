class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,r = 0,0
        curr_sum, max_sum = -1001, -1001

        while r < len(nums):
            curr_sum = nums[r] if curr_sum == -1001 else curr_sum + nums[r]
            # curr_sum += nums[r]
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                l = r
                curr_sum = 0

            r += 1

        return max_sum