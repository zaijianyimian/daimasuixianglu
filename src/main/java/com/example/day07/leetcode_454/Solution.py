from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        ans = 0
        arr = dict()
        for i in range(n):
            for j in range(n):
                if nums1[i] + nums2[j] in arr:
                    arr[nums1[i] + nums2[j]] += 1
                else:
                    arr[nums1[i] + nums2[j]] = 1
        for i in range(n):
            for j in range(n):
                key = -nums4[i] - nums3[j]
                if  key in arr:
                    ans += arr[key]
        return ans
