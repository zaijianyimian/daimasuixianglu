from typing import Optional

from src.main.java.com.example.day19.leetcode_501 import TreeNode


class Solution:
    def __init__(self):
        self.pre = None
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.convertBST(root.right)
        if self.pre:
            root.val += self.pre.val
        self.pre = root
        self.convertBST(root.left)
        return root
