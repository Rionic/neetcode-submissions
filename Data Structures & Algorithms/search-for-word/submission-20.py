class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_r = range(len(board)) # [0, 1, 2]
        board_c = range(len(board[0])) # [0, 1, 2, 3]

        def searchBoard(i, visited, r, c):
            if i == len(word):
                return True

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr in board_r and nc in board_c and (nr, nc) not in visited and board[nr][nc] == word[i]:
                    visited.add((nr, nc)) # Sets are pass by reference, we must remove
                    if searchBoard(i + 1, visited, nr, nc):
                        return True
                    visited.remove((nr, nc))

        for r in board_r:
            for c in board_c:
                if board[r][c] == word[0] and searchBoard(1, {(r,c)}, r, c):
                    return True
        
        return False


        