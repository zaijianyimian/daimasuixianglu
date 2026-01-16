from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        side = min(self.longSet(hBars), self.longSet(vBars)) + 1
        return side * side

    def longSet(self,nums : list[int]) -> int:
        st = set(nums)
        ans = 0
        for i in st:
            if i - 1 in st:
                continue
            y = i + 1
            while y in st:
                y += 1
            ans = max(ans,y - i)
        return ans

