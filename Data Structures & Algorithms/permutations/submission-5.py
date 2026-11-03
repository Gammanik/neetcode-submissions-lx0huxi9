class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        used = set()

        def dfs():
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for k in range(0, len(nums)):
                el = nums[k]
                if el not in used:
                    used.add(el)
                    curr.append(el)
                    dfs()
                    curr.pop()
                    used.remove(el)

        dfs()
        return res