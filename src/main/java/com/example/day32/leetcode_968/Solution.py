from typing import Optional
from main.java.com.example.day19.leetcode_501 import TreeNode


class Solution:
    def __init__(self):
        self.ans = 0
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if self.dfs(root) == 0:
            self.ans += 1
        return self.ans
    def dfs(self,node: Optional[TreeNode]) -> int:
        if not node:
            return 2
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if left == 2 and right == 2:
            return 0
        elif left == 0 or right == 0:
            self.ans += 1
            return 1
        elif left == 1 or right == 1:
            return 2
        return -1