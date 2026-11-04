class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        used = set()

        def dfs():
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            lvlUsed = set()
            for k in range(0, len(nums)):
                el = nums[k]
                if el not in lvlUsed and k not in used:
                    lvlUsed.add(el)
                    used.add(k)
                    curr.append(el)
                    dfs()
                    used.remove(k)
                    curr.pop()

        dfs()
        return res