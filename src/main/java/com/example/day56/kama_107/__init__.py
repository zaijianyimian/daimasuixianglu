class Solution:
    def __init__(self,size):
        self.parent = list(range(size + 1)) # 创建并查集
    def find(self,u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self,u,v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            self.parent[rootU] = rootV
    def isSameSet(self,u,v):
        return self.find(u) == self.find(v)
def main():
    m,n = map(int,input().split())
    graph = Solution(m)
    for _ in range(n):
        u,v = map(int,input().split())
        graph.union(u,v)
    source,direction = map(int,input().split())
    if graph.isSameSet(source,direction):
        print(1)
    else:
        print(0)
if __name__ == '__main__':
    main()
