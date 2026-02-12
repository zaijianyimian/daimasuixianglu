class Edge:
    def __init__(self,l,r,val):
        self.l = l
        self.r = r
        self.val = val
n = 10001
father = list(range(n))
def init():
    global father
    father = list(range(n))
def find(x):
    if father[x] != x:
        father[x] = find(father[x])
    return father[x]
def join(x,y):
    father[find(x)] = find(y)
def kruskal(v,edges):
    edges.sort(key = lambda edge: edge.val)
    init()
    res = 0
    for edge in edges:
        x = find(edge.l)
        y = find(edge.r)
        if x != y:
            res += edge.val
            join(x,y)
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
        v1 = int(data[index])
        v2 = int(data[index+1])
        val = int(data[index+2])
        edges.append(Edge(v1,v2,val))
        index += 3
    res = kruskal(v,edges)
    print(res)