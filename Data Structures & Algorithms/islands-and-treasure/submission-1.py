class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])

        def dfs(i,j,ln):
            if i<0 or j<0 or i>=n or j>=m or grid[i][j] == -1 or grid[i][j] < ln:
                return

            print(i,j, ln)

            grid[i][j] = ln
            ln += 1
            dfs(i,j+1,ln)
            dfs(i,j-1,ln)
            dfs(i+1,j,ln)
            dfs(i-1,j,ln)


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    print('=0', i, j)
                    dfs(i,j, 0)
        