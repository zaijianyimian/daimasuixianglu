# 买卖股票的最佳时机
dp[i][0] 持有股票的最大现金
dp[i][1] 卖出股票的最大现金
# 买卖股票最佳时机2
股票可以买卖多次
就是将dp[i][1] - prices[i]替代-price[i]
# 买卖股票最佳时机3
至多买卖两次
 dp[i][0] 不操作
dp[i][1] 第一次持有
dp[i][2] 第一次不持有
dp[i][3] 第二次持有
dp[i][4] 第二次不持有
dp[i][0] = dp[i - 1][0]
dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
dp[i][2] = max(dp[i - 1][2],dp[i - 1][1] + prices[i])
dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
dp[0][0] = 0
dp[0][1] = -price[i]
dp[0][2] = 0
dp[0][3] = -price[i]
dp[0][4] = 0
