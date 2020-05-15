def main():
    import sys
    input = sys.stdin.buffer.readline
    n, k = map(int, input().split())
    d = 60
    to = [[0]*(n) for _ in range(d)]
    to[0] = list(map(lambda x: int(x) - 1, input().split()))
    for i in range(d-1):
        for j in range(n):
            to[i+1][j] = to[i][to[i][j]]
    
    v = 0
    for i in range(d, -1 , -1):
        l = pow(2, i)
        if l <= k:
            v = to[i][v]
            k -= l
    print(v+1)


if __name__ == '__main__':
    main()