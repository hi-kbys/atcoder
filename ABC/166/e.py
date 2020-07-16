import numpy as np
from collections import Counter as cc
N = int(input())
A = list(map(int,input().split()))

ans = 0
A_p = cc(A+np.arange(N))
A_n = cc(np.arange(N) - A)
for k in range(1,N+1):
    ans += A_p[k]*A_n[k]
print(ans)