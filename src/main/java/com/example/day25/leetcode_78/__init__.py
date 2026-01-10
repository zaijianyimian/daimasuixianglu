from typing import List


class Solution:
    def __init__(self):
        self.res = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums,0,[])
        return self.res
    def dfs(self,nums: list[int],start: int,path : list[int]):
        self.res.append(path.copy())
        for i in  range(start,len(nums)):
            path.append(nums[i])
            self.dfs(nums,i+1,path)
            path.remove(nums[i])
