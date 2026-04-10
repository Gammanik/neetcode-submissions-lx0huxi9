class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        el = nums[0]

        for n in nums:
            if n == el:
                cnt += 1
            else:
                cnt -= 1

            if cnt <= 0:
                el = n

        return el