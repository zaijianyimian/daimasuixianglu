from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.mappint = [
            [''],
            [''],
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
        ]
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return self.ans
        self.dfs(digits,0,"")
        return self.ans
    def dfs(self,digits:str,index:int,path:str):
        if index == len(digits):
            self.ans.append(path)
            return
        for i in self.mappint[int(digits[index])]:
            self.dfs(digits,index+1,path+i)
