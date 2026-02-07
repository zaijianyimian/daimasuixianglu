from typing import List

directions = [
    [0,1],
    [1,0],
    [0,-1],
    [-1,0]
]
def dfs(grid:List[List[int]],visited:List[List[bool]],x:int,y:int):
    if visited[x][y]:
        return
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny]:
            if grid[nx][ny] >= grid[x][y]:
                dfs(grid, visited, nx, ny)

def main():
    m,n = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(m)]
    left_up = [[False for _ in range(n)] for _ in range(m)]
    right_down = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        if not left_up[i][0]:
            dfs(grid, left_up, i, 0)
    for j in range(n):
        if not left_up[0][j]:
            dfs(grid, left_up, 0, j)
    for i in range(m):
        if not right_down[i][n - 1]:
            dfs(grid, right_down, i, n - 1)
    for j in range(n):
        if not right_down[m - 1][j]:
            dfs(grid, right_down, m - 1, j)

    print_tag(left_up,right_down)
def print_tag(lef:List[List[bool]],rig:List[List[bool]]):
    for i in range(len(lef)):
        for j in range(len(lef[0])):
            if lef[i][j] and rig[i][j]:
                print(f"{i} {j}")

if __name__ == "__main__":
    main()