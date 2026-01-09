from typing import Optional

from src.main.java.com.example.day19.leetcode_501 import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            else:
                node = root.right
                while node.left:
                    node = node.left
                node.left = root.left
                return root.right
        return root