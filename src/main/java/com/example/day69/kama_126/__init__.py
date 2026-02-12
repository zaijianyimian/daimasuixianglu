import heapq

moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
def distance(a,b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
def bfs(start,end):
    q = [(distance(start,end),start)]
    step = {start: 0}
    while q:
        d,cur = heapq.heappop(q)
        if cur == end:
            return step[cur]
        for move in moves:
            new = (cur[0] + move[0], cur[1] + move[1])
            if 1 <= new[0] <= 1000 and 1 <= new[1] <= 1000:
                stepNew = step[cur] + 1
                if stepNew < step.get(new, float('inf')):
                    step[new] = stepNew
                    heapq.heappush(q, (stepNew + distance(new, end), new))
    return False

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a1, a2, b1, b2 = map(int, input().split())
        print(bfs((a1, a2), (b1, b2)))
