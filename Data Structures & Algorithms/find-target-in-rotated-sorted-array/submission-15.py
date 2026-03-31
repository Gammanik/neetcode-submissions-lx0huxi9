class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_idx = self.findMin(nums)

        nums = nums[min_idx:] + nums[:min_idx]
        print(nums)

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            # print(l,r, m, nums[m], nums[m] > target)

            if nums[m] == target:
                return (min_idx + m) % len(nums)

            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
                
        return -1



        # if nums[0] >= target:
        #     return self.bs(nums[min_idx:], min_idx, target)
        # else:
        #     return self.bs(nums[:min_idx], min_idx, target)

    def bs(self, nums: List[int], min_idx: int, target: int) -> int:
        print(nums)
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            print(l,r, m, nums[m], nums[m] > target)

            if nums[m] == target:
                return min_idx + m

            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
                
        return -1


    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == nums[r]:
                return l

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return l