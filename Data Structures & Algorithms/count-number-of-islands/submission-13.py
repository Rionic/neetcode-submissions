class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = []

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.append((r, c))
            DIRS = ((0, -1), (1, 0), (0, 1), (-1, 0))
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    mr, mc = r + dr, c + dc
                    if (mr in range(len(grid)) and
                        mc in range(len(grid[0])) and
                        (mr, mc) not in visited and
                        grid[mr][mc] == "1"):
                        q.append((mr, mc))
                        visited.append((mr, mc))
                

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands