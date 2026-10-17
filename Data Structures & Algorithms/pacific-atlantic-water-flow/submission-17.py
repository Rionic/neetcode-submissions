class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = {(r,c) for r in range(m) for c in range(n) if r == 0 or c == 0}
        atlantic = {(r,c) for r in range(m) for c in range(n) if r == m - 1 or c == n - 1}

        def dfs(r, c, visited, ocean):

            if (r, c) in visited:
                return
            visited.add((r, c))
            ocean.add((r, c))

            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited, ocean)
        
    
        for r, c in pacific.copy():
            dfs(r, c, set(), pacific)
        
        for r, c in atlantic.copy():
            dfs(r, c, set(), atlantic)
        
        return list(pacific & atlantic)