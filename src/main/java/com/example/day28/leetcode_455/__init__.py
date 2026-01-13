from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = n = 0
        while i < len(s) and j < len(g):
            if g[j] <= s[i]:
                n+=1
                i+=1
                j+=1
            elif g[j] > s[i]:
                i += 1
        return n
