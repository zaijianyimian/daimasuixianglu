from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = list()
        if len(nums) < 4:
            return ans
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] > target and nums[i] >= 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n):
                if nums[i] + nums[j] > target and nums[i] + nums[j] >= 0:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                tmp = nums[i] + nums[j]
                l = j + 1
                r = n - 1
                while l < r:
                    if nums[l] + nums[r] + tmp > target:
                        r -= 1
                    elif nums[l] + nums[r] + tmp < target:
                        l += 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:l += 1
                        while r < l and nums[r] == nums[r - 1]:r -= 1
                        r -= 1
                        l += 1
                while j < n - 1 and nums[j] == nums[j + 1]:
                    j += 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
        return ans