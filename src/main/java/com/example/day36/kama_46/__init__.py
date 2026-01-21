from typing import List


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 1

    def solve(self) -> int:
        m, n = map(int, input().split())
        self.m = m
        self.n = n
        weigh = []
        val = []
        for i in range(self.m):
            weigh.append(int(input()))
        for i in range(self.m):
            val.append(int(input()))

        return self.dp(weigh, val)

    def dp(self, weigh: List[int], val: List[int]) -> int:
        dp = [[0] * (self.n + 1) for i in range(self.m + 1)]
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                if j < weigh[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                elif j >= weigh[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], val[i - 1] + dp[i - 1][j - weigh[i - 1]])
        return dp[self.m][self.n]


if __name__ == '__main__':
    s = Solution()
    print(s.solve())
