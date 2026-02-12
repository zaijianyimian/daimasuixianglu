import collections


def main():
    n,m = map(int,input().split())
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        src,des,val = map(int,input().split())
        edges[src].append([des,val])
    minDist = [float('inf')] * (n+1)
    minDist[1] = 0
    que = collections.deque([1])
    visited = [False] * (n+1)
    visited[1] = True
    while que:
        cur = que.popleft()
        visited[cur] = False
        for dest,val in edges[cur]:
            if minDist[cur] != float('inf') and minDist[cur] + val < minDist[dest]:
                minDist[dest] = minDist[cur] + val
                if not visited[dest]:
                    que.append(dest)
                    visited[dest] = True
    if minDist[n] == float('inf'):
        print("unconnected")
    else:
        print(minDist[n])
main()
