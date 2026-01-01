# 反转二叉树
前序和后序最直接,
递归遍历中的写法:

if root == null return;

前序:swap(root.left,root.right):
invertTree(root.left);
invertTree(root.right);
中序遍历后会遍历两次,相当于根本没有改变
# 对称二叉树:
判断二叉树是否对称
 **左子树和右子树可以相互反转就是对称二叉树**
比较外侧和内侧节点是否相等.
遍历二叉树,确定遍历方式.
只能使用后序左右中,不断收集左右孩子的节点返回给上一层 节点.
boolean isSymmetric(TreeNode root) {}
左节点为空,右节点不为空,返回false;
左节点不为空,右节点为空,返回false;
左右节点都为空,返回true;
左右都不为空但是值不相等,返回false;
左右都不为空且值相等,继续遍历左节点的左子树和右节点的右子树,以及左节点的右子树和右节点的左子树.
遍历左节点外侧右节点外侧
左节点内侧,右节点内侧.
外侧相等内侧相等,返回true;
# 二叉树深度 前序遍历
# 二叉树高度, 后序遍历
int getHeight(TreeNode root):
if root == null: return 0;
int leftHeight = getHeight(root.left);
int rightHeight = getHeight(root.right);
return Math.max(leftHeight,rightHeight) + 1;
# 二叉树的最小深度
根节点到叶子节点的最小距离
后序遍历,求的是高度
int getMinDepth(TreeNode root){
if root == null: return 0;
int leftDepth = getMinDepth(root.left);
int rightDepth = getMinDepth(root.right);
if leftDepth == 0: return rightDepth + 1;
if rightDepth == 0: return leftDepth + 1;
return Math.min(leftDepth,rightDepth) + 1;