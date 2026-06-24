class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if text2[i] == text1[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])

        print(dp)
        return dp[0][0]
