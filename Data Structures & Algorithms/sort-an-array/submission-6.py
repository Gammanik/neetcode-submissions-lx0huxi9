import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(i, j):
            if i >= j:
                return

            pivot_idx = random.randint(i,j)
            nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]

            cnt, k = 0, i+1
            while k < j-cnt+1:
                if nums[k] >= nums[i]:
                    nums[k], nums[j-cnt] = nums[j-cnt], nums[k]
                    cnt += 1
                    continue
                k += 1

            nums[i], nums[j-cnt] = nums[j-cnt], nums[i]
            partition(i,j-cnt-1)
            partition(j-cnt+1,j)

        partition(0, len(nums)-1)
        return nums