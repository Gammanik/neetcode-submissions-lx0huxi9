class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ss = self.subsets(nums)

        sm = 0
        for s in ss:
            local_s = 0
            for s1 in s:
                local_s = local_s ^ s1
            sm += local_s

        return sm

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, sub):
            print(i, sub)
            if i >= len(nums):
                res.append(sub)
                return

            dfs(i+1, sub)
            dfs(i+1, sub + [nums[i]])
        
        dfs(0, [])
        return res