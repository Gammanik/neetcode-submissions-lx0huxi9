class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]), 
        visited = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if visited[i][j] == 1:
                return

            visited[i][j] = 1

            if grid[i][j] == '1':
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i-1, j)
            
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    print('~~', i, j, visited)
                    res += 1
                    dfs(i, j)
        
        print(visited)
        return res