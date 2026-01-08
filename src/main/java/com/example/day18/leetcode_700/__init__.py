from typing import Optional

from src.main.java.com.example.day18.leetcode_654.Solution import TreeNode


class Solution:
    def searchBST(self,root: Optional[TreeNode],val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left if val < root.val else root.right,val)