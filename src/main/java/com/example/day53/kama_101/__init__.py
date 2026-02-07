from typing import List

directions = [[0,1],[0,-1],[1,0],[-1,0]]
def dfs(grid:List[List[int]],visited:List[List[int]],x:int,y:int) -> None:
    if visited[x][y]:
        return
    visited[x][y] = True
    grid[x][y] = 0
    for i,j in directions:
        nextx = x + i
        nexty = y + j
        if nextx < 0 or nextx >= len(grid) or nexty < 0 or nexty >= len(grid[0]):
            continue
        if grid[nextx][nexty] == 0:
            continue
        dfs(grid,visited,nextx,nexty)
    return
def main() :
    m,n = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        if grid[i][0] == 1:
            dfs(grid,visited,i,0)
        if grid[i][n-1] == 1:
            dfs(grid,visited,i,n-1)
    for j in range(n):
        if grid[0][j] == 1:
            dfs(grid,visited,0,j)
        if grid[m-1][j] == 1:
            dfs(grid,visited,m-1,j)
    res = sum(sum(row) for row in grid)
    print(res)
if __name__ == '__main__':
    main()