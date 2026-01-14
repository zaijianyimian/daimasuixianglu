from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n  = len(nums)
        next,cur,res = 0,0,0
        for i in range(n):
            next = max(next,i + nums[i])
            if i == cur:
                if cur != n - 1:
                    cur = next
                    res+=1
        return res

