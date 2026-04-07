class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        total = 0
        for i in range(n+1): total += i

        res = 0
        for n in nums:
            res += n

        print(total, res)
        return total - res