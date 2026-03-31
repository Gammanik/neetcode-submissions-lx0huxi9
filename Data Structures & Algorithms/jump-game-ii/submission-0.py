class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        steps = 0

        while r < len(nums) - 1:
            farthest = 0
            print(':',l, r)
            for i in range(l,r+1):
                farthest = max(i + nums[i], farthest)
                print(farthest)

            l = r + 1
            r = farthest
            steps += 1

        return steps