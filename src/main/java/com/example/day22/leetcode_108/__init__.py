from typing import List, Optional

from src.main.java.com.example.day19.leetcode_501 import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums,0,len(nums)-1)

    def dfs(self,nums:list[int],lo:int ,hi : int) -> TreeNode:
        if lo > hi:
            return None
        mid  = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = self.dfs(nums,lo,mid-1)
        node.right = self.dfs(nums,mid+1,hi)
        return node