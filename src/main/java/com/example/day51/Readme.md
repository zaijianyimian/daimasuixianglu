# 图的理论基础
有向图，无向图，权值
度：入度，出度 针对有向图来说的，
连通图： 无向图情况下考虑连通性，图里面任何一个节点都可以到达其他节点
强连通图：
联通分量指的是在图中的极大联通分量
图的构造：
1. 邻接矩阵
2. 邻接表
节点多边少适合用邻接表
图的遍历：
1. dfs
2. bfs
# 深度优先搜索：
不撞南墙不回头
# 广度优先搜索
按照广度一圈圈发散搜索
深度优先搜索：
1. 确定终止条件：栈溢出在终止条件，最终存放结果
2. 处理节点：找下一步方向，回溯，撤销处理结果，
# 可达路径：
节点1到节点n的所有路径，
输入n,m：
1. 创建一个二维邻接矩阵，n + 1 大小
2. 输入m条边，graph[a][b] = 1
3. 一维数组，存放单一结果，二维数组，存放最终结果
4. 确定递归函数：graph，x,y:终点
5. 终止条件：if x == n{
6. path.add(x),return,
7. for: 遍历当前连接节点的连接的所有节点
8. for i in range(1,n + 1):
9. if graph[x][i] == 1:
10. path.add(i)
11. dfs(graph,i,n)
12. path.remove(i)
# 广度优先搜索：
利用队列实现，对顺时针遍历，逆时针遍历没有要求
void bfs(int[][] graph,int[][] visited,int x,int n)
directions = [[0,1],[0,-1],[1,0],[-1,0]]
queue = new LinkedList<>();
queue.add(x);
while(!queue.isEmpty()) {
    一直遍历队列
    int cur = queue.poll();
    for(int[] direction : directions) {
        nextx = cur[0] + direction[i][0]
        nexty = cur[1] + direction[i][1]
        if(nextx >= 0 && nextx < n && nexty >= 0 && nexty < n && graph[nextx][nexty] == 1 && visited[nextx][nexty] == 0){
            queue.add(new int[]{nextx,nexty});
            visited[nextx][nexty] = 1;# 重复节点不要加入队列
            path.add(new int[]{nextx,nexty});

    }
}
对应四个方向
判断越界和是否访问过，访问过则不加入队列