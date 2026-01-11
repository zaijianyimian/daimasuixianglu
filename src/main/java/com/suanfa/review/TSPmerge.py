class TspDivideConquer:
    def __init__(self, graph):
        """
        初始化TSP分治求解器

        Args:
            graph: 图的邻接矩阵表示，graph[i][j]表示城市i到城市j的距离
        """
        self.graph = graph
        self.n = len(graph)
        self.inf = float('inf')

    def solveTsp(self) -> float:
        """
        解决TSP问题，返回最短路径长度

        Returns:
            最短哈密顿回路的总距离
        """
        cities = list(range(self.n))
        # 从城市0开始的TSP
        minPathLength = self.inf

        # 尝试从城市0出发，连接所有城市后回到城市0
        for endCity in range(1, self.n):
            # 计算从城市0出发，经过所有城市到endCity的最短路径
            remainingCities = [city for city in cities if city != endCity]
            pathLength = self.divideAndConquerTsp([0], remainingCities, endCity)

            # 加上从endCity回到起始城市0的距离
            if pathLength != self.inf:
                pathLength += self.graph[endCity][0]
                minPathLength = min(minPathLength, pathLength)

        return minPathLength if minPathLength != self.inf else -1

    def divideAndConquerTsp(self, visitedPath, remainingCities, targetEndCity):
        """
        使用分治思想解决TSP的子问题

        Args:
            visitedPath: 已经访问的路径
            remainingCities: 剩余待访问的城市
            targetEndCity: 目标终点城市

        Returns:
            从当前路径到目标终点的最短距离
        """
        # 基本情况：如果没有剩余城市，检查是否到达目标终点
        if not remainingCities:
            lastCity = visitedPath[-1]
            return self.graph[lastCity][targetEndCity] if lastCity != targetEndCity else 0

        # 尝试将剩余城市分成两部分
        if len(remainingCities) == 1:
            # 只剩一个城市，直接连接
            nextCity = remainingCities[0]
            lastVisited = visitedPath[-1]
            distanceToNext = self.graph[lastVisited][nextCity]

            # 递归处理剩下的路径
            newPath = visitedPath + [nextCity]
            newRemaining = [city for city in remainingCities if city != nextCity]
            subResult = self.divideAndConquerTsp(newPath, newRemaining, targetEndCity)

            return distanceToNext + subResult if subResult != self.inf else self.inf

        # 分治策略：选择一个城市加入路径，递归解决剩余问题
        minDistance = self.inf

        # 尝试将每一个剩余城市作为下一个访问的城市
        for i, nextCity in enumerate(remainingCities):
            lastVisited = visitedPath[-1]

            # 计算从最后访问的城市到下一个城市的距离
            distance = self.graph[lastVisited][nextCity]

            if distance != self.inf:
                # 更新路径和剩余城市列表
                newVisitedPath = visitedPath + [nextCity]
                newRemainingCities = remainingCities[:i] + remainingCities[i + 1:]

                # 递归计算剩余部分的TSP
                subResult = self.divideAndConquerTsp(newVisitedPath, newRemainingCities, targetEndCity)

                if subResult != self.inf:
                    totalDistance = distance + subResult
                    minDistance = min(minDistance, totalDistance)

        return minDistance if minDistance != self.inf else self.inf

    def solveWithAllStartPoints(self) -> float:
        """
        尝试从所有可能的起始点解决TSP问题

        Returns:
            最短哈密顿回路的总距离
        """
        minTotalDistance = self.inf

        # 尝试从每个城市开始
        for startCity in range(self.n):
            # 重新组织城市列表，使startCity为第一个
            cities = list(range(self.n))
            cities.remove(startCity)
            cities = [startCity] + cities

            # 计算从startCity出发的最短TSP路径
            remainingCities = cities[1:]
            minDistance = self.inf

            for endCity in remainingCities:
                otherCities = [city for city in remainingCities if city != endCity]
                pathDistance = self.divideAndConquerTsp([startCity], otherCities, endCity)

                if pathDistance != self.inf:
                    totalDistance = pathDistance + self.graph[endCity][startCity]
                    minDistance = min(minDistance, totalDistance)

            if minDistance != self.inf:
                minTotalDistance = min(minTotalDistance, minDistance)

        return minTotalDistance if minTotalDistance != self.inf else -1


def findOptimalTspPath():
    """
    使用分治算法求解TSP问题的示例
    """
    # 示例图：完全图，4个城市
    graph = [
        [0, 10, 15, 20],  # 从城市0到其他城市的距离
        [10, 0, 35, 25],  # 从城市1到其他城市的距离
        [15, 35, 0, 30],  # 从城市2到其他城市的距离
        [20, 25, 30, 0]  # 从城市3到其他城市的距离
    ]

    tspSolver = TspDivideConquer(graph)
    result = tspSolver.solveTsp()

    print(f"最短TSP路径长度: {result}")

    # 测试另一种求解方法
    result2 = tspSolver.solveWithAllStartPoints()
    print(f"从所有起始点考虑的最短TSP路径长度: {result2}")


if __name__ == "__main__":
    findOptimalTspPath()
