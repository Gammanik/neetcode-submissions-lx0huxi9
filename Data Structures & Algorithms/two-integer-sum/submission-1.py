class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # idx = map()

        # for i in range(0, len(nums) - 1):
        #     idx[i] = nums
        i = 0
        j = 0

        for el in nums:
            try:
                i = nums.index(target - el)
                j = nums.index(el, i + 1)
            except ValueError:
                pass

        return [i, j]
        