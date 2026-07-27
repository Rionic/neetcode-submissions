class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0        
        visited = set()

        def dfs(r, c, s):
            s.append((r,c))
            visited.add((r,c))

            DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in DIRS:
                nr, nc = dr + r, dc + c
                if nr in range(len(grid)) and nc in range(len(grid[r])) and grid[nr][nc] == '1' and (nr, nc) not in visited:
                    dfs(nr, nc, s)
            s.pop()
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c, [])
                    num += 1

        return num
