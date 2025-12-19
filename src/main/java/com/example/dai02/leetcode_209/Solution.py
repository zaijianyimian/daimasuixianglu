from typing import List


class Solution:
    def minSubArrayLen(self,target : int,nums : List[int]) -> int:
        start,end = 0,0
        sum = 0
        res = len(nums) + 1
        while end < len(nums):
            while end < len(nums) and sum < target:
                sum += nums[end]
                end += 1
            while sum >= target:
                res = min(res,end - start)
                sum -= nums[start]
                start += 1
        return 0 if res == len(nums) + 1 else res