import heapq
from typing import List, Tuple


class TspBranchBound:
    def __init__(self, graph: List[List[int]]):
        """
        初始化TSP分支界限求解器

        Args:
            graph: 图的邻接矩阵表示
        """
        self.graph = graph
        self.n = len(graph)
        self.inf = float('inf')

    def reduceMatrix(self, matrix: List[List[float]]) -> Tuple[List[List[float]], float]:
        """
        矩阵约简：将邻接矩阵约简以获得下界

        Args:
            matrix: 待约简的矩阵

        Returns:
            约简后的矩阵和约简常数（下界贡献）
        """
        reduced_matrix = [row[:] for row in matrix]  # 深拷贝
        reduction_cost = 0.0

        # 行约简：每行减去最小值
        for i in range(len(reduced_matrix)):
            min_val = self.inf
            for j in range(len(reduced_matrix[i])):
                if reduced_matrix[i][j] < min_val:
                    min_val = reduced_matrix[i][j]

            if min_val != self.inf and min_val != 0:
                reduction_cost += min_val
                for j in range(len(reduced_matrix[i])):
                    if reduced_matrix[i][j] != self.inf:
                        reduced_matrix[i][j] -= min_val

        # 列约简：每列减去最小值
        for j in range(len(reduced_matrix[0])):
            min_val = self.inf
            for i in range(len(reduced_matrix)):
                if reduced_matrix[i][j] < min_val:
                    min_val = reduced_matrix[i][j]

            if min_val != self.inf and min_val != 0:
                reduction_cost += min_val
                for i in range(len(reduced_matrix)):
                    if reduced_matrix[i][j] != self.inf:
                        reduced_matrix[i][j] -= min_val

        return reduced_matrix, reduction_cost

    def calculateLowerBound(self, matrix: List[List[float]], path: List[int]) -> float:
        """
        计算当前路径的下界

        Args:
            matrix: 约简后的邻接矩阵
            path: 当前已确定的路径

        Returns:
            下界值
        """
        # 先对矩阵进行约简
        reduced_matrix, base_cost = self.reduceMatrix(matrix)

        # 计算路径中边的代价
        path_cost = 0
        for i in range(len(path) - 1):
            path_cost += self.graph[path[i]][path[i + 1]]

        return base_cost + path_cost

    def branchAndBoundTsp(self) -> Tuple[float, List[int]]:
        """
        使用分支界限法求解TSP问题

        Returns:
            (最短路径长度, 最优路径)
        """
        # 初始化距离矩阵，将已访问的路径设为无穷大
        initial_matrix = [row[:] for row in self.graph]

        # 优先队列：(下界, 当前路径, 已访问城市集合, 当前代价)
        pq = []

        # 从城市0开始
        initial_lower_bound = self.calculateLowerBound(initial_matrix, [0])
        heapq.heappush(pq, (initial_lower_bound, [0], {0}, 0))

        best_cost = self.inf
        best_path = []

        while pq:
            lower_bound, current_path, visited, current_cost = heapq.heappop(pq)

            # 剪枝：如果当前下界已经超过已知最优解，则跳过
            if lower_bound >= best_cost:
                continue

            # 如果所有城市都已访问，检查是否能回到起点
            if len(visited) == self.n:
                final_cost = current_cost + self.graph[current_path[-1]][0]
                if final_cost < best_cost:
                    best_cost = final_cost
                    best_path = current_path + [0]  # 回到起点
                continue

            # 分支：尝试访问下一个未访问的城市
            current_city = current_path[-1]
            for next_city in range(self.n):
                if next_city not in visited:
                    # 创建新的约束矩阵
                    new_matrix = [row[:] for row in initial_matrix]

                    # 设置已访问路径的边为无穷大
                    for i in range(len(current_path)):
                        if i < len(current_path) - 1:
                            new_matrix[current_path[i]][current_path[i + 1]] = self.inf

                    # 设置不能走的路径为无穷大
                    for i in range(self.n):
                        new_matrix[current_city][i] = self.inf  # 从当前城市不能再出发
                        new_matrix[i][next_city] = self.inf  # 到达下一城市后不能再到达

                    # 计算新的下界
                    new_path = current_path + [next_city]
                    new_visited = visited.copy()
                    new_visited.add(next_city)
                    new_cost = current_cost + self.graph[current_city][next_city]

                    new_lower_bound = self.calculateLowerBound(new_matrix, new_path)

                    # 如果下界仍然有希望，则加入队列
                    if new_lower_bound < best_cost:
                        heapq.heappush(pq, (new_lower_bound, new_path, new_visited, new_cost))

        return best_cost, best_path[:-1]  # 移除重复的起点

    def solve(self) -> Tuple[float, List[int]]:
        """
        解决TSP问题的入口函数

        Returns:
            (最短路径长度, 最优路径)
        """
        return self.branchAndBoundTsp()


# 使用示例
def solveTspWithBranchBound():
    """
    使用分支界限法求解TSP问题的示例
    """
    # 示例图：完全图，4个城市
    graph = [
        [0, 10, 15, 20],  # 从城市0到其他城市的距离
        [10, 0, 35, 25],  # 从城市1到其他城市的距离
        [15, 35, 0, 30],  # 从城市2到其他城市的距离
        [20, 25, 30, 0]  # 从城市3到其他城市的距离
    ]

    tspSolver = TspBranchBound(graph)
    minCost, optimalPath = tspSolver.solve()

    print(f"最短TSP路径长度: {minCost}")
    print(f"最优路径: {optimalPath}")

    # 验证路径
    if optimalPath:
        total_distance = 0
        path_str = ""
        for i in range(len(optimalPath)):
            path_str += str(optimalPath[i])
            if i < len(optimalPath) - 1:
                path_str += " -> "
                total_distance += graph[optimalPath[i]][optimalPath[i + 1]]
        # 加上回到起点的距离
        total_distance += graph[optimalPath[-1]][optimalPath[0]]
        path_str += f" -> {optimalPath[0]} (回起点)"

        print(f"路径详情: {path_str}")
        print(f"总距离（含回起点）: {total_distance}")


if __name__ == "__main__":
    solveTspWithBranchBound()

