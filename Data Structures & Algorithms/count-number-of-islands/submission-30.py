class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def bfs(r, c):

            q = deque([(r, c)])

            while q:
                r, c = q.popleft()
                visited.add((r, c))
                for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1


        return islands