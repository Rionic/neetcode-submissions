class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
# . 1 0 .
# . . . 1
# . 1 . 1
# 0 1 . .
        def bfs(r, c):
            q = deque([(r, c, 1)])
            visited = [(r, c)]
            DIRS = ((0, -1), (1, 0), (0, 1), (-1, 0))
            while q:
                r, c, dist = q.popleft()
                for dr, dc in DIRS:
                    mr, mc = r + dr, c + dc
                    if (mr in range(len(grid))
                        and mc in range(len(grid[0]))
                        and grid[mr][mc] >= dist
                        and (mr, mc) not in visited
                        ):
                        print('adding dist', dist)
                        print('to bigger dist', grid[mr][mc])
                        print('to coords', mr, mc)
                        visited.append((mr, mc))
                        grid[mr][mc] = dist
                        q.append((mr, mc, dist+1))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    bfs(r, c)
        