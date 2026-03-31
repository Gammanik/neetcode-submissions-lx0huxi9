class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            mp = set()
            for n in row:
                if n in mp:
                    return False
                if n != '.':
                    mp.add(n)

        for i in range(0, len(board[0])):
            mp = set()
            print(board[i])
            for j in range(0, len(board[0])):
                if board[j][i] in mp:
                    return False
                if board[j][i] != '.':
                    mp.add(board[j][i])

        def scan_square(f: List[int], s: List[int]):
            mp = set()
            for i in range(f[0], f[1]): 
                for j in range(s[0], s[1]):
                    print(i, j, mp)
                    if board[i][j] in mp:
                        return False
                    if board[i][j] != '.':
                        mp.add(board[i][j])
            print()
            return True
        
        return scan_square([0, 3], [0, 3]) and scan_square([0, 3], [3, 6]) and scan_square([0, 3], [6, 9]) and scan_square([3, 6], [0, 3]) and scan_square([3, 6], [3, 6]) and scan_square([3, 6], [6, 9]) and scan_square([6, 9], [0, 2]) and scan_square([6, 9], [3, 6]) and scan_square([6, 9], [5, 8])

        # for i in range(0, len(board) // 3, 3):
        #     for j in range(0, len(board) // 3, 3):
        #         if not scan_square([i, i+3], [j, j + 3]):
        #             return False

        return True

                
        