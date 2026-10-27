class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1) + 1, len(text2) + 1

        dp = [[0 for i in range(m)] for j in range(n)]

        for i in range(1, n):

            for j in range(1, m):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] =  dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n - 1][m - 1]