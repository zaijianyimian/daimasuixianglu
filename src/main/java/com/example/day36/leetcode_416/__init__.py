from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        return self.dp(nums, target)

    def dp(self, nums: List[int], target: int) -> bool:
        dp = [0] * (target + 1)
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        return dp[target] == target
