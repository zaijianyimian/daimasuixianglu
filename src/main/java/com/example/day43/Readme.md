# 买卖股票的最佳时机4
最多允许买卖k次
for j = 0 j < 2 * k ;j += 2:
dp[i][j + 1] = max(dp[i - 1][j + 1],dp[i - 1][j] - prices[i])
dp[i][j + 2] = max(dp[i - 1][j +  2,dp[i - 1][j + 1] + prices[i]])

for j = 0;j < 2 * k;j += 2:
 dp[0][j] = -prices[0]
# 买卖股票最佳时机，含冷冻时期
dp:基于冷冻期列出每一天的状态，
dp[i][0] 持股
dp[i][1] 保持卖出股票
dp[i][2] 卖出股票状态
dp[i][3] 冷冻期
递推公式：
dp[i][0] = max(dp[i - 1][0],max(dp[i - 1][3] - prices[i],dp[i - 1][1] - prices[i]))
dp[i][1] = max(dp[i - 1][1],dp[i - 1][3])
dp[i][2] = dp[i - 1][0] + prices[i]
dp[i][3] = dp[i - 1][2]
初始化：
dp[0][0] = -prices[0]
dp[0][1] = 0
dp[0][2] = 0
dp[0][3] = 0
for i = 1;i < n;i += 1:


return max(dp[n - 1][3],max(dp[n - 1][1],dp[n - 1][2]))