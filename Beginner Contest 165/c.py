import sys
from itertools import combinations_with_replacement as cwr
input = sys.stdin.readline

N,M,Q = map(int,input().split())
A,B,C,D = [],[],[],[]
for i in range(Q):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ans = 0
combs = list(cwr(range(1,M+1),N))
ans = [0]*(len(combs))
for i,comb in enumerate(combs):
    for a,b,c,d in zip(A,B,C,D):
        if comb[b-1] - comb[a-1] ==c:
            ans[i] += d
print(max(ans))