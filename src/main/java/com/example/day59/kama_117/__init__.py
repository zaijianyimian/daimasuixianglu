from collections import defaultdict, deque


def topologicalSort(n,edges):
    inDegree = [0 for _ in range(n)]
    umap = defaultdict(list)
    for s,t in edges:
        umap[s].append(t) # s->t
        inDegree[t] += 1
    queue = deque([i for i in range(n) if inDegree[i] == 0])
    result  = []
    while queue:
        cur = queue.popleft()
        result.append(cur)
        for file in umap[cur]:
            inDegree[file] -= 1
            if inDegree[file] == 0:
                queue.append(file)
    if len(result) == n:
        print(" ".join(map(str,result)))
    else:
        print("-1")
if __name__ == "__main__":
    n,m = map(int,input().split())
    edges = [tuple(map(int,input().split())) for _ in range(m)]
    topologicalSort(n,edges)