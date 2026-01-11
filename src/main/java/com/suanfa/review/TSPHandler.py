class Solution:
    def __init__(self, graph: dict):
        """
        初始化TSP求解器

        Args:
            graph: 图的邻接矩阵表示，graph[i][j]表示城市i到城市j的距离
        """
        self.n = len(graph)
        self.dist = graph  # 距离矩阵
        self.memo = {}  # 记忆化存储，避免重复计算
        self.INF = float("inf")  # 无穷大值

    def solve(self) -> int:
        """
        解决TSP问题，返回最短路径长度

        Returns:
            最短哈密顿回路的总距离
        """
        allCity = set(range(self.n))  # 所有城市的集合 {0, 1, 2, ..., n-1}
        minCost = self.INF  # 初始化最小成本为无穷大

        # 尝试从城市0出发，访问其他城市后回到城市0
        for i in range(1, self.n):  # i表示最后一个访问的城市
            curSet = allCity.copy()  # 当前待访问城市集合
            # 计算从城市0经过其他所有城市到达城市i的最短路径
            pathCost = self.dfs(i, curSet)
            # 加上从城市i回到起点城市0的距离
            returnCost = self.dist[i][0]
            minCost = min(minCost, pathCost + returnCost)

        return minCost

    def dfs(self, current_city: int, remaining_cities: set) -> int:
        """
        使用动态规划和记忆化搜索计算最短路径

        Args:
            current_city: 当前所在城市
            remaining_cities: 剩余待访问的城市集合

        Returns:
            从起点城市0开始，经过remaining_cities中的所有城市，
            最终到达current_city的最短路径长度
        """
        # 如果只剩下当前城市未访问，则检查是否是起点城市0
        if len(remaining_cities) == 1:
            if current_city == 0:  # 如果当前城市就是起点0
                return 0
            else:
                return self.INF  # 不可能的情况

        # 创建状态键用于记忆化
        state_key = (current_city, frozenset(remaining_cities))
        if state_key in self.memo:
            return self.memo[state_key]

        # 移除当前城市，得到之前的剩余城市集合
        prev_cities = remaining_cities.copy()
        prev_cities.remove(current_city)

        min_cost = self.INF

        # 尝试从之前任何一个城市到达当前城市
        for prev_city in prev_cities:
            # 递归计算到达prev_city的最短路径
            cost = self.dfs(prev_city, prev_cities)
            if cost != self.INF:
                # 加上从prev_city到current_city的距离
                total_cost = cost + self.dist[prev_city][current_city]
                min_cost = min(min_cost, total_cost)

        # 存储计算结果到记忆化字典
        self.memo[state_key] = min_cost
        return min_cost


# 使用示例
if __name__ == "__main__":
    # 示例图：完全图，4个城市
    graph = [
        [0, 10, 15, 20],  # 从城市0到其他城市的距离
        [10, 0, 35, 25],  # 从城市1到其他城市的距离
        [15, 35, 0, 30],  # 从城市2到其他城市的距离
        [20, 25, 30, 0]  # 从城市3到其他城市的距离
    ]

    solution = Solution(graph)
    result = solution.solve()
    print(f"最短TSP路径长度: {result}")
