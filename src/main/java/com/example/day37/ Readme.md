# 石头相撞
把是否分成尽可能相似的两堆
dp数组含义： 背包容量为j所背的最大价值，重量和价值相同
dp[j] = max(dp[j] ,dp[j - weight[i]] + weigh[i]);
第一层遍历物品，第二层遍历背包
# 目标和
表达式等于目标和，可以随意放置
前面放加号的一个集合，加法集合减去减法集合等于target
求凑加法集合的数目
dp装满背包容量为j的有多少种方法
dp[j - nums[i]]
dp[j] += dp[j - nums[i]]
# 一和0
找到子集，最多有m个0，n个1，找到元素最多个数
0，1背包i
二维数组
dp[i][j]最大装了dp[i][j]个物品
dp[m][n]
dp[i - x][j - y] + 1
dp[i][j] = max(dp[i - x][j - y] + 1,dp[i][j])

dp[0][0] = 0
for (String s : strs):
int x = 0,y = 0
for (c : str.toCharArray()){
if c == '0' x ++
else y ++
for int (i = m;i >= x ;i --){
for(j = n;j >= y;j --)