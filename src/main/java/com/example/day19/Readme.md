def TreeNode(param):
    pass双指针直接得出更好操作
``` python
a = int('inf')
pre = TreeNode(None)
void traverser(TreeNode root):
    if root == None:
        return
    traverser(root.left)
    if pre is not None:
        a = min(a, root.val - pre.val)
    pre= root
    traverser(root.right)
```
# 二叉搜索树求众数
中序遍历
```python
pre = TreeNode(None)
maxCount = 0
arr = []
class Solutin:
    def findMode(self, root):
        count = 0
        if root == None:
            return arr
        if pre is None:
            count = 1
        elif pre.val == root.val:
            count += 1
        else:
            count = 1
        pre =  root
        if(count == maxCount):
            arr.append(root.val)
        if (count > maxCount):
            maxCount = count
            arr.clear()
            arr.append(root.val)
             

```
# 最近公共祖先
从下往上处理
后序遍历
``` python
def traverse(root:TreeNode, p:TreeNode, q:TreeNode) -> Option[TreeNode]:
    if root == None:
        return root
    if root == p or root == q:
        return root
    left = traverse(root.left, p, q)
    right = traverse(root.right, p, q)
    if left != None and right != None:
        return root
    elif left != None and right == None:
        return left
    elif left == None and right != None:
        return right
    return None
        
```