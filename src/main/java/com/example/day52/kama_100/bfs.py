from collections import deque
from typing import List

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid: List[List[int]], visited: List[List[bool]], x: int, y: int) -> int:
    if visited[x][y] or grid[x][y] == 0:
        return 0
    visited[x][y] = True
    queue = deque([(x, y)])
    count = 1
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                continue
            if not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1
    return count

if __name__ == '__main__':
    try:
        n, m = map(int, input().split())
        assert n > 0 and m > 0
    except (ValueError, AssertionError):
        print("Invalid input")
        exit(1)

    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) != m:
            print("Invalid input")
            exit(1)
        grid.append(row)

    visited = [[False] * m for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 1:
                count = bfs(grid, visited, i, j)
                res = max(res, count)
    print(res)
