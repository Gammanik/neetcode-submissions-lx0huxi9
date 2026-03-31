class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt_max = 0
        s = set(nums)

        for n in nums:
            s.add(n)
            cnt = 0
            var = n
            while var in s:
                var += 1
                cnt += 1
            
            if cnt > cnt_max:
                cnt_max = cnt

            

        return cnt_max
        