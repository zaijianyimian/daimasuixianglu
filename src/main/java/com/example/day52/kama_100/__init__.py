from typing import List

directions = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(graph:List[List[int]],visited:List[List[bool]],x:int,y:int) -> int:
    if visited[x][y] or graph[x][y] == 0:
        return 0
    visited[x][y] = True
    count = 1
    for i,j in directions:
        next_x = x + i
        next_y = y + j
        if next_x < 0 or next_x >= len(graph) or next_y < 0 or next_y >= len(graph[0]):
            continue
        if not visited[next_x][next_y] and graph[next_x][next_y] == 1:
            visited[x][y] = True
            count += dfs(graph,visited,next_x,next_y)
    return count


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
                count = dfs(grid,visited,i,j)
                res = max(res,count)
    print(res)