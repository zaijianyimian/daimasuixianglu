def main():
    import sys
    input  = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    total_sum = 0
    vec = []
    for i in range(n):
        row = []
        for j in range(m):
            num = int(data[idx])
            idx += 1
            row.append(num)
            total_sum += num
        vec.append(row)
    heng = [0] * n
    for i in range(n):
        for j in range(m):
            heng[i] += vec[i][j]
    zong = [0] * m
    for j in range(m):
        for i in range(n):
            zong[j] += vec[i][j]
    res = float('inf')
    cur = 0
    for i in range(n):
        cur += heng[i]
        res = min(res,abs(total_sum - 2 * cur))
    cur = 0
    for i in range(m):
        cur += zong[i]
        res = min(res,abs(total_sum - 2 * cur))
    print(res)
if __name__ == '__main__':
    main()
