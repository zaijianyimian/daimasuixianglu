import collections

path = set()
def bfs(root,graph):
    global path
    que = collections.deque([root])
    while que:
        node = que.popleft()
        path.add(node)
        for child in graph[node]:
            que.append(child)
        graph[node] = []
    return
def main():
    n,m = map(int,input().split())
    graph = collections.defaultdict(list)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
    bfs(1,graph)
    if path == {i for i in range(1,n + 1)}:
        return 1
    return -1
if __name__ == '__main__':
    print(main())