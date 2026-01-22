from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if abs(target) > totalSum:
            return 0
        if (target + totalSum) % 2 == 1:
            return 0
        targetSum = (target + totalSum) // 2
        dp = [0] * (targetSum + 1)
        dp[0] = 1
        for num in nums:
            for j in range(targetSum,num - 1, -1):
                dp[j] += dp[j - num]
        return dp[targetSum]