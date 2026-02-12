def dijkstra(n,m,edges,start,end):
    grid = [[float('inf')] * (n+1) for _ in range(n+1)]
    for p1,p2,val  in edges:
        grid[p1][p2] = val

    minDist = [float('inf')] * (n+1)
    visited = [False] * (n+1)
    minDist[start] = 0
    for _ in range(1,n + 1):
        minVal = float('inf')
        cur = -1

        for v in range(1,n + 1):
            if not visited[v] and minDist[v] < minVal:
                minVal = minDist[v]
                cur = v
        if cur == -1:
            break
        visited[cur] = True
        for v in range(1,n + 1):
            if not visited[v] and grid[cur][v] != float('inf') and minDist[cur] + grid[cur][v] < minDist[v]:
                minDist[v] = minDist[cur] + grid[cur][v]
    return -1 if minDist[end] == float('inf') else minDist[end]
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        p1 = int(data[index])
        p2 = int(data[index+1])
        val = int(data[index+2])
        edges.append([p1,p2,val])
        index += 3
    start = 1
    end = n
    res = dijkstra(n,m,edges,start,end)
    print(res)