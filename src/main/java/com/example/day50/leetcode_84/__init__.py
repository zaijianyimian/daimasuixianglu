from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0,0)
        heights.append(0)
        stack = [0]
        res = 0
        for i in range(1,len(heights)):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    if stack:
                       lefind = stack[-1]
                       rigind = i
                       area = h * (rigind - lefind - 1)
                       res = max(res,area)
                stack.append(i)
        return res