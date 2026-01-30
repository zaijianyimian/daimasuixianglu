class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s) + 1
        n = len(t) + 1
        dp = [[0] * n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1] == m - 1
