# 最大递增子序列:
要求不能有重复子序列,不可以进行排序,一旦排序就会出现问题
**树根上可以重复取,数层上不可以**
会遇到重复问题
树层上去重,树根上不去重
元素个数>= 2时进行收获
```python
path = []
res = []
def backtrack(nums,start,path:list):
    if len(path) > 1:
        res.append(path.copy())
    set = {}
    for i in range(start,len(nums)):
        if nums[i] < path[-1] and nums[i] in set:
            continue
        set.update(nums[i])
        path.append(nums[i])
        backtrack(nums,i+1,path)
        path.pop()
```
### 全排列2问题
卡在了去重这里
排序+used数组
中间只能用continue
# N皇后问题
回溯 + 剪枝
```python
result = [[[0] * n] * n] * n
if row == n:
    res.append(result.copy())
for i in range(n) :
    if isValid(row,i,chessBoard,n)
```
