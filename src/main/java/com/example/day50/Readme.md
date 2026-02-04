# 接雨水
单调递增栈，求右边第一个比他大的元素，左边第一个比他大的元素，然后求出面积。
``` python
栈中存放的是下标，
for i in range(len(h)):
if h[i] < h[stack[-1]]:
stack.append(i)
elif h[i] == h[stack[-1]]:
st.pop()
st.push(i)
while stack and h[i] > h[stack[-1]]:
mid = stack.pop()

```
# 数组中的最大矩形
找左边比低的柱子，右边低于当前的数组，
高度为
左边第一个比他矮的，右边第一个比他矮的数组
暴力解法，双指针预处理
右边或者左边第一个比他大/小的就是
mid < st.pop()
左边比他小的一定是
首位还得加0，否则会无法计算
```python
res = 0
stack = [0]
h.insert(0,0)
h.insert(0,-1)
# 当前遍历元素 大于栈口元素直接入栈
for i in range(1,len(h)):
   if h[i] > h[stack[-1]]:
       stack.append(i)
   elif h[i] == h[stack[-1]]:
       stack.pop()
       stack.append(i)
   else:
       while stack and h[i] < h[stack[-1]]:
           mid = stack.pop()
           res = max(res,h[mid] * (i - stack[-1] - 1))
           
return res
          
# 当前遍历元素小于栈口元素，栈中元素出栈，计算面积
    
```