class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        curr = []

        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            usedLvl = set()
            for j in range(len(nums)):
                if j not in used and nums[j] not in usedLvl:
                    usedLvl.add(nums[j])
                    used.add(j)
                    curr.append(nums[j])
                    dfs()
                    curr.pop()
                    used.remove(j)
                        
            usedLvl.clear()
                
        dfs()
        return res