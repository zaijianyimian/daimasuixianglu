# 零钱问题，背包容量为amount的
dp[j] += dp[j - coins[i]]
dp[0] = 1
组合数：
for(i = 0;i < coins.size();i ++){
for (j = coins[i];j <= amount;j ++){
    先遍历物品再遍历背包是组合数
}}