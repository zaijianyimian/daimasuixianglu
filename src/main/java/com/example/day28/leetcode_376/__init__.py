from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        dp = [0] * (n - 1)
        for i in range(1,n):
            dp[i - 1] = nums[i] - nums[i - 1]
        up = down = False
        count = 0
        for i in range(0,len(dp)):
            if dp[i] > 0 and not up:
                count += 1
                up = True
                down = False
            elif dp[i] < 0 and not down:
                count += 1
                up = False
                down = True
        return count + 1
