class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)

        for n in nums:
            if (n - 1) not in numSet:
                cnt = 0
                while (n + cnt) in numSet:
                    cnt += 1
                
                res = max(cnt, res)

            

        return res
        