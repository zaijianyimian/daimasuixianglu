def main():
    n,m = map(int,input().split())
    edges = list()
    for _ in range(m):
        edges.append(list(map(int,input().split())))
    start,end,k = map(int,input().split())
    minDist = [float('inf')]*(n+1)
    minDist[start] = 0
    for _ in range(k + 1):
        update = False
        minDistCopy = minDist.copy()
        for src,desc,w in edges:
            if minDistCopy[src] != float('inf') and minDistCopy[src] + w < minDist[desc]:
                minDist[desc] = minDistCopy[src] + w
                update = True
        if not update:
            break
    if minDist[end] == float('inf'):
        print("unreachable")
    else:
        print(minDist[end])
main()