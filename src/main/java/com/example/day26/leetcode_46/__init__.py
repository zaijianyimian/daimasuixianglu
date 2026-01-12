from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return []
        self.backtrack(nums,[],res)
        return res
    def backtrack(self,nums : list[int],path : list[int],res : list[list[int]]) -> None:
        if len(path) == len(nums):
            res.append(path.copy())
            return
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.backtrack(nums,path,res)
            path.pop()