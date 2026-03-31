class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[0]*m for _ in range(n)]
        area = 0
        max_sum = 0

        def dfs(i, j, sm):
            nonlocal max_sum, area
            if i >= n or j >= m or i < 0 or j < 0 or visited[i][j] != 0 or grid[i][j] == 0:
                return

            area += 1
            visited[i][j] = 1
            

            dfs(i, j+1, sm)
            dfs(i, j-1, sm)
            dfs(i-1, j, sm)
            dfs(i+1, j, sm)
            max_sum = max(max_sum, area)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = 0
                    dfs(i, j, 0)

        print(visited)
        return max_sum