# 整数拆分
dp[j] = max(dp[j], dp[j - i] * i)]
dp[0] = 0
dp[1] = 1
dp[2] = 1
for i in range(3, n + 1):
for j in range(1, i + 1):
    dp[i] = max(dp[i],max((i - j) * j,dp[i - j] * j))
**拆成两个，一个是i另一个是dp[i - j]相当于固定了一个数**
# 不同的二叉搜索树
左子树，右子树分别计算
0个节点时是dp[0] = 1
其余节点按照dp[i] = dp[j - 1] * dp[i - j]就可以推出了