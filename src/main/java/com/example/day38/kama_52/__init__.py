class Solution:
    def knapsack(self, n, bgWeight, weight, value):
        # 创建二维DP数组
        dp = [[0] * (bgWeight + 1) for _ in range(n)]

        # 初始化第一行 - 对于完全背包，第一个物品可以重复使用
        for j in range(weight[0], bgWeight + 1):
            dp[0][j] = dp[0][j - weight[0]] + value[0]

        # 填充DP表
        for i in range(1, n):
            for j in range(bgWeight + 1):
                if j < weight[i]:
                    # 当前容量无法装下第i个物品
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 可以选择不放或放第i个物品，取最大值
                    # 注意：这里使用dp[i][j - weight[i]]而不是dp[i-1][j - weight[i]]
                    # 这是完全背包的关键，允许重复选择同一个物品
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - weight[i]] + value[i])

        return dp[n - 1][bgWeight]


if __name__ == '__main__':
    n, bag_weight = map(int, input().split())
    weight = []
    value = []
    for i in range(n):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    print(Solution().knapsack(n, bag_weight, weight, value))
