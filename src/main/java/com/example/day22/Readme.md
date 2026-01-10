# 修剪二叉树
```python
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        if root.val < low:
            right = self.trimBST(root.right, low, high)
            return right
        elif root.val > high:
            left =  self.trimBST(root.left, low, high)
            return left
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

```
# 将二叉树转换为累加树:
右中左遍历
```python
class Solution:
    def __init__(self):
        self.pre = None
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.convertBST(root.right)
        if self.pre:
            root.val += self.pre.val
        self.pre = root
        self.convertBST(root.left)
        return root
```