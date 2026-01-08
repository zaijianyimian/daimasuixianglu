from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        node = TreeNode(0)
        maxValue = 0
        maxValueIndex = 0
        for i in range(len(nums)):
            if nums[i] > maxValue:
                maxValue = nums[i]
                maxValueIndex = i
        node.val = maxValue
        if maxValueIndex > 0:
            node.left = self.constructMaximumBinaryTree(nums[:maxValueIndex])
        if maxValueIndex < len(nums)-1:
            node.right = self.constructMaximumBinaryTree(nums[maxValueIndex+1:])
        return node

