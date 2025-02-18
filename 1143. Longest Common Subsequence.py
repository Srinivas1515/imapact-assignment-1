class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        # Initialize the first row and column
        for i in range(n1 + 1):
            dp[i][0] = 0
        for j in range(n2 + 1):
            dp[0][j] = 0

        # Fill the dp array
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n1][n2]
