class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        # 0: {1, 2, 3}
        #
        #

        for r in range(9):

            for c in range(9):
                if r not in rows: rows[r] = set()
                if c not in cols: cols[c] = set()

                if (board[r][c] != "." and
                    (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)])):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                

        return True