# 动态规划求回文字串
- dp数组含义 dp[i][j]表示s[i:j]是否为回文字串
- 状态转移方程
i== j dp[i][j] = true
j - i == 1 dp[i][j] = s[i] == s[j] 
dp[i + 1][j  -  1] = true: dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
- 初始化
dp[i][j] = false
- 遍历顺序：
从下往上，从左往右
 i = n - 1; i >= 0; i--
 j = i; j < n; j++
# 最长回文子序列：
bb,aa,cc就是回文串
可以不连续
1. dp数组含义
dp[i][j]表示s[i][j]中回文子序列的长度
2. s[i] == s[j]:
dp[i][j] = dp[i + 1][j - 1] + 2
3. s[i] != s[j]:
dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
4. i == j:
dp[i][j] = 1
- 遍历顺序：
i = n - 1; i >= 0; i--
j = i + 1; j < n; j++

return dp[0][n - 1];