# 单调递增的数字：
 给定一个非负整数 N，找出小于或等于 N 的最大的整数，且其各位数字是单调递增的。
 **遍历数字：如果当前数字之前位数满足单调递增，直接返回当前数字，否则从前往后遍历，找到第一个不满足单调递增的位置，将该位置之前的数字减一，将该位置及之后的数字设为9，返回结果。**
*但是遇到问题，比如12214，遍历到1后发现当前位置不是递增的，需要将前一位减一，得到12199*
``` python
n:int
s = str(n)
for i in range(len(s) - 1,0,-1):
    if int(s[i - 1]) > int(s[i]):
        if s[i - 1] > s[i]:
            s[i - 1] = str(int(s[i - 1]) - 1)
            for j in range(i,len(s)):
                s[j] = '9'
return int(''.join(s))


```
注意str是不可变类型，需要转换为list才能进行赋值操作
# 监控摄像头，
从下往上遍历二叉树，后序遍历，左右中，按照每隔两个节点放一个摄像头
0：无覆盖
1： 有摄像头
2： 有覆盖
空节点只能是有覆盖状态，否则会导致叶子节点放置摄像头
左右孩子都有覆盖，只能在父节点放置摄像头
左右孩子有一个没被覆盖，只能在父节点放置摄像头
左右孩子有一个摄像头，父节点就是有覆盖状态，
根节点可能会没有赋值，
``` python
result = 0
TreeNode: root
if not root: return 2
left = dfs(root.left)
right = dfs(root.right)
if left == 2 and right == 2:
    return 0
elif left == 0 or right == 0:
    return 1
elif left == 1or right == 1:    
    return 2
return -1
if dfs(root) == 0:
    result += 1
```