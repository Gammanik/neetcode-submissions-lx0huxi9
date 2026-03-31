class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                return abs(nums[i])

            nums[idx] *= -1

        # sm, mx = 0, 0
        # for el in nums:
        #     sm += el
        #     mx = max(el, mx)
        
        # n = len(nums)
        # repeats = n - mx + 1
        # ideal_sum = (n * (n + 1)) / 2
        # print(repeats, sm, ideal_sum)
        # return 0