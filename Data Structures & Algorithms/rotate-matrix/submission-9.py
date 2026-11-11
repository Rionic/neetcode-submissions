class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n // 2):

            for j in range(i, n - i - 1): # 10x10, 8x8, 6x6, 4x4, 2x2, (0x0 no loop)
                print('i', i, 'j', j)
                top = matrix[i][j]
                right = matrix[j][n - i - 1]
                bottom = matrix[n - i - 1][n - j - 1]
                left = matrix[n - j - 1][i]
                matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] = left, top, right, bottom

        # 5  1  9  11
        # 2  4  8  10
        # 13 3  6  7
        # 15 14 12 14