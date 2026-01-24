# 零钱兑换
装满背包最少用多少个物品
动归五部曲
1. 装满容量为j的背包的最少物品容量为dp[j]
2. dp[j - consume[i]] + 1,dp【j]
3. dp[0] = 0
4. 非零下标应该初始为fload('inf')
5. 先遍历物品再遍历背包
6. for i in range(0,coins[i] + 1):
7. dor j in range(coins[i],len(dp)):
# 完全平方数：
i = 1:
while i * i <= n:
    for j in range(i * i, n + 1):
        dp[j] = min(dp[j], dp[j - i * i] + 1)
# 单词拆分：
如果字符串长度可以被组成就可以设置为对应内容
如果区间【j,i] && dp[j] == true
dp[0] = true
先遍历背包再遍历物品求的是排列
先遍历物品，再遍历物品求的是组合数
for i in range(1, len(s) + 1):
    for j in range(i):
        if s[j:i] in wordDict and dp[j] == True:
            dp[i] = True
