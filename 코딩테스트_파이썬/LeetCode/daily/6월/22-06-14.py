#583. Delete Operation for Two Strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for col in range(len(word2) + 1)] for row in range(len(word1) + 1)]
        for i in range(len(word1)):
            dp[i][len(word2)] = len(word1) - i
        for i in range(len(word2)):
            dp[len(word1)][i] = len(word2) - i
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    penalty = 0
                else:
                    penalty = 2
                dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j + 1] + 1, dp[i + 1][j + 1] + penalty)

        return dp[0][0]