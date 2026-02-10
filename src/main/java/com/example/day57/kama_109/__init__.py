from collections import defaultdict

# 全局变量
father = list()


def find(u):
    # 路径压缩
    if father[u] != u:
        father[u] = find(father[u])
    return father[u]


def isSame(u, v):
    return find(u) == find(v)


def join(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root != v_root:
        father[u_root] = v_root


def init_father(n):
    """辅助函数：初始化并网集数组"""
    global father
    # 修改点 1: 节点是从 1 到 n，所以数组大小需要是 n + 1
    father = [i for i in range(n + 1)]


def isTreeAfterRemoveEdge(edges, edge_index, n):
    """
    判断删除指定下标的边后，剩下的图是否是树（这里主要判断是否还有环）
    """
    init_father(n)  # 每次检查前都要重置并查集

    for i in range(len(edges)):
        if i == edge_index:
            continue
        s, t = edges[i]
        if isSame(s, t):
            return False  # 依然存在环，说明删错边了
        else:
            join(s, t)
    return True


def getRemoveEdge(edges, n):
    """
    处理只有环没有入度为2的情况 (类似于 Redundant Connection I)
    """
    init_father(n)  # 修改点 2: 必须在这里初始化 father

    # 修改点 3: 只需要遍历一次 edges，不需要双重循环
    for s, t in edges:
        if isSame(s, t):
            print(s, t)
            return
        else:
            join(s, t)


if __name__ == "__main__":
    try:
        # 读取 n (通常第一行是节点数/边数)
        line1 = input().strip()
        if not line1:
            exit()
        n = int(line1)

        edges = list()
        inDegree = defaultdict(int)

        for i in range(n):
            line = input().strip()
            if not line:
                break
            s, t = map(int, line.split())
            edges.append((s, t))
            inDegree[t] += 1

        vec = list()
        # 倒序寻找入度为 2 的节点对应的两条边
        # 优先删除靠后的边，所以倒序遍历
        for i in range(n - 1, -1, -1):
            if inDegree[edges[i][1]] == 2:
                vec.append(i)

        # 情况 1: 存在入度为 2 的节点
        if len(vec) > 0:
            # vec[0] 是靠后的那条边，优先尝试删除它
            if isTreeAfterRemoveEdge(edges, vec[0], n):
                print(edges[vec[0]][0], edges[vec[0]][1])
            else:
                # 如果删了 vec[0] 还是不成树（还有环），那就必须删 vec[1]
                print(edges[vec[1]][0], edges[vec[1]][1])
        # 情况 2: 没有入度为 2 的节点，说明只有环
        else:
            getRemoveEdge(edges, n)

    except EOFError:
        pass