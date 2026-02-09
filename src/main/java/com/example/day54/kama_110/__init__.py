def judge(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count == 1
if __name__ == '__main__':
    n = int(input())
    begin,end = input().split()
    if begin == end:
        print(0)
        exit()
    strlist = []
    for i in range(n):
        strlist.append(input())
    visited = [False for _ in range(n)]
    queue = [[begin,1]]
    while queue:
        cur,step = queue.pop(0)
        if judge(cur,end):
            print(step + 1)
            exit()
        for i in range(n):
            if not visited[i] and judge(strlist[i],cur):
                visited[i] = True
                queue.append([strlist[i],step + 1])
    print(0)