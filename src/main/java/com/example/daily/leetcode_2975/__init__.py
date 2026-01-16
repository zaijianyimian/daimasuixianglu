from itertools import combinations
from typing import List, Set

from itertools import combinations
from typing import List, Set


class Solution:
    def f(self, a: List[int], mx: int) -> Set[int]:
        """
        计算数组a中所有元素与边界值(1和mx)组合后，任意两个数之间差值的集合

        Args:
            a: 输入的整数列表
            mx: 最大边界值

        Returns:
            包含所有可能差值的集合
        """
        a += [1, mx]
        a.sort()
        # 计算 a 中任意两个数的差，保存到哈希集合中
        return set(y - x for x, y in combinations(a, 2))

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        """
        计算在给定网格中由水平和垂直栅栏围成的最大正方形面积

        Args:
            m: 网格的行数
            n: 网格的列数
            hFences: 水平栅栏的位置列表
            vFences: 垂直栅栏的位置列表

        Returns:
            最大正方形面积对MOD取模的结果，如果无法形成正方形则返回-1
        """
        MOD = 1_000_000_007
        h_set = self.f(hFences, m)
        v_set = self.f(vFences, n)

        ans = max(h_set & v_set, default=0)
        return ans * ans % MOD if ans else -1






