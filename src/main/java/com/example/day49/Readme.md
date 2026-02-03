# 每日温度，找到后面比当天气温大的
单调栈，左边和右边
大于时直接弹出，将下标1继续加入，
要记录栈顶元素的下标，
```python
if t[i] <= t[stack[-1]]:
    stack.append(i)
while stack and t[i] > t[stack[-1]]:
    ans[stack[-1]] = i - stack[-1]
    stack.pop()
stack.append(i)
return ans
```
# 下一个更大的元素
单调递增栈
n = len(nums1)
if n == 0:
return  []
res = [-1] * n
做hash映射到元素的索引
for i in range(len(nums2)):
   dict[nums2[i]] = i
if 
