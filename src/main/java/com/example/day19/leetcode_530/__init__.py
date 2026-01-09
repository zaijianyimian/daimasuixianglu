from typing import Optional

from src.main.java.com.example.day18.leetcode_654.Solution import TreeNode


class Solution:
    def __init__(self):
        self.a = float('inf')
        self.pre = None
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.a

    def dfs(self,root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.dfs(root.left)
        if(self.pre is not None):
            self.a = min(self.a,root.val - self.pre.val)
        self.pre = root
        self.dfs(root.right)