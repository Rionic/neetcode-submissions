class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            area = 1
            q = deque([(r, c)])
            # q.append((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                (curR, curC) = q.popleft()
                for dr, dc in directions:
                    r, c = curR + dr, curC + dc
                    print('r, c', r, c)
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        area += 1
                        q.append((r, c))
                        visited.add((r, c))
                print(q, visited)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and grid[r][c] not in visited:
                    visited.add((r, c))
                    maxArea = max(maxArea, bfs(r, c))
                    print('max', maxArea)

        return maxArea
                