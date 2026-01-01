# 找左下角节点,
前中后遍历都可以,
最后一行最左侧
int maxDepth = Integer.MIN_VALUE;
int result = null;
void traverse(TreeNode root,int depth){
if (root.left == null && root.right == null){
if (depth > maxDepth){
maxDepth = depth;
result = root.val;}
}
if (root.left != null){
traverse(root.left,depth+1);
}
if (root.right != null){
traverse(root.right,depth+1);}

# 判断是否有目标和
一路减下去

boolean hasPathSum(TreeNode root,int sum){
if(root.left == null && root.right == null){
count == 0;
if(root.left != null){
if traverse(root.left,sum-root.val)
return true;
if(root.right != null){
if(traverse(root.right,sum-root.val);){
return true;}
return false;
# 从序列中构建二叉树给出中序和后序序列 
1. 后序数组为0,空节点
2. 后续数组中的最后一个元素为根节点
3. 寻找中序数组位置作为切割点
4. 切中序数组
5. 切后序数组
6. 递归处理左区间后区间
if
