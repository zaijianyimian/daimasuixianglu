# 平衡二叉树
左右子树的节点高度差不能超过1
求高度后序遍历,求深度前序遍历 
```java
int getDepth(TreeNode root){
	if(root == null) return 0;
```
# 求二叉树所有路径
前序遍历,求路径,父节点指向孩子节点
```java
void travesel(TreeNode node, List<Integer> path, List<String> result) {
    path.add(node.val);
    if (node.left == null && node.right == null) {
        result.add(path.toString());
    }
    if(node.left != null){
        travesel(node.left, path, result);
        path.remove(node.val);
    }
    if(node.right != null){
        travesel(node.right, path, result);
        path.remove(node.val);
    }

}
```
# 求左叶子集合
# 求完全二叉树:
后续遍历: 
判断子树是否是满二叉树,一直往左递归,
```java
if(node ==  null){
return 0;}
lef = node.left;
right = node.right;
leftDepth = 0;
rightDepth = 0;
while(lef != null){
left = lef.left;
leftDepth++;}
while(right != null){
    right = right.right;
    rightDepth++;
        }
if(leftDepth == rightDepth){
    return 2<<leftDepth - 1;
        }
```
