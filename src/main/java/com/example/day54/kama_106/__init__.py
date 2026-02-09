def main():
    m, n = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    for i in range(m):
        row = list(map(int, input().split()))
        for j in range(n):
            graph[i][j] = row[j]
    num = bfs(graph)
    print(num)

def bfs(graph):
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
               if i == 0:
                    count += 1
               if j == 0:
                    count += 1
               if i == len(graph) - 1:
                    count += 1
               if j == len(graph[i]) - 1:
                    count += 1
               if i > 0 and graph[i - 1][j] == 0:
                    count += 1
               if j > 0 and graph[i][j - 1] == 0:
                    count += 1
               if i < len(graph) - 1 and graph[i + 1][j] == 0:
                    count += 1
               if j < len(graph[i]) - 1 and graph[i][j + 1] == 0:
                    count += 1
    return count
if __name__ == '__main__':
    main()