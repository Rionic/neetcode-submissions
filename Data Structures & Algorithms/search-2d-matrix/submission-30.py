class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        arr = []

        while top <= bot:
            m = (top + bot)//2
            print(m)
            if target < matrix[m][0]:
                bot = m - 1
            elif target > matrix[m][-1]:
                top = m + 1
            else:
                break

        if top > bot : # none of the rows contain target
            return False

        arr = matrix[m]
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