from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        # 传入对应长度减一方便判断数组start end是否相等
        result1 = self.rang(nums,0,len(nums) - 2)
        result2 = self.rang(nums,1,len(nums) - 1)
        return max(result1, result2)
    def rang(self, nums: List[int],start,end):
        if end == start:
            return nums[start]
        pre = nums[start]
        cur = max(nums[start],nums[start + 1])
        for i in range(start + 2,end + 1):
            tmp = cur
            cur = max(pre + nums[i],cur)
            pre = tmp
        return cur