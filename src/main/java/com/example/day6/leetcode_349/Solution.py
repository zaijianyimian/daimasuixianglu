from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen1 = set(nums1)
        seen2 = set(nums2)
        return self.set_intersection(seen1,seen2)
    def set_intersection(self,seen1,seen2):
        if len(seen1) > len(seen2):
            return self.set_intersection(seen2,seen1)
        return [x for x in seen1 if x in seen2]