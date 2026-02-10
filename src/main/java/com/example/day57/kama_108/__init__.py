father = list()
def find(u):
    if father[u] != u:
        father[u] = find(father[u])
    return father[u]
def isSame(u,v):
    return find(u) == find(v)
def union(u,v):
    if not isSame(u,v):
        father[find(u)] = find(v)
if __name__ == '__main__':
    n = int(input())
    for i in range(n + 1):
        father.append(i)
    res = None
    for i in range(n):
        u,v = map(int,input().split())
        if isSame(u,v):
            res = str(u) + " " + str(v)
        else:
            union(u,v)
    print(res)