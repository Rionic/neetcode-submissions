class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        def bfs(r, c):
            q = deque([(r, c)])
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                r, c = q.popleft()
                for d in directions:
                    dr, dc = r + d[0], c + d[1]
                    if (0 <= dr < len(grid) and
                        0 <= dc < len(grid[0]) and
                        grid[dr][dc] == '1' and
                        (dr, dc) not in visited):
                        visited.add((dr, dc))
                        q.append((dr, dc))
                        print('visited', dr, dc)
            return 1


        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited:
                    visited.add((r, c))
                    if grid[r][c] == '1':
                        islands += bfs(r, c)
        
        return islands