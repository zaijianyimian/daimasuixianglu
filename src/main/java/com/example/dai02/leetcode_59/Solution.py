from typing import List


class Solution:
    def generateMatrix(self,n : int) -> List[List[int]]:
        arr = [[0] * n for _ in range(n)] # 创建一个二维数组
        left,right,top,bottom = 0,n-1,0,n-1
        num,res = 1,n * n
        while num <= res:
            for i in range(left,right + 1):
                arr[top][i] = num
                num += 1
            top += 1
            for i in range(top,bottom + 1):
                arr[i][right] = num
                num += 1
            right -= 1
            for i in range(right,left - 1, -1): # python中要设置步长为-1否则会出错
                arr[bottom][i] = num
                num += 1
            bottom -= 1
            for i in range(bottom,top - 1,-1):
                arr[i][left] = num
                num += 1
            left += 1
        return arr