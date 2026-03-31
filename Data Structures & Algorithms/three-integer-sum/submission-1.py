class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        arr = []

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate i

            res = self.twoSum(nums, i)
            arr.extend(res)

        return arr

        
    def twoSum(self, nums: List[int], i: int):
        t = -nums[i]
        l, r = i + 1, len(nums) - 1
        res = []

        while l < r:
            s = nums[l] + nums[r]
            if s == t:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1

                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

            elif s > t:
                r -= 1
            elif s < t:
                l += 1

        return res