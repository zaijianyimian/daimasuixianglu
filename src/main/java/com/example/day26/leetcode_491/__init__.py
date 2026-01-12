from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums,0,[],res)
        return res
    def dfs(self,nums: list[int],startIndex: int,path: list[int],res : list[list[int]]) -> None:
        if len(path) > 1:
            res.append(path.copy())
        se = set()
        for i in range(startIndex,len(nums)):
            if nums[i] in se or (len(path) != 0 and nums[i] < path[-1]):
                continue
            se.add(nums[i])
            path.append(nums[i])
            self.dfs(nums,i + 1,path,res)
            path.pop()
