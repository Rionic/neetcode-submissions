class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            m = (top + bot) // 2
            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bot = m - 1
            else:
                break

        if top > bot:
            return False
        row = matrix[m]
        
        l, r = 0, len(row) - 1

        while l <= r:
            m = (r + l) // 2
            if row[m] == target:
                return True
            elif row[m] > target:
                r = m - 1
            elif row[m] < target:
                l = m + 1
        return False
            
            

