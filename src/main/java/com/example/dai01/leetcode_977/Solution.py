from typing import List


class Solution:
    def sortedSquares(self,nums : List[int]) -> List[int]:
        l,r = 0,len(nums) - 1
        ans = [0] * len(nums)
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans[r - l] = nums[l] * nums[l]
                l += 1
            else:
                ans[r - l] = nums[r] * nums[r]
                r -= 1
        return ans