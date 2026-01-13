from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = float('-inf')
        for i in range(len(nums)):
            curSum += nums[i]
            if nums[i] > curSum:
                curSum = nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum
