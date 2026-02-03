from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = nums * 2
        n = len(arr)
        res = [-1] * n
        stack = [0]
        for i in range(1,n * 2):
            if arr[stack[-1]] >= arr[i]:
                stack.append(i)
            else:
                while stack and arr[stack[-1]] < arr[i]:
                    res[stack.pop()] = arr[i]
                stack.append(i)
        return res[:n]