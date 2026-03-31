class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 0

        for el in nums:
            try:
                i = nums.index(target - el)
                j = nums.index(el, i + 1)
            except ValueError:
                pass

        return [i, j]
        