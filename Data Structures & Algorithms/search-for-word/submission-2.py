class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = [[0] * m for _ in range(n)]

        def dfs(l, i, j):
            if l >= len(word):
                return True

            if i >= n or j >= m or i < 0 or j < 0:
                return False

            if board[i][j] == word[l] and visited[i][j] == 0:
                visited[i][j] = 1
                l = l+1
                res = dfs(l, i, j+1) or dfs(l, i+1, j) or dfs(l, i, j-1) or dfs(l, i-1, j)
                visited[i][j] = 0
                return res

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    print(i,j)
                    if dfs(0, i, j):
                        return True

        return False
        