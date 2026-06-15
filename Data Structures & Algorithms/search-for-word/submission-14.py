class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # row_1 = [1][0]
        # col_2 = [0][2]
        self.found = False
        board_r = range(len(board)) # [0, 1, 2]
        board_c = range(len(board[0])) # [0, 1, 2, 3]

        def searchBoard(curWord, visited, r, c):
            # Base case
            if curWord == word:
                self.found = True
                return

            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr in board_r and nc in board_c and (nr, nc) not in visited and board[nr][nc] == word[len(curWord)]:
                    visited.add((nr, nc)) # Sets are pass by reference, we must remove
                    searchBoard(curWord + board[nr][nc], visited, nr, nc)
                    visited.remove((nr, nc))
                if self.found == True:
                    return

        # Search each tile in board, returning when the word doesn't start at pos r, c
        for r in board_r:
            for c in board_c:
                if board[r][c] == word[0]:
                    searchBoard(word[0], {(r,c)}, r, c)
                if self.found == True:
                    return True
        
        return self.found


        