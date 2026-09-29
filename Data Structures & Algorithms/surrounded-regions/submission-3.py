class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        search = []

        search = [(r, c) 
                for r in range(rows) for c in range(cols)
                if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == "O"]
        
        safe = set(search)

        q = deque(search)
        
        while q:
            r, c = q.popleft()

            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and board[nr][nc] == "O" and (nr, nc) not in safe:
                    safe.add((nr, nc))
                    q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in safe:
                    board[r][c] = "X"
        