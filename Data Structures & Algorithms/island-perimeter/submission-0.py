class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        per = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            nonlocal per
            if i < 0 or j < 0 or i >= rows or j >= cols:
                per += 1
                return

            if grid[i][j] == 0:
                per += 1
                return

            if grid[i][j] == 1:
                grid[i][j] = 2

                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i-1, j)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return per

        return 0
