from typing import List


class Solution:

    def __init__(self):
        self.ans = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.dfs(candidates,target,[],0,[False] * len(candidates))
        return self.ans
    def dfs(self,arr:list[int],target:int,path:list[int],index:int,used:list[bool]):
        if target < 0:
            return
        if target == 0:
            self.ans.append(path)
            return
        for i in range(index,len(arr)):
            if used[i]:
                continue
            if i > 0 and arr[i] == arr[i-1] and not used[i - 1]:
                continue
            used[i] = True
            self.dfs(arr,target-arr[i],path+[arr[i]],i+1,used)
            used[i] = False

