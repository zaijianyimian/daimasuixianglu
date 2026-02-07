from collections import deque
from typing import List

directions = [
    [0,1],
    [1,0],
    [0,-1],
    [-1,0]
]
def bfs(grid:List[List[int]],visited:List[List[int]],nums:List[List[int]],x:int,y:int):
    if visited[x][y]:
        return
    queue = deque([(x,y)])
    visited[x][y] = True
    nums[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                continue
            if visited[nx][ny] or grid[nx][ny] == 0:
                continue
            queue.append((nx,ny))
            visited[nx][ny] = True
            nums[nx][ny] = 1
    return
def main():
    m,n = map(int,input().split())
    # grid = [list(map(int,input().split())) for _ in range(m)]
    grid = [list(map(int,input().split())) for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    nums = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        if grid[i][0] == 1:
            bfs(grid,visited,nums,i,0)
        if grid[i][n-1] == 1:
            bfs(grid,visited,nums,i,n-1)
    for i in range(n):
        if grid[0][i] == 1:
            bfs(grid,visited,nums,0,i)
        if grid[m-1][i] == 1:
            bfs(grid,visited,nums,m-1,i)
    print_grid(nums)
def print_grid(nums:List[List[int]]):
    for row in nums:
        print(' '.join(map(str,row)))

if __name__ == '__main__':
    main()
