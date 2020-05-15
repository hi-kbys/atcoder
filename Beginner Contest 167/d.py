def main():
    import sys
    input = sys.stdin.buffer.readline
    N, K = map(int, input().split())
    A = list(map(lambda x: int(x)-1, input().split()))
    now = 0
    dict_ = {}
    stack = []
    for i in range(N):
        if now not in dict_:
            dict_[now] = A[now]
            stack.append(now)
            now = A[now]
        else:
            idx = stack.index(now)
            mod = i - idx
            break
    idx = idx + (K-idx) % mod
    idx = min(K, idx)
    print(stack[idx]+1)


if __name__ == '__main__':
    main()
