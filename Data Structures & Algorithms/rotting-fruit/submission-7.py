class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if all(all(cell == 0 for cell in row) for row in grid):
            return 0
        minutes = -1
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        temp_q = deque()
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr = r + dr
                    nc = c + dc
                    if (nr in range(len(grid)) and 
                        nc in range(len(grid[0])) and 
                        grid[nr][nc] == 1):
                        temp_q.append((nr, nc))
                        grid[nr][nc] = 2

            minutes += 1
            q = temp_q.copy()
            temp_q.clear()
        
        if any(1 in row for row in grid):
            return -1
        return minutes

        