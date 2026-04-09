class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, n in enumerate(nums[:]):
            if n != val:
                k += 1
            if n == val:
                nums.pop(k)

        return k