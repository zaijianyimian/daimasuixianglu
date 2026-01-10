from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums,0,[],res)
        return res
    def dfs(self,nums: list[int],start : int,path: list[int],res:list[list[int]]) -> None:
        res.append(path.copy())
        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums,i + 1,path,res)
            path.pop()

