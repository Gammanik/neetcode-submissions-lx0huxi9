class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = set()

        def dfs(i: int):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for j in range(0,len(nums)):
                el = nums[j]
                if el not in used:
                    used.add(el)
                    curr.append(el)
                    dfs(i+1)
                    curr.pop()
                    used.remove(el)

        dfs(0)
        return res