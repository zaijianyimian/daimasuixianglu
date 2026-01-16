# 重叠区间问题
## 用最少的弓箭引爆气球
如果左边界大于前一个气球的右边界,
小于等于前一个起球的有边界,那么就说明重叠了,弓箭数量
```python
if size == 0 return 0
nums.sort(x = lambda x : x[0])
int count = 1
for i in range(1,size):
    if nums[i][0] > nums[i - 1][1]:
        count += 1
    else:
        nums[i][1] = min(nums[i][1],nums[i - 1][1])
return count
```
# 划分数组区间
每个字符只能出现在一个区间中