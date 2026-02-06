from typing import List

directions = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(graph: List[List[int]], visited: List[List[bool]], x: int, y: int) -> None:
    if visited[x][y] or graph[x][y] == 0:
        return
    visited[x][y] = True
    for i,j in directions:
        next_x = x + i
        next_y = y + j
        if next_x < 0 or next_x >= len(graph) or next_y < 0 or next_y >= len(graph[0]):
            continue
        dfs(graph,visited,next_x,next_y)
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
                dfs(grid,visited,i,j)
    print(res)