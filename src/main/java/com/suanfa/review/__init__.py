from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        n = len(A)
        self.dfs(n,A,B,C)

    def move(self, src: list[int], tar:list[int]):
        pan = src.pop()
        tar.append(pan)

    def dfs(self,i : int,src : list[int],buf : list[int],tar:list[int]):
        if i == 1:
            self.move(src,tar)
            return
        self.dfs(i - 1,src,tar,buf)
        self.move(src,tar)
        self.dfs(i - 1,buf,src,tar)


