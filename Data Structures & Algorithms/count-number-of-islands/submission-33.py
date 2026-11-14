class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited, islands = set(), 0
        n, m = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands