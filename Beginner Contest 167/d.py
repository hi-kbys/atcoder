import sys
input = sys.stdin.buffer.readline
N, K = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
now = 0
dict_ = {}
stack = []
for i in range(N):
    if not now in dict_:
        dict_[now] = A[now]
        stack.append(now)
        now = A[now]
    else:
        idx = stack.index(now)
        break
if K <= idx:
    print(stack[K-1]+1)
else:
    mod = len(stack[idx:])
    idx = idx + (K-idx) % mod
    print(stack[idx]+1)