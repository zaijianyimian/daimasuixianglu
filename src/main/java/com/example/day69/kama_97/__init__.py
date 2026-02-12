if __name__=='__main__':
    maxInt = 10005
    n,m = map(int,input().split())
    grid = [[[maxInt] * ( n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        grid[u][v][0] = w
        grid[v][u][0] = w
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                grid[i][j][k] = min(grid[i][j][k-1],grid[i][k][k-1] + grid[k][j][k-1])
    z = int(input())
    for _ in range(z):
        start,end = map(int,input().split())
        if grid[start][end][n] == maxInt:
            print(-1)
        else:
            print(grid[start][end][n])