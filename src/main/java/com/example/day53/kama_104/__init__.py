from typing import List

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
area = 0

def dfs(grid: List[List[int]], visited: List[List[bool]], x: int, y: int, num: int) -> None:
    global area
    if visited[x][y]:
        return
    visited[x][y] = True
    grid[x][y] = num
    area += 1
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
            dfs(grid, visited, nx, ny, num)

def main():
    global area
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    rec = {}
    cnt = 2

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                area = 0
                dfs(grid, visited, i, j, cnt)
                rec[cnt] = area
                cnt += 1

    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                max_island = 1
                seen = set()
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > 1:
                        island_id = grid[ni][nj]
                        if island_id not in seen:
                            max_island += rec[island_id]
                            seen.add(island_id)
                ans = max(ans, max_island)

    if ans == 0:
        ans = max(rec.values()) if rec else 0

    print(ans)

if __name__ == "__main__":
    main()
