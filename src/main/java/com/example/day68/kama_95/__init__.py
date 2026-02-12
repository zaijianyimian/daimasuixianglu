from collections import deque
from math import inf

# 这个好像过不了
def main():
    n, m = [int(i) for i in input().split()]
    graph = [[] for _ in range(n + 1)]
    min_dist = [inf for _ in range(n + 1)]
    count = [0 for _ in range(n + 1)]
    for _ in range(m):
        s, t, v = [int(i) for i in input().split()]
        graph[s].append([t, v])

    min_dist[1] = 0
    count[1] = 1
    d = deque([1])
    flag = False

    while d:
        cur_node = d.popleft()
        for next_node, val in graph[cur_node]:
            if min_dist[next_node] > min_dist[cur_node] + val:
                min_dist[next_node] = min_dist[cur_node] + val
                count[next_node] += 1
                if next_node not in d:
                    d.append(next_node)
                if count[next_node] == n:
                    flag = True
        if flag:
            break

    if flag:
        print("circle")
    else:
        if min_dist[-1] == inf:
            print("unconnected")
        else:
            print(min_dist[-1])


if __name__ == "__main__":
    main()