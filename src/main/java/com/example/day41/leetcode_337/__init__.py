from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        result = self.travesal(root)
        return max(result)
    def travesal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [0,0]
        left = self.travesal(root.left)
        right = self.travesal(root.right)
        val1 = root.val + left[0] + right[0] # 偷当前节点
        val2 = max(left[0],left[1]) + max(right[0],right[1]) # 不偷当前节点
        return [val2,val1]

