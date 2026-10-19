class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0,0
        s = 0
        res = 100001

        while r < len(nums):
            s += nums[r]
            # print(f"({l},{r}) +{nums[r]} {s}")
            while l < r and s - nums[l] >= target:
                s -= nums[l]
                l += 1
                # print(f"({l},{r}) -{nums[l-1]} {s}")

            if s >= target:
                # print(":", l, r, s)
                res = min(res, r - l + 1)

            r += 1
        
        return res if res != 100001 else 0