import numpy as np
N, M, X = map(int, input().split())
C = []
A = np.zeros((N, M), dtype=int)
for i in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A[i] = a

S = np.sum(A, axis=0)
print(A)
print(S)
if True in (S < X):
    print(-1)
    exit(0)

mlt = [0]*12
C_ = []
for i in range(2**N):
    total = 0
    arr = np.zeros((M,), dtype=int)
    for j in range(N):
        # bit 演算！j桁ずらしている。
        if ((i >> j) & 1) == 1:

            total += C[j]
            arr += A[j]
    if True in (arr < X):
        continue
    C_.append(total)
print(min(C_))
