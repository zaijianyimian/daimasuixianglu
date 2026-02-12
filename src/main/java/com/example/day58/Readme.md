# 最小生成树 prim算法
最少的边的权值和，
随便选一个节点就可以
非生成树距离生成树节点
将节点加入生成树，更新所有非生成树节点到生成树。
minDist 每一个节点到生成树的距离
n个节点，执行n - 1次，非生成树节点距离生成树的最小距离，
加入到生成树
更新生成树距离
while m > 0:
   val = int(input())
   grid[i][j] = val
   grid[j][i] = val
isInTree = [False] * n
minDist = [float('inf')] * (n + 1)
for i in range(1,n):
  minVal = float('inf')
  cur = 1
  for j in range(1,n + 1):
      if minDist[j] < minVal:
          minVal = minDist[j]
          cur = j
  isInTree[cur] = True
  for j in range(1,n + 1):
      if not isInTree[j] and grid[cur][j] < minDist[j]:
          minDist[j] = grid[cur][j] 
# 最小生成树 kruskal算法
对排完序的边进行排序
如果边两边的节点不在生成树中，加入生成树，更新生成树距离
如果在生成树中，直接就不用这条边
用并查集判断是否在同一个节点等，

