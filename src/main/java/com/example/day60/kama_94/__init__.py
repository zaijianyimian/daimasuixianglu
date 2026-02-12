def main():
    n,m = map(int,input().strip().split())
    edges = []
    for _ in range(m):
        src,des,val = map(int,input().split())
        edges.append([src,des,val])
    minDist = [float("inf")] * (n + 1)
    minDist[1] = 0
    for i in range(1,n):
        updated = False
        for src,des,weig in edges:
            if minDist[src] != float('inf') and minDist[des] > minDist[src] + weig:
                minDist[des] = minDist[src] + weig
                updated = True
        if not updated:
            break
    if minDist[-1] == float('inf'):
        return "unconnected"
    return minDist[-1]
if __name__ == '__main__':
    print(main())