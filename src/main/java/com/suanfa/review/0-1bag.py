class Solution:
    def bag(self,val: list[int],weight: list[int],capacity: int) -> list[list[int]]:
        m,n = len(val),capacity
        dp = [[0] * (n + 1) for  _ in range(m + 1)]
        for i in range(1,m + 1):
            curWeight = weight[i - 1]
            curVal = val[i - 1]
            for j in range(1,n + 1):
                if j < curWeight:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j],dp[i - 1][j - curWeight] + curVal)
        return dp
    def print(self,dp: list[list[int]]) -> None:
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