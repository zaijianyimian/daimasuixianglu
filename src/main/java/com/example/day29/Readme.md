# 买卖股票的最佳时机2:
可以买卖多次,不限制交易次数
这里使用贪心思路来解决:
找到最低点,最高点,逐渐买卖,
可以拆成每一天的利润,只收获正数,将数组转换为利润数组
# 跳跃游戏2:
只去看覆盖范围
if nums.length == 1:
return 0
int cur = 0:
int next = 0:
result = 0
for i in range(len(nums)):
next = max(next,i + nums[i])
if i == cur:
cur = next
step += 1
re