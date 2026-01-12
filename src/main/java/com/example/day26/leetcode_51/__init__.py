from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr = [["."] * n for _ in range(n)]
        res = []
        self.dfs(arr, 0, res, n)
        return res

    def dfs(self, arr: List[List[str]], row: int, res: List[List[str]], n: int):
        if row == n:
            # 复制当前棋盘状态
            res.append([''.join(r[:]) for r in arr])
            return
        for col in range(n):
            if self.isValid(arr, row, col, n):
                arr[row][col] = "Q"
                self.dfs(arr, row + 1, res, n)
                arr[row][col] = "."

    def isValid(self, arr: List[List[str]], row: int, col: int, n: int) -> bool:
        # 检查列
        for i in range(row):
            if arr[i][col] == 'Q':
                return False

        # 检查左上对角线
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if arr[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # 检查右上对角线
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if arr[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True
