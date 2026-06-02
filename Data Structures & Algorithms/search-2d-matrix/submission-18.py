class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        arr = []
# 1
# 4
# 7
# 12
# 23
# 44
# t = 34
        while top <= bot:
            m = (top + bot)//2
            cur = matrix[m][0]

            if target == cur:
                return True
            elif target < cur:
                if m <= 0: # Target < smallest element
                    return False
                bot = m - 1
                
            elif target > cur:
                if m >= len(matrix) - 1:
                    arr = matrix[-1]
                    break
                if matrix[m + 1][0] > target:
                    arr = matrix[m]
                    break
                else:
                    top = m + 1
                    
            else:
                return False
        
        if not arr: return False

        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r)//2
            if arr[m] == target:
                return True
            elif arr[m] > target:
                r = m - 1
            elif arr[m] < target:
                l = m + 1
        return False