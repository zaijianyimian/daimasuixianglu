class Solution:
    def bag(self,val : list[int],weight: list[int],capacity: int) -> list[list[int]]:
        m,n = len(val),capacity
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1,m + 1):
            for c in range(1,n + 1):
                if weight[i - 1] > c:
                    dp[i][c] = dp[i - 1][c]
                else:
                    dp[i][c] = max(dp[i - 1][c],dp[i][c - weight[i - 1]] + val[i - 1])
        return dp
    def print(self,dp : list[list[int]]) -> None:
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                print(dp[i][j],end = " ")
            print()
if __name__ == "__main__":
    s = Solution()
    weight = [3, 2, 1, 4, 5]
    val = [25, 20, 15, 40, 50]
    capacity = 6
    s.print(s.bag(val,weight, capacity))