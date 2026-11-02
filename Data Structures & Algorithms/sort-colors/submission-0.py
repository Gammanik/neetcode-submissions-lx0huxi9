class Solution:
    def sortColors(self, nums: List[int]) -> None:
        mp = { 0: 0, 1: 0, 2: 0}

        for c in nums:
            mp[c] += 1
        
        for i in range(len(nums)):
            if i < mp[0]:
                nums[i] = 0
            if i >= mp[0] and i < mp[0] + mp[1]:
                nums[i] = 1
            if i >= mp[0] + mp[1]:
                nums[i] = 2