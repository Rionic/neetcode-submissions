class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearchCol(matrix, target):
            l, r = 0, len(matrix) - 1

            while l <= r:
                m = (r + l)//2
                if matrix[m][0] <= target and nextRow(matrix, m):
                    return matrix[m]
                elif matrix[m][0] > target:
                    r = m - 1
                elif matrix[m][0] < target:
                    l = m + 1
            return False

        def nextRow(matrix, m):
            if m + 1 >= len(matrix):
                return True
            if matrix[m + 1][0] > target:
                return True
            return False

        row = binarySearchCol(matrix, target)
        if row == False:
            return False
        l, r = 0, len(row) - 1

        while l <= r:
            m = (r + l)//2
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
        return False

