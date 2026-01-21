from typing import List


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 1
# 倒序遍历确保每隔元素只添加一次
    def solve(self) -> int:
        m, n = map(int, input().split())
        self.m = m
        self.n = n
        weights = list(map(int, input().split()))
        values = list(map(int, input().split()))

        return self.dp(weights, values)

    def dp(self, weigh: List[int], val: List[int]) -> int:
        dp = [0] * (self.n + 1)
        for i in range(self.m):
            for j in range(self.n, weigh[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - weigh[i]] + val[i])
        return dp[self.n]


if __name__ == '__main__':
    s = Solution()
    print(s.solve())
