from typing import Optional

from src.main.java.com.example.day18.leetcode_654.Solution import TreeNode


class Solution:
    def __init__(self):
        self.max_Value = float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left = self.isValidBST(root.left)
        if root.val > self.max_Value:
            self.max_Value = root.val
        else:
            return False
        right = self.isValidBST(root.right)
        return left and right
