class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # todo: build tree
        head = {}
        rows, cols = len(board), len(board[0])
        res = []

        visiting = set()
        def dfs(i, j, curr, currW):
            if i<0 or j<0 or i>=rows or j>= cols or (i,j) in visiting:
                return

            c = board[i][j]
            if not c in curr:
                return

            curr = curr[c]
            currW += c

            if '#' in curr:
                res.append(currW)
                curr.pop('#')

            visiting.add((i,j))
            dfs(i, j+1, curr, currW)
            dfs(i, j-1, curr, currW)
            dfs(i+1, j, curr, currW)
            dfs(i-1, j, curr, currW)
            visiting.remove((i,j))

        def insert(word):
            curr = head
            for c in word:
                if not c in curr:
                    curr[c] = {}
                curr = curr[c]

            curr['#'] = '#'

        for w in words:
            insert(w)

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,head, "")

        return res

