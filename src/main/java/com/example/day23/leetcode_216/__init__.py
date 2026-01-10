from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.dfs(k,n,1,[],ans)
        return ans
    def dfs(self,k : int ,n : int ,start: int,path: list[int],ans : list[list[int]]) -> None:
        if n < 0 or k < 0 or start > 9:
            return
        if k == 0 and n == 0:
            ans.append(path.copy())
        for i in range(start,10):
            path.append(i)
            self.dfs(k - 1,n - i,i + 1,path,ans)
            path.pop()
