from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtrack(n,k,1,[],result)
        return result

    def backtrack(self,n:int ,k : int,startIndex:int,path:list[int],res:list[list[int]]):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(startIndex,n - (k - len(path)) + 2):
            path.append(i)
            self.backtrack(n,k,i+1,path,res)
            path.pop()
