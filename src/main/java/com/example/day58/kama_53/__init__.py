
def prim(v,e,edges):
    import sys
    import heapq
    grid = [[float('inf')] * (v+1) for _ in range(v+1)]
    for edge in edges:
        x,y,w = edge
        grid[x][y] = w
        grid[y][x] = w
    minDist = [float('inf')] * (v+1)
    isInTree = [False] * (v+1)
    minDist[1] = 0
    for i in range(1,v):
        cur = -1
        minVal = float('inf')
        for j in range(1,v + 1):
            if not isInTree[j] and minDist[j] < minVal:
                cur = j
                minVal = minDist[j]
        isInTree[cur] = True
        for j in range(1,v + 1):
            if not isInTree[j] and grid[cur][j] < minDist[j]:
                minDist[j] = grid[cur][j]

    res = sum(minDist[2:v+1])
    return res
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    v = int(data[0])
    e = int(data[1])

    edges = []
    index = 2
    for _ in range(e):
        x = int(data[index])
        y = int(data[index + 1])
        k = int(data[index + 2])
        edges.append((x, y, k))
        index += 3

    result = prim(v, e, edges)
    print(result)