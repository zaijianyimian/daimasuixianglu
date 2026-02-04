from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        res = 0
        for i in range(1,len(height)):
            if height[i] < height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    mid_height = height[stack[-1]]
                    stack.pop()
                    if stack:
                        right = height[i]
                        left = height[stack[-1]]
                        h = min(left,right) - mid_height
                        w = i - stack[-1] - 1
                        res += h * w
                stack.append(i)
        return res