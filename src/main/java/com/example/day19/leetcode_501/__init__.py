from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def __init__(self):
        self.maxValue = 0
        self.count = 0
        self.ans = []
        self.pre = None
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs( root)
        return self.ans
    def dfs(self,root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.dfs(root.left)
        if self.pre is None:
            self.count = 1
        elif self.pre.val == root.val:
            self.count += 1
        else:
            self.count = 1
        if self.count == self.maxValue:
            self.ans.append(root.val)
        elif self.count > self.maxValue:
            self.maxValue = self.count
            self.ans.clear()
            self.ans.append(root.val)
        self.pre = root
        self.dfs(root.right)
        return