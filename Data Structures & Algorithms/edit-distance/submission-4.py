class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        dp = [[float('inf')] * (m + 1) for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][m] = n - i

        for j in range(m + 1):
            dp[n][j] = m - j

        # dp[0][0] is the answer
        # work backwards from dp[-1][-1]
        # "abzde"
        # "abcde"

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j], # delete
                        dp[i][j + 1], # insert
                        dp[i + 1][j + 1] # replace
                    )

        return dp[0][0]