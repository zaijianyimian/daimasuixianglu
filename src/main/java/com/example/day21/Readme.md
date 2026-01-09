# 二叉搜索树的最近公共祖先
利用特性,递归
如果当前节点大于对应节点,则在当前节点的左子树中查找
反之则从右子树查找.
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
```
# 二叉搜索树的插入操作:
```python
# 遇到终止条件就说明找到了插入位置
if root == None:
    node = TreeNode(val)
    return node
if root.val > val:
    root.left = self.insertIntoBST(root.left, val)
else:
    root.right = self.insertIntoBST(root.right, val)
return root
```

# 删除二叉树节点
1. 没找到要删除的节点
2. 要删除的节点是叶子节点:左为空右为空
3. 要删除的节点左不为空右为空:父节点直接指向左孩子
4. 左为空右不为空
5. 左不空,右不空
```python
class TreeNode delete(TreeNode root, int key) -> TreeNode:
    if root == None:
        return None
    if root.val == key:
        if root.left == None and root.right == None:
            return None
        elif root.left != None and root.right == None:
            return root.left
        elif root.left == None and root.right != None:
            return root.right
        else:
            node = root.right
            while node.left != None:
                node = node.left
            node.left = root.left
            return root.right

```