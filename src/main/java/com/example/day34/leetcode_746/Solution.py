from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return 0
        dp = [0] * (len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(dp),1):
            dp[i] = min(dp[i - 1],dp[i - 2]) + (cost[i] if i < len(cost) else 0)
        return dp[-1]