from typing import List

from numpy import sort


class Solution:
    def threeSum(self,nums : List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        for i in range(n):
            if nums[i] > 0:
                return ans
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1;
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1;
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1;
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1;
                    l += 1
                    r -= 1
        return ans
