# 构造二叉树
根据传入数组构建二叉树,确定递归终止条件
数组大小等于1时直接返回
if nums.size() == 1:
return new TreeNode(nums[0])
maxValue,index = 0,0
for i in range(len(nums)):
    if nums[i] > maxValue:
        maxValue = nums[i]
index = nums.index(maxValue)
root = TreeNode(maxValue)
if index >  0:
root.left = constructMaximumBinaryTree(nums[0:index:1])
if index < len(nums) - 1:
root.right = constructMaximumBinaryTree(nums[index+1:len(nums):1])
return root
# 合并二叉树:
给出两个二叉树,涉及到遍历顺序
前序遍历最好,中左右实现
终止条件: if(root1 == null)return root2;
if(root2 == null)return root1;
root1.val += root2.val;
root1.left = mergeTrees(root1.left,root2.left);
root1.right = mergeTrees(root1.right,root2.right);
# 验证二叉搜索树
max_Value = int("-inf")
if root == None:
return True
left = isValidBST(root.left)
if root.val > max_Value:
    max_Value = root.val
else:
return False\
right = isValidBST(root.right)
return left and right

## 双指针优化:
pre = Treenode(None)
if pre != None and pre.val > root.val:
return 