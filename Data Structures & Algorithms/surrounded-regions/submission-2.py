class Sides:
    left: bool
    right: bool
    up: bool
    down: bool

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        border = [[0]*cols for _ in range(rows)]

        
        def dfs(i, j):
            if i<0 or j<0 or i>=rows or j>=cols or border[i][j] == 1 or board[i][j] == 'X':
                return

            border[i][j] = 1
            if j == 5:
                print(j, border[i][j])
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)

        for i in range(rows): dfs(i,0)
        for i in range(rows): dfs(i,cols-1)

        for j in range(cols): dfs(0,j)
        for j in range(cols): dfs(rows-1,j)

        print(border)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and border[i][j] == 0:
                    board[i][j] = 'X'
