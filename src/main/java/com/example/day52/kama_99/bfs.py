from collections import deque
from typing import List

directions = [[0,1],[0,-1],[-1,0],[1,0]]
def bfs(grid:List[List[int]],visited: List[List[bool]],x : int,y : int) -> None:
    queue = deque([])
    queue.append([x,y])
    visited[x][y] = True
    while queue:
        curx,cury = queue.popleft()
        for i, j in directions:
            nextx = curx + i
            nexty = cury + j
            if nextx < 0 or nexty < 0 or nexty >= len(grid[0]) or nextx >= len(grid): # 一定要记得是大于等于
                continue
            if not visited[nextx][nexty] and grid[nextx][nexty] == 1:
                visited[nextx][nexty] = True
                queue.append([nextx,nexty])
if __name__ == '__main__':
    n,m = map(int,input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int,input().split())))
    visited = [[False] * m for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 1:
                res += 1
                bfs(grid,visited,i,j)
    print(res)
