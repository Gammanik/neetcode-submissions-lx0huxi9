class Solution:
    def canJump(self, nums: List[int]) -> bool:

        i, goal = len(nums) - 1, len(nums) - 1
        while i >= 0:
            print(i, nums[i], goal)
            if i + nums[i] >= goal:
                goal = i
            i -= 1

        return goal == 0
        