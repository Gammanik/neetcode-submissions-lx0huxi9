class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:    
        def dfs(l: int, r: int):
            if l > r:
                return None
            elif l == r:
                return TreeNode(nums[l])

            m = l + (r-l) // 2
            return TreeNode(nums[m], dfs(l,m-1), dfs(m+1,r))

        return dfs(0,len(nums)-1)
