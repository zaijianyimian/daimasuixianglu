from typing import List


class Solution:
    def search(self,nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        index = -1
        while l <= r:
            # 必须//整除,否则就会变为小数,与java中不同
            mid = (l + r) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return index