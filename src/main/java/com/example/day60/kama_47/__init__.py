import heapq


class Edge:
    def __init__(self,to,val):
        self.to = to
        self.val = val
def dijkstra(n,m,start,end,edges):
    grid = [[] for _ in range(n+1)]
    for p1,p2,val in edges:
        grid[p1].append(Edge(p2,val))
    minDist = [float('inf')] * (n+1)
    visited = [False] * (n+1)
    pq = []
    heapq.heappush(pq,(0,start))
    minDist[start] = 0
    while pq:
        curDist,curNode = heapq.heappop(pq)
        if visited[curNode]:
            continue
        visited[curNode] = True
        for edge in grid[curNode]:
            if not visited[edge.to] and curDist + edge.val < minDist[edge.to]:
                minDist[edge.to] = curDist + edge.val
                heapq.heappush(pq,(minDist[edge.to],edge.to))
    return -1 if minDist[end] == float('inf') else minDist[end]
if __name__=='__main__':
    n,m = map(int,input().split())
    edges = [tuple(map(int,input().split())) for _ in range(m)]
    start = 1
    end = n
    print(dijkstra(n,m,start,end,edges))