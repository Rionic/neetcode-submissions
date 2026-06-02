class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        grid = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                num = board[r][c]
                if num == '.':
                    continue
                if num in rows[r]:
                    return False
                rows[r].add(num)
                if num in cols[c]:
                    return False
                cols[c].add(num)
                if num in grid[(r//3, c//3)]:
                    return False
                grid[(r//3, c//3)].add(num)


        return True
