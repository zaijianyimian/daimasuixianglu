# 字符串接龙
begin,end = map(str,input().split())
set = set()
map = dict()
queue = collections.deque()
queue.append(begin)
while(queue):
    word = queue.popleft()
    for i in range(len(word)):
        word = word  
        for j in range(26):
             word[i] = chr(ord('a')+j)
              if word in set:
                  continue
                if word == end:
                    print(map[word]+1)
# 有向图完全可达
用邻接表存储
点少变多邻接矩阵
点多边少邻接表
n,m = map(int,input().split())
arr = [[0 for i in range(n)] for j in range(n)]]
while(m - 1 >= 0):
    a,b = map(int,input().split())
