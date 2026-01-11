class Solution:
    def maxSubArray(self,nums: list[int]) -> int:
        curSum = maxSum = float("-inf")
        for i in nums:
            curSum = max(i,curSum + i)
            maxSum = max(curSum,maxSum)
        return maxSum