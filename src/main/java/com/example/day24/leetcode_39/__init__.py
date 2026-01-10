from typing import List


class Solution:
    def __init__(self):
        self.ans = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.dfs(candidates,target,[],0)
        return self.ans

    def dfs(self,candidates: List[int], target: int, path: List[int],index:int):
        if target < 0:
            return
        if target == 0:
            self.ans.append(path)
        for i in range(index,len(candidates),1):
            self.dfs(candidates,target-candidates[i],path+[candidates[i]],i)
