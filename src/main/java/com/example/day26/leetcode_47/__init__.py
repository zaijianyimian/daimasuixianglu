from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [0] * len(nums)
        nums.sort()
        self.dfs(nums,[],used,res)
        return res
    def dfs(self,nums:list[int],path:list[int],used:list[int],res:list[int]) -> None:
        if len(path) == len(nums):
            res.append(path.copy())
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 0:
                continue
            if used[i] == 1:
                continue
            used[i] = 1
            path.append(nums[i])
            self.dfs(nums,path,used,res)
            path.pop()
            used[i] = 0