class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(prev,i,j,isPacific):
            if i<0 or j<0 or i>=ROWS or j>=COLS or prev>heights[i][j]:
                return

            if isPacific:
                if (i,j) in pacific:
                    return
                pacific.add((i,j))

            if not isPacific:
                if (i,j) in atlantic:
                    return
                atlantic.add((i,j))

            print(i,j,prev,heights[i][j],pacific if isPacific else atlantic)

            val = heights[i][j]
            dfs(val,i,j+1,isPacific)
            dfs(val,i,j-1,isPacific)
            dfs(val,i+1,j,isPacific)
            dfs(val,i-1,j,isPacific)

        for j in range(COLS):
            dfs(-1,0,j,True)
        for i in range(ROWS):
            dfs(-1,i,0,True)

        for j in range(COLS):
            dfs(-1,ROWS-1,j,False) 
        for i in range(ROWS):
            dfs(-1,i,COLS-1,False)

        print(atlantic)
        print(pacific)
        return list(pacific & atlantic)            