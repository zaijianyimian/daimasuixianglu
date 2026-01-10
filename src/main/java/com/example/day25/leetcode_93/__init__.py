from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.backtracking(s,0,0,"",res)
        return res
    def backtracking(self,s : str,startIndex : int,pointNum:int,cur:str,res:list[int]):
        if pointNum == 3:
            if self.isValid(s,startIndex,len(s) - 1):
                cur += s[startIndex:]
                res.append(cur)
            return
        for i in range(startIndex,len(s)):
            if self.isValid(s,startIndex,i):
                self.backtracking(s,i + 1,pointNum + 1,cur + s[startIndex:i + 1]+'.',res)
            else:
                 break
    def isValid(self,s : str,start : int,end : int) -> bool:
        if start > end:
            return False
        if s[start] == "0" and start != end:
            return False
        num = 0
        for i in range(start,end + 1):
            if not s[i].isdigit():
                return False
            num = num * 10 + int(s[i])
            if num > 255:
                return False
        return True