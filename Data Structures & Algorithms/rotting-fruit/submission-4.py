from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        def rot(i, j):
            if i<0 or j<0 or i>=ROWS or j>=COLS or grid[i][j] != 1:
                return

            grid[i][j] = 2
            q.append((i,j))


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))

        res = -1
        while q:
            res += 1
            for c in range(len(q)):
                i, j = q.popleft()

                rot(i,j+1)
                rot(i,j-1)
                rot(i+1,j)
                rot(i-1,j)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return res if res != -1 else 0