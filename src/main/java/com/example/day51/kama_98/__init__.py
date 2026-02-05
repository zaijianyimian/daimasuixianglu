from typing import List


def dfs(graph:List[List[int]],x : int,n : int ,path: List[int],res : List[List[int]]):
    if x == n:
        res.append(path.copy())
        return
    for i in range(1,n + 1):
        if graph[x][i] == 1:
            path.append(i)
            dfs(graph,i,n,path,res)
            path.pop()
def main():
    n,m = map(int,input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a][b] = 1
    res = []
    dfs(graph,1,n,[1],res)
    if not res:
        print(-1)
    else:
        for path in res:
            print(' '.join(map(str,path)))
if __name__ == '__main__':
    main()