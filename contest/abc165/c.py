import sys
from itertools import combinations_with_replacement as cwr
input = sys.stdin.readline

def dfs(n,m):
    adj = {}
    for i in range(1,m+1):
        adj[i] = [j for j in range(i,m+1)]
    
    stack = [[i] for i in range(1,m+1)]
    combs = []
    while stack:
        node = stack.pop()
        if len(node) == n:
            combs.append(node)
        else:
            for child in adj[node[-1]]:
                cand = node+[child]
                stack.append(cand)
    return combs


N,M,Q = map(int,input().split())
A,B,C,D = [],[],[],[]
for i in range(Q):
    a,b,c,d = map(int,input().split())
    a,b = a-1, b-1
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ans = 0
combs = dfs(N,M)
#combs = cwr(range(1,M+1),N)
# print(combs)
ans = [0]*(len(combs))
for i,comb in enumerate(combs):
    for a,b,c,d in zip(A,B,C,D):
        if comb[b] - comb[a] ==c:
            ans[i] += d
print(max(ans))

